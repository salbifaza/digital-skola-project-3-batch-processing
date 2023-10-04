# ---------- Import packages ----------
import os
import csv
import psycopg2

# ---------- Connect to postgresql ----------
conn = psycopg2.connect("host = localhost dbname = postgres user = postgres password= admin")
cur = conn.cursor()

# ---------- Create Table ---------- 
cur.execute("""
            CREATE TABLE IF NOT EXISTS tbl_user(
              id serial PRIMARY KEY
            , email text
            , name text
            , phone text
            , postal_code text
            )
        """
)

# ---------- Get File Directory ---------- 
path      = os.getcwd()
file      = '/source/users_w_postal_code.csv'
file_path = path + file

# ---------- Open File ---------- 
with open(file_path,'r') as f:
    csv_reader = csv.reader(f, delimiter = ',')
    next(csv_reader)
    for row in csv_reader:
      cur.execute(
         "INSERT INTO tbl_user VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
         row
      )
conn.commit()