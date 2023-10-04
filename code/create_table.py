# ---------- Import packages ----------
import os
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

path = os.getcwd()