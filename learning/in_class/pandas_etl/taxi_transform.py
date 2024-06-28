import datetime
import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df['Trip_Date'] = pd.to_datetime(df['tpep_pickup_datetime'].dt.date)
    df['Trip_Month'] = df['Trip_Date'].dt.month_name()
    df['Trip_Day'] = df['Trip_Date'].dt.day_name()
    df['Trip_Year'] = df['Trip_Date'].dt.year 
    df['Trip_Duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() // 60
    df['Total_Trip_Charge'] = df['fare_amount'] + df['extra'] + df['mta_tax'] + df['tolls_amount'] + df['improvement_surcharge'] + df['congestion_surcharge'] + df['Airport_fee'] + df['tip_amount']


    cols = ['VendorID', 'Trip_Date', 'Trip_Year', 'Trip_Month', 'Trip_Day',
       'passenger_count', 'trip_distance', 'store_and_fwd_flag',
       'payment_type', 'Trip_Duration',
       'Total_Trip_Charge' ]
    df = df[cols]

    df.rename(columns={
    'VendorID': 'Vendor_ID',
    'passenger_count': 'No_of_Passengers',
    'store_and_fwd_flag': 'SF_Flag',
    'payment_type': 'Payment_Type'
    }, inplace=True)

    return df


def stats(name: str, start: datetime.datetime, end: datetime.datetime, df: pd.DataFrame) -> dict:
    rows, cols = df.shape
    return {
        "name": name,
        "records": rows,
        "cols": cols,
        "num_na": df.isna().sum(),
        "start": start,
        "end": end
    }
