# ---------- Import packages ----------
import os
import psycopg2


# ---------- Connect to postgresql ----------
conn = psycopg2.connect("host = localhost dbname = postgres user = postgres password= admin")
cur = conn.cursor()

# ---------- Create Table ---------- 
cur.execute("""
            CREATE TABLE IF NOT EXISTS tbl_user_copy(
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

# ---------- Open File Use Copy From  ---------- 
with open(file_path,'r') as f:
    next(f)
    cur.copy_from(f, 'tbl_user_copy', sep=',', columns=('email','name','phone','postal_code'))
conn.commit()

# ---------- Check the Data ---------- 
cur.execute("""
            SELECT * FROM tbl_user_copy
        """
)
cur.fetchall()