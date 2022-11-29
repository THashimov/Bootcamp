import sqlite3

# Create a database
db = sqlite3.connect("python_db")

cursor = db.cursor()

# Create a table if the table does not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS python_programming ("id" INT PRIMARY KEY, "name" VARCHAR(15), "grade" INT)''')

db.commit()

ids = [55, 66, 77, 12, 2]
names = ["Carl Davis", "Dennis Fredrickson", "Jane Richards", "Peyton Sawyer", "Lucas Brooke"]
grades = [61, 88, 78, 45, 99]

# Insert all the rows into the table
for i in range(len(ids)) :
    cursor.execute('''INSERT OR IGNORE INTO python_programming
    VALUES(?, ?, ?)''', (ids[i], names[i], grades[i]))

    db.commit()
    print("User added")

# Get all the users with a grade between 60 and 80
cursor.execute('''SELECT * FROM python_programming WHERE grade >=60 AND grade <= 80''')
user = cursor.fetchall()
print(f"Id: {user[0][0]}, Name: {user[0][1]}, Grade: {user[0][2]}\nId: {user[1][0]}, Name: {user[1][1]}, Grade: {user[1][2]}")

# Change Carl Davis's grade to 65
cursor.execute('''UPDATE python_programming
                    SET grade = "65"
                    WHERE name = "Carl Davis" ''')

db.commit()

# Delete Dennis Fredrickson's row
cursor.execute('''DELETE  from python_programming
                    WHERE name = "Dennis Fredrickson" ''')

db.commit()

# Change the grade of every user who has an id of less than 55
cursor.execute('''UPDATE python_programming
                    SET grade = "100"
                    WHERE id < 55 ''')

db.commit()