import sqlite3, csv

connection = sqlite3.connect('traveldb.db')
cursor = connection.cursor()

with open('Travel_data1.csv','r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO TravTable VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(','))
        connection.commit()
        no_records += 1

connection.close()
print(" \n{} Records Transferred".format(no_records))


