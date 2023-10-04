# ---------- Import packages ----------
import os
import pandas as pd
from sqlalchemy import create_engine, text

# ---------- Get File Directory ---------- 
path      = os.getcwd()
file      = '/source/users_w_postal_code.csv'
file_path = path + file

# ---------- Open File Use Pandas & Use Engine SQL Alchemy ----------
df = pd.read_csv(file_path, sep = ',')

user        = 'postgres'
password    = 'admin'
hostname    = '127.0.0.1'
database    = 'postgres'

conn_string = f'postgresql://{user}:{password}@{hostname}:5432/{database}'
engine      = create_engine(conn_string)
conn        = engine.connect()

df.to_sql("from_file_table",engine, if_exists='replace')

# ---------- Check the Data ---------- 
query   = "SELECT * FROM from_file_table"
df_read = pd.read_sql(query,engine)
print(df_read)

# ---------- Close the Connection ---------- 
conn.close()
                   