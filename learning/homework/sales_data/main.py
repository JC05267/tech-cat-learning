import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read("aws.cfg")

ACCESS = config['AWS']['ACCESS_KEY']
SECRET = config['AWS']['SECRET_KEY']

def read() -> pd.DataFrame:
    df = pd.read_csv('s3://techcatalyst-raw/SalesRaw/sales_data.csv', storage_options={
        'key': ACCESS,
        'secret': SECRET
    })
    return df


def write(df: pd.DataFrame) -> pd.DataFrame:
    df.to_parquet('s3://techcatalyst-transformed/SalesTransformed/jc/sales_data.csv', storage_options={
        'key': ACCESS,
        'secret': SECRET
    }, partition_cols=['Country']
    )
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    threshold = 37000
    df.loc[df['Sales Amount'] == "?", 'Sales Amount'] = pd.NA
    df.loc[df['Sales Amount'] == "None", 'Sales Amount'] = pd.NA
    df['Sales Amount'] = pd.to_numeric(df['Sales Amount'])
    df.loc[df['Sales Amount'] > threshold, 'Sales Amount'] = pd.NA
    
    average = df['Sales Amount'].mean()
    df.loc[df['Sales Amount'] == pd.NA, 'Sales Amount'] = average 
    df['Sales Amount'] = df['Sales Amount'].round(2)
    df.drop([9723, 9373], inplace=True)

    df['DateTime'] = pd.to_datetime(df['DateTime']) 
    df['DateTime_Localized'] = df.apply(lambda row: row['DateTime'].tz_localize(row['Time Zone']), axis=1)
    df['DateTime_UTC'] = df['DateTime_Localized'].apply(lambda row: row.tz_convert('UTC'))
    return df

def analysis(df: pd.DataFrame):
    SalesByCountry = df.groupby('Country')['Sales Amount'].sum()
    print(SalesByCountry)
    SalesBySP = df.groupby('Sales Person')['Sales Amount'].sum()
    print(SalesBySP)

def main():
    df = read()
    df_t = transform(df)
    analysis(df_t)
    write(df_t)


if __name__ == '__main__':
    main()
