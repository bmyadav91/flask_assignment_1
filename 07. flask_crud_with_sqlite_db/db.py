import sqlite3
import os

folder = "07. flask_crud_with_sqlite_db"
if not os.path.exists(folder):
    os.makedirs(folder)
db_path = os.path.join(folder, "database.db")
conn = sqlite3.connect(db_path)
print("opened database")
conn.execute("""
             CREATE TABLE `users`(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             email TEXT,
             address TEXT
             )
             """)
print("Table Created Success")
conn.close()