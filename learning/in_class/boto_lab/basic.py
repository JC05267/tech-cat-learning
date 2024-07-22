import configparser
import boto3

config = configparser.ConfigParser()

config.read("aws.cfg")

aws_access_key = config["AWS"]["ACCESS_KEY"]
aws_secret_key = config["AWS"]["SECRET_KEY"]


s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)


response = s3.get_bucket_location(Bucket='techcatalyst-public')
type(response)
response.keys()

bucket_name = "jc-bucket-lab"
location = {'LocationConstraint': 'us-east-1'}

s3.create_bucket(
   Bucket=bucket_name,
   CreateBucketConfiguration=location
)

def upload_files(lst):
    for file in lst:
        s3.upload_file(file, bucket_name, file)

def download_files(lst):
    for file in lst:
        s3.download_file(Bucket=bucket_name,
                         Key=file, Filename=f"downloads/{file}")
