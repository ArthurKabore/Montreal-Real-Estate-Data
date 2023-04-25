import snowflake.connector
import pandas as pd

# First and last commit for this file as I do not want to expose private info :)  

df = pd.read_csv('Outputs/snowflake_data.csv')

conn = snowflake.connector.connect(
    user='',
    password='',
    account='',
    warehouse='',
    database='',
    schema=''
)

cursor = conn.cursor()
cursor.execute("CREATE TEMPORARY STAGE my_stage")

cursor.execute(f"COPY INTO my_stage FROM (SELECT * FROM VALUES {','.join([str(tuple(row)) for row in df.values])}) FILE_FORMAT = (TYPE = CSV, SKIP_HEADER = 1)")
cursor.execute("COPY INTO my_table FROM @my_stage FILE_FORMAT = (TYPE = CSV, SKIP_HEADER = 1)")

cursor = conn.close()