# ---------- Import packages ----------
import os
import pandas as pd
from sqlalchemy import create_engine

# ---------- Get File Directory ---------- 
path      = os.getcwd()
file      = '/source/users_w_postal_code.csv'
file_path = path + file

# ---------- Open File Use Pandas & Use Engine SQL Alchemy ----------
df = pd.read_csv(file_path, sep = ',')
engine = create_engine('postgresql://postgres:admin@127.0.0.1:5432/postgres')
df.to_sql("from_file_table",engine)