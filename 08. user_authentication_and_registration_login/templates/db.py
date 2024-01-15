import sqlite3
import os

foler_path = "08. user_authentication_and_registration_login"
if not os.path.exists(foler_path):
    os.makedirs(foler_path)
db_path = os.path.join(foler_path, "database.db")
conn = sqlite3.connect(db_path)
print("DB Opened")
conn.execute("""
CREATE TABLE `users`(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name VARCHAR,
             email TEXT,
             password TEXT,
             date DATETIME
)            
""")
print("Data Created Successfully")
conn.close()