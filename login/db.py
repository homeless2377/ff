import sqlite3

conn = sqlite3.connect("DB.sqlite3")
c = conn.cursor()

c.execute("""create table accounts (
    email text,
    password text,
    site text
)""")
