import configparser
import re
import boto3
import pandas as pd
import matplotlib.pyplot as plt

config = configparser.ConfigParser()

config.read("aws.cfg")

aws_access_key = config["AWS"]["ACCESS_KEY"]
aws_secret_key = config["AWS"]["SECRET_KEY"]


s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-east-1'
)
sentiment = boto3.client(
    'comprehend',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-east-1'
)

rekognition = boto3.client(
    'rekognition',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-west-2'
)



states = [
"Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Delaware",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"OH",
"Ohio",
"OK",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Rhode Island",
"South Carolina",
"South Dakota",
"TN",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming"
]

def list_s3_files(bucket_name: str, prefix=""):
    resp = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    files = [item['Key'] for item in resp.get('Contents', [])]
    return files


def read_file(url: str) -> pd.DataFrame:
    return pd.read_csv(url, storage_options={
        'key': aws_access_key,
        'secret': aws_secret_key
    })

def write_csv(df: pd.DataFrame, bucket_name: str, file_name: str):
    url = f's3://{bucket_name}/{file_name}'
    df.to_csv(url, storage_options={
        'key': aws_access_key,
        'secret': aws_secret_key
    })


def upload_fileobj(fpath: str, bucket_name: str, key: str):
    with open(fpath, 'rb') as data:
        s3.upload_fileobj(data, bucket_name, key)
        print(f'{fpath} uploaded to {bucket_name}')


def analyze_text(txt: str) -> str:
    resp = sentiment.detect_sentiment(
        Text=txt,
        LanguageCode='en'
    )
    return resp['Sentiment']


def analyze_col_sentiment(df: pd.DataFrame, col_name: str):
    sent_col = f'{col_name}_sentiment'
    df[sent_col] = [analyze_text(x) for x in df[col_name]]
    df[sent_col].value_counts().plot(kind='bar')
    plt.savefig('sentiment.jpg', format='jpg')


def extract_text_from_image(bucket_name, document_name) -> str:
    resp = rekognition.detect_text(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': document_name}}
    )
    txt = ' '.join([item['DetectedText'] for item in resp['TextDetections']])
    return txt


def extract_state(txt: str) -> str:
    for s in states:
        if s.upper() in txt.upper():
            return s
    return 'Unknown'


def get_license_plate_df(bucket_name: str, prefix="") -> pd.DataFrame:
    files = list_s3_files(bucket_name, prefix)
    print("files: ", files)
    data = []
    for f in files:
        if '.csv' not in f and f != 'resources/license-plates/':
            print('checking file: ', f)
            text = extract_text_from_image(bucket_name, f)
            state = extract_state(text)
            data.append({'Image': f, 'State': state})
    df = pd.DataFrame(data)
    df['State'].value_counts().plot(kind='bar')
    plt.savefig('license_plates.jpg', format='jpg')
    return pd.DataFrame(data)


if __name__ == '__main__':
    bucket_name = "techcatalyst-public"
    write_bucket = "techcatalyst-public"

    # sentiment stuff
    product_url = "s3://techcatalyst-public/resources/sentiment/product.csv"
    review_url = "s3://techcatalyst-public/resources/sentiment/review.csv"
    product_df = read_file(product_url)
    review_df = read_file(review_url)
    print(product_df.head())
    print(review_df.head())

    sentiment_df = product_df.merge(review_df, on='REVIEW ID', how='inner')
    analyze_col_sentiment(sentiment_df, 'REVIEW TEXT')
    print(sentiment_df.head())
    write_csv(sentiment_df, write_bucket, 'jc/product_sentiment.csv')

    # plate stuff
    plates_df = get_license_plate_df(bucket_name, prefix="resources/license-plates")
    print(plates_df.head())
    write_csv(plates_df, write_bucket, "jc/plates.csv")
    upload_fileobj("license_plates.jpg", write_bucket, "jc/license_plates.jpg")
    upload_fileobj("sentiment.jpg", write_bucket, "jc/sentiment.jpg")
