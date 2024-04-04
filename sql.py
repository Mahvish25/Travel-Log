import sqlite3
# connection is used to connect to a  sqlite database
connection = sqlite3.connect('traveldb.db')

# cursor will be used to interact with our database through SQL commands
cur = connection.cursor()

sql = """
    CREATE TABLE TravTable (
                  Trip_ID INTEGER,
                  Destination TEXT,
                  Start_Date TEXT,	
                  End_Date TEXT,	
                  Duration(days) INTEGER,
                  Traveler_Name TEXT,
                  Traveler_Age INTEGER,
                  Traveler_Gender TEXT,
                  Traveler_Nationality TEXT,
                  Accommodation_Type TEXT,	
                  Accommodation_Cost INTEGER,	
                  Transportation_Type	TEXT,
                  Transportation_Cost INTEGER,
                  primary key(Trip_ID)
                  ) """

cur.execute(sql)
print("Database has been created")

# commit changes and close connection

connection.commit()
connection.close()
