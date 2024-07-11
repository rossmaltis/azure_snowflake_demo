from snowflake.snowpark.session import Session 
from snowflake.snowpark.session import Session 
from snowflake.snowpark import DataFrame 
from snowflake.snowpark.functions import col
import json

def hello(session: Session) -> DataFrame:
    df = session.table("DEV_ROSSM.MFR_SCHEMA.CUSTOMERS")
    #df = df.groupBy("STATE").count()
    return df

# For local debugging
if __name__ == "__main__":
    session = Session.builder.configs(json.load(
      open("/snowflake_connection.json"))).create()
    print (hello (session).show())
