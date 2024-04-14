import sqlite3

connection = sqlite3.connect('tripdata.db')
cursor = connection.cursor()

with open('Trip.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT OR REPLACE INTO Travel VALUES(?,?,?,?,?)", row.split(","))
        connection.commit()
        no_records += 1
connection.close()
print(" \n{} Records Transferred".format(no_records))
