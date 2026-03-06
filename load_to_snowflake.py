import snowflake.connector
import pandas as pd
from config import (
    SNOWFLAKE_USER,
    SNOWFLAKE_PASSWORD,
    SNOWFLAKE_ACCOUNT,
    SNOWFLAKE_WAREHOUSE,
    SNOWFLAKE_DATABASE,
    SNOWFLAKE_SCHEMA,
    SNOWFLAKE_TABLE
)

def load_data_to_snowflake():
    df = pd.read_csv("data/clean_weather.csv")

    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {SNOWFLAKE_TABLE}
            (city, country, temperature, feels_like, humidity, pressure, wind_speed, cloudiness, weather)
            VALUES (
                '{row.city}',
                '{row.country}',
                {row.temperature},
                {row.feels_like},
                {row.humidity},
                {row.pressure},
                {row.wind_speed},
                {row.cloudiness},
                '{row.weather}'
            )
        """)

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Data loaded into Snowflake successfully")


if __name__ == "__main__":
    load_data_to_snowflake()