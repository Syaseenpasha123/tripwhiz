import sqlite3
conn = sqlite3.connect("base1.db")
print("opened database successfully")
conn.execute("CREATE TABLE register1(username varchar,email varchar,password varchar,phone number)")
conn.execute("CREATE TABLE book(yourname varchar,youremail varchar,date date,message varchar)")
conn.execute("CREATE TABLE feedback(feedname varchar,feedemail varchar,subject varchar,feedmessage varchar)")
print("table created successfully")
conn.close()
