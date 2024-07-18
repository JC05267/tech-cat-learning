import boto3
import json
import time
import pandas as pd
import configparser

# Read AWS credentials from config file
config = configparser.ConfigParser()
config.read('aws.cfg')

aws_access_key_id = config['AWS']['AccessKeyID']
aws_secret_access_key = config['AWS']['Secret']
region_name = config['AWS']['region_name']

# Initialize the boto3 client with credentials from config file
kinesis_client = boto3.client(
    'kinesis',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)


def produce(stream_name, data, partition_key):
    try:
        # Convert timestamps to strings
        for key in data:
            if isinstance(data[key], pd.Timestamp):
                data[key] = data[key].isoformat()
                # using the put_record method to push the stream
        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=partition_key
        )
        return response
    except Exception as e:
        print(f"Error producing record: {e}")

# this function takes 5 records at a time and streams every 2-seconds
def stream_data(df, stream_name):
    for i in range(0, len(df), 5):
        records = df.iloc[i:i+5].to_dict(orient='records')
        for record in records:
            partition_key = str(record['tpep_pickup_datetime'])  # Use a valid column as the partition key

            # call the produce function
            produce(stream_name, record, partition_key)
        print(f"Sent {len(records)} records to Kinesis")
        time.sleep(2)


if __name__ == "__main__":
    stream_name = 'jc-ds'
    # Reading the yellow_taxis parquet file and stream it
    df = pd.read_parquet('s3://techcatalyst-public/yellow_tripdata_2024-01.parquet',
                     storage_options={
                      'key': aws_access_key_id,
                     'secret': aws_secret_access_key,
                     })
    stream_data(df, stream_name)
