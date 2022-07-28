import sqlite3

connection = sqlite3.connect("addressbook.db")
print("Database opened successfully")
cursor = connection.cursor()
# delete
cursor.execute('''DROP TABLE Address;''')
connection.execute("CREATE TABLE Address (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE "
                   "NOT NULL, address TEXT NOT NULL)")
# connection.execute("CREATE TABLE Address (id INTEGER PRIMARY KEY AUTOINCREMENT,name varchar(255),email varchar(255),"
# "address varchar(255)")
print("Table created successfully")
connection.close()
