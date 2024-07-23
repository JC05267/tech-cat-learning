import configparser
import boto3
import awswrangler as wr
import pandas as pd

# Import your credentials from your .cfg file
# YOUR CODE

config = configparser.ConfigParser()

config.read("aws.cfg")

aws_access_key = config["AWS"]["ACCESS_KEY"]
aws_secret_key = config["AWS"]["SECRET_KEY"]


s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

bucket_name = "jc-bucket-lab"
location = {'LocationConstraint': 'us-east-1'}


def create_bucket():
    s3.create_bucket(
       Bucket=bucket_name,
       # only include this if the region is NOT us-east-1
       # CreateBucketConfiguration=location
    )
create_bucket()

def list_buckets():
    response = s3.list_buckets()
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

boto3.setup_default_session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-east-1'
)

try:
    df = wr.s3.read_parquet(path="s3://techcatalyst-raw/yellow_tripdata_2024-01.parquet")
except Exception as e:
    print('error')
    print(e)

print(type(df))
print(df.shape)
print(df.head(5))

wr.s3.to_parquet(
    df = df,
    path = "s3://jc-bucket-lab/yellow_trip_data_2024-01.parquet",
    dataset=True,
    mode = "overwrite"
)

databases = wr.catalog.databases()
print(databases)

if "`jc-awswrangler_test`" not in databases.values:
    wr.catalog.create_database(name = 'jc-awswrangler_test')
else:
    print("database already exists")

desc = "This the Taxi table for January, 2024."
param = {"source": "NYC Taxi Web Service https://www.nyc.gov", "class": "e-commerce"}
comments = {
    "tpep_pickup_datetime": "The date and time when the meter was engaged.",
    "PULocationID": "TLC Taxi Zone in which the taximeter was engaged",
    "payment_type": "A numeric code signifying how the passenger paid for the trip",
    "fare_amount": "The time-and-distance fare calculated by the meter.",
}

bucket = "techcatalyst-transformed-glue"

res = wr.s3.to_parquet(
    df=df,
    path=f"s3://{bucket}/jc/nyc/",
    dataset=True,
    database="jc-awswrangler_test",
    table="jcawswrtbl",
    mode="overwrite",
    glue_table_settings=wr.typing.GlueTableSettings(description=desc, parameters=param, columns_comments=comments),
)

wr.catalog.tables(database="jc-awswrangler_test")

df_athena = wr.athena.read_sql_query(
    sql="SELECT * FROM jcawswrtbl LIMIT 10",
    database="jc-awswrangler_test",
    ctas_approach=True
)
print(df_athena)

