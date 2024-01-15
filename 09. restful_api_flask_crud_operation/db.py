import sqlite3
import os

folder = "09. restful_api_flask_crud_operation"
if not os.path.exists(folder):
    os.makedirs(folder)

db_path = os.path.join(folder, "database.db")
con = sqlite3.connect(db_path)
print("database created successfully")

con.execute("""
CREATE TABLE `movies` (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_name VARCHAR,
            actor VARCHAR,
            description TEXT,
            release_data DATETIME
)
""")
print("movie table created successfully")