import sqlite3 as sql

def colourSearch(c):
    db = sql.connect('Car_Database.sqlite')
    cursor = db.cursor()

    colour_id = c
    cursor.execute('''SELECT * FROM Cars WHERE Colour=?''', (colour_id,))
    user = cursor.fetchall()
    print(user)
    db.close()

def locationSearch(l):
    db = sql.connect('Car_Database.sqlite')
    cursor = db.cursor()

    location_id = l
    cursor.execute('''SELECT * FROM Cars WHERE Location=?''', (location_id,))
    user1 = cursor.fetchall()
    print(user1)
    db.close()

def seatSearch(s):
    db = sql.connect('Car_Database.sqlite')
    cursor = db.cursor()

    seat_id = s
    cursor.execute('''SELECT * FROM Cars WHERE "No. of Seats"=?''', (seat_id,))
    user2 = cursor.fetchall()
    print(user2)
    db.close()

def doorSearch(d):
    db = sql.connect('Car_Database.sqlite')
    cursor = db.cursor()

    door_id = d
    cursor.execute('''SELECT * FROM Cars WHERE "No. of Doors"=?''', (door_id,))
    user3 = cursor.fetchall()
    print(user3)
    db.close()


#Min Price not working yet

def minPriceSearch(mn):
    db = sql.connect('Car_Database.sqlite')
    cursor = db.cursor()

    minPrice_id = mn
    cursor.execute('''SELECT * FROM Cars WHERE LEN(Price) >= int(minPrice_id)''', (minPrice_id,))
    user4 = cursor.fetchall()
    print(user4)
    db.close()
