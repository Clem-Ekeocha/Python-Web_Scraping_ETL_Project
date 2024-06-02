

import sqlite3


# Create a connection instance
connection = sqlite3.connect("data.db")

# Create a cursor for executing sql queries
cursor = connection.cursor()

# Query the data using the SQL script
cursor.execute("SELECT * FROM events WHERE date = '2088.10.15'")

# Extract data from sql code
rows = cursor.fetchall()

# Print out the data
print(rows)

# How to insert new rows
# You must create a tiple in order to inseet data in the the db
new_rows = [('Cats', 'Cat City', '2088.10.17'),
            ('Hens', 'Hen City', '2088.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

#Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)


