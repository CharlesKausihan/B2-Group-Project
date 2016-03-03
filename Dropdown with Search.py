from Tkinter import *
import sqlite3 as sql

master = Tk()

col = StringVar(master)
col.set("Colour")

option = OptionMenu(master, col,"Any","", "Black", "Blue", "Green", "Red", "Silver", "White")
option.pack()


loc = StringVar(master)
loc.set("Location")

option = OptionMenu(master, loc,"Any","", "Birmingham", "Cardiff", "Dublin", "Glasgow", "London", "Manchester")
option.pack()


seat = StringVar(master)
seat.set("Seats")

option = OptionMenu(master, seat,"Any","", "2", "5", "7")
option.pack()


door = StringVar(master)
door.set("Doors")

option = OptionMenu(master, door,"Any","", "3", "5")
option.pack()


minp = StringVar(master)
minp.set("Min")

option = OptionMenu(master, minp,"Any","", "1000")
option.pack()


maxp = StringVar(master)
maxp.set("Max")

option = OptionMenu(master, maxp,"Any","", "30000")
option.pack()


def search():
    colour_id = col.get()
    location_id = loc.get()
    seat_id = seat.get()
    door_id = door.get()
    minPrice = minp.get()
    maxPrice = maxp.get()
    master.quit()
    print(colour_id, location_id, seat_id, door_id, minPrice, maxPrice)

    #Search algorithm for all criteria
    db = sql.connect('Car_Database.sqlite')
    cursor = db.cursor()

    cursor.execute('''SELECT * FROM Cars WHERE Colour=? and Location=? and Seats=? and Doors=? and Price BETWEEN ? AND ?''', (colour_id, location_id, seat_id, door_id, minPrice, maxPrice,))
    user = cursor.fetchall()
    print(user)
    db.close()
    
button = Button(master, text="Search", command=search)
button.pack()


mainloop()

#list of result from searching
resultList=user
#list for make names to be sorted
nameList=[]
#final sorted list
Sorted_Name_List=[]

for n in resultList:
    nameList.append(n[0])



def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))

unsort_list = nameList
sort_list   = quicksort(unsort_list)

for x in nameList:
        for y in resultList:
            if x!=y[0]:
                pass
            else:
                Sorted_Name_List.append(y)

print(sort_list)
