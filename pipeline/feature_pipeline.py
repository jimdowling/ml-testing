import hsfs
import pandas as pd
from features import ip_features as ipf


def connect(host: str, project : str) -> hsfs.Connection.connection:
    print("Connecting....")
    connection = hsfs.connection(
        host=host,
        project=project,
        engine="hive",
        secrets_store="local",
        api_key_file="./api-key.txt"
    )
    return connection


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    print("Creating features....")
    df['ip_str'] = df.ip.apply(ipf.ip_int_to_str)
    df['city'] = df.ip_str.apply(ipf.ip_str_to_city2)
    return df


def read_data(path: str) -> pd.DataFrame: 
    print("Reading raw data....")
    return pd.read_csv(path, dtype={'is_attributed': 'bool'}, parse_dates=['click_time'])


def run(host: str, project: str) : 
    # First, you have to create a project on Hopsworks called 'prod'
    connection = connect(host, project)
    fs = connection.get_feature_store()
    df = read_data("sample-click-logs.csv")
    df = engineer_features(df)

    print("Writing features to feature store....")
    fg_name="clicks2"
    try:
        fg = fs.get_feature_group(fg_name,version=1)
        fg.insert(df)
    except:
        print("Creating feature group...")
        fg = fs.create_feature_group(fg_name,
                        version=1,
                        description="User clicks on our website",
                        primary_key=['id'],
                        online_enabled=True)
        fg.save(df)
    connection.close()

run(host="791bb4a0-bb1c-11ec-8721-7bd8cdac0b54.cloud.hopsworks.ai",project="dev")
