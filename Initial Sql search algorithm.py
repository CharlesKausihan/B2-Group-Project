import sqlite3 as sql

db = sql.connect('Car_Database.sqlite')
cursor = db.cursor()

make_id = 'BMW'

cursor.execute('''SELECT * FROM Cars WHERE Make=?''', (make_id,))
user = cursor.fetchall()
print(user)

db.close()
