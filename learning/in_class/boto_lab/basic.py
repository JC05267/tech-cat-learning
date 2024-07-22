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
#location = {'LocationConstraint': 'us-east-1'}


def create_bucket():
    s3.create_bucket(
       Bucket=bucket_name,
#       CreateBucketConfiguration=location
    )


def list_buckets():
    response = s3.list_buckets()
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

def upload_file(fpath: str, b_name: str, key: str):
    s3.upload_file(fpath, b_name, key)
    print(f'File {fpath} uploaded to bucket {b_name} with key {key}.')


def upload_fileobj(fpath: str, b_name: str, key: str):
    with open(fpath, 'rb') as data:
        s3.upload_fileobj(data, b_name, key)
        print(f'File {fpath} uploaded to bucket {b_name} with key {key}.')


def put_object(fpath: str, b_name: str, key: str):
    with open(fpath, 'rb') as f:
        s3.put_object(Body=f, Bucket=b_name, Key=key)
        print(f'File {fpath} uploaded to bucket {b_name} with key {key}.')


def download_file(b_name: str, obj_name: str, f_name: str):
    s3.download_file(b_name, obj_name, f_name)
    print(f'File {obj_name} downloaded from bucket {b_name} to {f_name}.')


def download_fileobj(b_name: str, obj_name: str, f_name: str):
    with open(f_name, 'wb') as f:
        s3.download_fileobj(b_name, obj_name, f)
        print(f'File {obj_name} downloaded from bucket {b_name} to {f_name}.')


def get_object(b_name: str, obj_name: str, f_name: str):
    resp = s3.get_object(Bucket=b_name, Key=obj_name)
    content = resp['Body'].read().decode('utf-8')
    print(resp)
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f'File {obj_name} downloaded from bucket {b_name} to {f_name}.')


if __name__ == '__main__':
    create_bucket()
    upload_file('test_files/r1.txt', bucket_name, 'r1.txt')
    upload_fileobj('test_files/r2.txt', bucket_name, 'r2.txt')
    put_object('test_files/r3.txt', bucket_name, 'r3.txt')
    download_file(bucket_name, 'r1.txt', 'downloads/new_r1.txt')
    download_fileobj(bucket_name, 'r2.txt', 'downloads/new_r2.txt')
    get_object(bucket_name, 'r3.txt', 'downloads/new_r3.txt')
