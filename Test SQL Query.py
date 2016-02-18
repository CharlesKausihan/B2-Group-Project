import sqlite3 as sql
con = sql.connect('Car_Database.sqlite')
cur = con.cursor()
cur.execute('''SELECT * FROM Cars;''')
for row in cur:
    print(row)  
con.close()

