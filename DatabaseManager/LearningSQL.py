__author__ = 'karinamarie'

import sqlite3

conn = sqlite3.connect("LearningDatabase.db")
cursor = conn.cursor()

#Create a table
cursor.execute('''CREATE TABLE animals
(name text, breed text, color text, gender text, weight text, squirrel_count text, date_entry text)''')

# table name = animals with 5 text fields
#sqlite only supports five data types null, integer, real, text, and blob

animal = [('Ducky' , 'Springer Spaniel' , 'Black and White' , 'Male' , '34.5' , '2','5/19/2015' ),
          ('Buster', 'Border Collie Mix', 'Black and White', 'Male', '57', '1', '5/12/2015'),
          ('Barney', 'Springer Spaniel', 'Liver and White', 'Male', '43', '1', '05/04/2015')]

cursor.executemany("INSERT INTO animals VALUES (?,?,?,?,?,?,?)", animal)
conn.commit()
for row in cursor:
    print row
