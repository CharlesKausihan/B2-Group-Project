#Make sure the database and this file are in the same directory when testing.3
import sqlite3 as sql

#You quotation marks for inputs when testing
colour_id = input("Colour of the car? :")
location_id = input("Location of the car?: ")
seat_id = int(input("How many seats in the car?: "))
door_id = int(input("How many doors in the car?: "))
minPrice = float(input("Min price of the car?: "))
maxPrice = float(input("Max price of the car?: "))


#Search algorithm for all criteria
db = sql.connect('Car_Database.sqlite')
cursor = db.cursor()

cursor.execute('''SELECT * FROM Cars WHERE Colour=? and Location=? and Seats=? and Doors=? and Price BETWEEN ? AND ?''', (colour_id, location_id, seat_id, door_id, minPrice, maxPrice,))
user = cursor.fetchall()
print(user)
db.close()
