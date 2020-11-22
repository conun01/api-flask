import sqlite3

con_db = sqlite3.connect("data.db")
cursor = con_db.cursor()

query_table = "SELECT * FROM users,items"
abc = cursor.execute(query_table).fetchall()

print(abc)