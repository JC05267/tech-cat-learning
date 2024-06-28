import datetime
import configparser
from boto3 import client
import pandas as pd
from taxi_transform import transform, stats

config = configparser.ConfigParser()
config.read("aws.cfg")

AWS_ACCESS_KEY = config["AWS"]["ACCESS_KEY"]
AWS_SECRET_KEY = config["AWS"]["SECRET_KEY"]

s3 = client("s3", aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY)

bucket_dest = 'techcatalyst-transformed'
bucket_source = 'techcatalyst-raw'


def s3_url(bucket: str, obj_name: str) -> str:
    """create s3 url"""
    return f"s3://{bucket}/{obj_name}"


def main():
    resp = s3.list_objects_v2(Bucket=bucket_source)
    objs = resp.get("Contents")
    stat_list = []
    for obj in objs:
        start = datetime.datetime.now()
        obj_name = obj['Key']
        print(f"processing {obj_name}")
        s3_read_loc = s3_url(bucket_source, obj_name)
        df = pd.read_parquet(s3_read_loc, storage_options={
            'key': AWS_ACCESS_KEY,
            'secret': AWS_SECRET_KEY
        })
        new = transform(df)

        s3_write_loc = s3_url(bucket_dest, f"jc/jc-{obj_name}")
        new.to_parquet(s3_write_loc, partition_cols=['Trip_Year', 'Trip_Month'], storage_options={
            'key': AWS_ACCESS_KEY,
            'secret': AWS_SECRET_KEY
        })
        print(f"writing {obj_name}")
        end = datetime.datetime.now()
        stat = stats(obj_name, start, end, df)
        stat_list.append(stat)

    summary = pd.DataFrame(stat_list)
    print(summary.head(len(objs)))


if __name__ == '__main__':
    main()
