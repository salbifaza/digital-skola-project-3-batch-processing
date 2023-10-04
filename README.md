# digital-skola-project-3-batch-processing


Command
```
pip install --no-cache-dir -r requirements.txt
```

Command to Execute Inside Postgres Container
```
docker exec -it ds-postgresql psql -U postgres
```

If current transaction is aborted
```
cur.execute("ROLLBACK")
conn.commit()
```