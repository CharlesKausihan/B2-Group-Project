# This SQL Query searches for cars within a specified price range
import sqlite3 as sql
minPrice = float(input("Minimum Price of Car"))
maxPrice = float(input("Maximum Price of Car"))
if minPrice < maxPrice:
    con = sql.connect('Car_Database.sqlite')
    cur = con.cursor()
    cur.execute('''SELECT * FROM Cars WHERE Price BETWEEN ? AND ?;''', (minPrice, maxPrice))
    for row in cur:
        print(row)  
    con.close()
else:
    raise ValueError ("Minium price must be less than maximum price.")
print ()

# Queries for searching different car colours
# Silver
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Colour = 'Silver';''')
for row in cur:
    print(row)  
con.close()
print ()

# Green
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Colour = 'Green';''')
for row in cur:
    print(row)  
con.close()
print ()

# Red
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Colour = 'Red';''')
for row in cur:
    print(row)  
con.close()
print ()

# Black
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Colour = 'Black';''')
for row in cur:
    print(row)  
con.close()
print ()

# Blue
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Colour = 'Blue';''')
for row in cur:
    print(row)  
con.close()
print ()

# White
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Colour = 'White';''')
for row in cur:
    print(row)  
con.close()
print ()

# Yellow
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Colour = 'Yellow';''')
for row in cur:
    print(row)  
con.close()
print ()

# SQL queries to search for location of the cars.

# Birmingham
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Location = 'Birmingham';''')
for row in cur:
    print(row)  
con.close()
print()

# London
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Location = 'London';''')
for row in cur:
    print(row)  
con.close()
print()

# Cardiff
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Location = 'Cardiff';''')
for row in cur:
    print(row)  
con.close()
print()

# Manchester
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Location = 'Manchester';''')
for row in cur:
    print(row)  
con.close()
print()

# Glasgow
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Location = 'Glasgow';''')
for row in cur:
    print(row)  
con.close()
print()

# Dublin
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Location = 'Dublin';''')
for row in cur:
    print(row)  
con.close()
print()

# SQL Query to search number of Doors
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Doors = 5;''')
for row in cur:
    print(row)  
con.close()
print()

import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Doors = 3;''')
for row in cur:
    print(row)  
con.close()
print()

# SQL Query to search for number of Seats.
import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Seats = 2;''')
for row in cur:
    print(row)  
con.close()
print()

import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Seats = 5;''')
for row in cur:
    print(row)  
con.close()
print()

import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars WHERE Seats = 7;''')
for row in cur:
    print(row)  
con.close()
print()

