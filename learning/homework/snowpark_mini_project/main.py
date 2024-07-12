from snowflake.snowpark import Session
import pandas as pd
import configparser


def connect_to_snowflake() -> Session:
    config = configparser.ConfigParser()
    config.read('snow.cfg')
    
    params = dict(config['SNOW'])
    s = Session.builder.configs(params).create()
    
    print(s.get_current_user())
    print(s.get_current_database())
    print(s.get_current_schema())
    return s 


def write_pandas_to_snowflake(df: pd.DataFrame, loc: str, sess: Session):
    sdf = sess.create_dataframe(df)
    
    target = f"techcatalyst_de.js.snowpark_{loc}"
    print(f"writing: {target}")
    sdf.write.mode("overwrite").save_as_table(target)


def transform_fact_accidents(df: pd.DataFrame) -> pd.DataFrame:
    cols = {
        "body_style_code".capitalize(): "body_style_id",
        "accident_type".capitalize(): "accident_type_id",
        "gender_maritial_status".capitalize(): "gender_martialstatus_id",
        "use_code".capitalize(): "vehicle_usecode_id",
        "year".capitalize(): "vehicle_year",
        "birthdate".capitalize(): "policyholder_birthdate",
        "dui".capitalize(): "is_dui"
    }
    df = df.rename(columns=cols)
    return df


def transform_accident_type(df: pd.DataFrame) -> pd.DataFrame:
    cols = {
        "accident_type_code".capitalize(): "accident_type_id"
    }
    df = df.rename(columns=cols)
    return df


def transform_body_style(df: pd.DataFrame) -> pd.DataFrame:
    cols = {
        "body_style_code".capitalize(): "body_style_id"
    }
    df = df.rename(columns=cols)
    return df


def transform_policyholder(df: pd.DataFrame) -> pd.DataFrame:
    return df


def transform_dim_states(df: pd.DataFrame) -> pd.DataFrame:
    cols = {
        "state_code".capitalize(): "state_id"
    }
    df = df.rename(columns=cols)
    return df


def transform_vehicle_use(df: pd.DataFrame) -> pd.DataFrame:
    cols = {
        "c1".capitalize(): "vehicle_usecode_id",
        "c2".capitalize(): "vehicle_use"
    }
    df = df.rename(columns=cols)
    # drop that stupid row
    df.drop(0)
    return df


if __name__ == '__main__':
    session = connect_to_snowflake()
    accidents = session.table("ins_accidents")
    policyholder = session.table("ins_policyholder")
    coverage = session.table("ins_insurance_coverage")
    vehicles = session.table("ins_vehicles")
    vehicle_use = session.table("ins_vehicle_use")
    accident_type = session.table("ins_accident_type")
    body_style = session.table("ins_body_style")
    states = session.table("ins_states")
    
    accidents_df = accidents.to_pandas()
    policyholder_df = policyholder.to_pandas()
    coverage_df = coverage.to_pandas()
    vehicles_df = vehicles.to_pandas()
    vehicle_use_df = vehicle_use.to_pandas()
    body_style_df = body_style.to_pandas()
    accident_type_df = accident_type.to_pandas()
    states_df = states.to_pandas()
   
    fact_accidents = pd.merge(accidents_df, policyholder_df, how='inner', on="POLICYHOLDER_ID")
    fact_accidents = pd.merge(fact_accidents, coverage_df, how='inner', on=["POLICYHOLDER_ID"])
    fact_accidents = pd.merge(fact_accidents, vehicles_df, how='inner', on=["VEHICLE_ID"])
    fact_accidents = pd.merge(fact_accidents, vehicle_use_df, how='inner', on=["VEHICLE_ID"])

    fact_accidents_renamed = transform_fact_accidents(fact_accidents)
    dim_accident_type = transform_accident_type(accident_type_df)
    dim_body_style = transform_body_style(body_style_df)
    dim_policyholder = transform_policyholder(policyholder_df)
    dim_states = transform_dim_states(states_df)
    dim_vehicle_use = transform_vehicle_use(vehicle_use_df)
    
    write_pandas_to_snowflake(fact_accidents, "fact_accidents", session)
    write_pandas_to_snowflake(dim_accident_type, "dim_accident_type", session)
    write_pandas_to_snowflake(dim_body_style, "dim_body_style", session)
    write_pandas_to_snowflake(dim_policyholder, "dim_policyholder", session)
    write_pandas_to_snowflake(dim_states, "dim_states", session)
    write_pandas_to_snowflake(dim_vehicle_use, "dim_vehicle_use", session)


