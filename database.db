import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
name TEXT,
title TEXT,
skills TEXT,
projects TEXT,
email TEXT
)
""")

conn.commit()
conn.close()

print("DB 생성 완료")
