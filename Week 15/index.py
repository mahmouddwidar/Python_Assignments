# -------------------------------
# -------------117-127-----------
# -------------------------------



# -------------------------------
# ---------Assignment-1----------
# -------------------------------


# import SQLite module 
import sqlite3

# connect database
db = sqlite3.connect("Database Data Types.db")

# setting up the cursor
cr = db.cursor()

# create tables and fields
cr.execute("create table if not exists Data (id INT, name TEXT, age TINYINT, dob DATE, rank FLOAT)")

# insert data into database
cr.execute("insert into Data (id, name, age, dob, rank) values (1, 'Ali', 22, '6/2/2000', 96.5)")
cr.execute("insert into Data (id, name, age, dob, rank) values (2, 'Ola', 20, '30/7/2002', 92.5)")

# commit changes
db.commit()

# close database
db.close()



# -------------------------------
# -------Assignment-2,3,4,5------
# -------------------------------

import sqlite3

# connect database
db = sqlite3.connect(r"D:\Python\Videos ElZero\15\Assignments\elzero.db")

# setting up the cursor
cr = db.cursor()

# create tables and fields
cr.execute("create table if not exists users (id INT unique, name TEXT unique, dob DATE unique, email TEXT unique)")

# inserting data into database
try:
    cr.execute("insert into users (id, name, dob, email) values (1, 'Ahmed', '3/2/2000', 'a@elzero.org')")
    cr.execute("insert into users (id, name, dob, email) values (2, 'Ali', '12/2/2000', 'l@elzero.org')")
    cr.execute("insert into users (id, name, dob, email) values (3, 'Mona', '20/2/2000', 'm@elzero.org')")
    cr.execute("insert into users (id, name, dob, email) values (4, 'Gamal', '7/2/2000', 'g@elzero.org')")
    cr.execute("insert into users (id, name, dob, email) values (5, 'Ola', '26/2/2000', 'o@elzero.org')")

except:
    pass


# fetch data of last row
cr.execute("select * from users where id = 5")
fifth_result = cr.fetchall()
print(fifth_result)


# user input
user_id = input("Enter your Id ")

cr.execute(f"select id from users where id = '{user_id}'")
id_results = cr.fetchone()

if id_results != None:
    cr.execute(f"delete from users where id = '{user_id}'")
    print(f"User '{user_id}' Deleted.")
    print("Show Other Data:")
    cr.execute("select * from users")
    all_results = cr.fetchall()
    for row in all_results:
        print(f"ID => {row[0]}, Name => {row[1]}, Date Of Birth => {row[2]}, Email => {row[3]}")

else:
    print("User Not Found.")


# commit changes
db.commit()

# close database
db.close()