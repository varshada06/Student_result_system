import sqlite3
import csv

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    rollno INTEGER,
    name TEXT,
    total INTEGER,
    percentage REAL,
    grade TEXT,
    status TEXT
)
""")

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = int(row['Maths']) + int(row['Science']) + int(row['English'])
        percentage = total / 3

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "Fail"

        status = "Pass" if grade != "Fail" else "Fail"

        cursor.execute(
            "INSERT INTO results VALUES (?, ?, ?, ?, ?, ?)",
            (row['RollNo'], row['Name'], total, percentage, grade, status)
        )

conn.commit()
conn.close()

print("✅ Data stored in database successfully")
