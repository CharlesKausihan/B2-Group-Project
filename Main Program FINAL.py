#GUI
import Tkinter
from Tkinter import *
import tkMessageBox


class Labels:
   def __init__(self, root):
      self.root = root

      self.label=Label(root, text='Search Criteria                ',height=2).grid(row=1,column=1,sticky=W)
      self.label=Label(root, text='Location: ').grid(row=2,column=1,sticky=E)
      self.label=Label(root, text='Number of Seats: ').grid(row=3,column=1,sticky=E)
      self.label=Label(root, text='Number of Doors: ').grid(row=4,column=1,sticky=E)
      self.label=Label(root, text='Colour: ').grid(row=5,column=1,sticky=E)
      self.label=Label(root, text='Minimum Price: ').grid(row=6,column=1,sticky=E)
      self.label=Label(root, text='Maximum Price: ').grid(row=6,column=3,sticky=E)
      self.label=Label(root, text='Sort by: ', height=5).grid(row=16,column=2,sticky=E)
      self.label=Label(root, text='Results: ', height=5).grid(row=16,column=1,sticky=W)


class DropDownMenu:
   def __init__(self, root, loc, col, sort):
      self.root = root
      self.loc = loc
      self.col = col
      self.sort = sort
      #Location
      self.OptionMenu=OptionMenu(self.root, self.loc, "Any","", "Birmingham", "Cardiff", "Dublin", "Glasgow", "London", "Manchester").grid(row=2,column=2,sticky=W+E)
      #Colour
      self.OptionMenu=OptionMenu(self.root, self.col, "Any","", "Black", "Blue", "Green", "Red", "Silver", "White").grid(row=5,column=2,sticky=W+E)
      #Sorting
      self.OptionMenu=OptionMenu(self.root, self.sort, "Any","", "High to Low", "Low to High").grid(row=16,column=3,sticky=W+E)     


class Entrys:
   def __init__(self,root):
      self.root = root
      #Minimum
      self.entry = Entry(self.root)
      self.entry.grid(row=6,column=2)
      self.entry.insert(END, unichr(163))
      #Maximum
      self.entry = Entry(self.root)
      self.entry.grid(row=6,column=4)
      self.entry.insert(END, unichr(163))


class Checkbuttons:
   def __init__(self, root):
      self.root = root
      self.checkbutton = Checkbutton(self.root)
      #Number of Seats
      self.checkbutton = Checkbutton(text="2").grid(row=3,column=2,sticky=W)
      self.checkbutton = Checkbutton(text="5").grid(row=3,column=2,sticky=N)
      self.checkbutton = Checkbutton(text="7").grid(row=3,column=2,sticky=E)
      self.checkbutton = Checkbutton(text="Any").grid(row=3,column=3,sticky=E)
      #Number of Doors
      self.checkbutton = Checkbutton(text="3").grid(row=4,column=2,sticky=W)
      self.checkbutton = Checkbutton(text="5").grid(row=4,column=2,sticky=N)
      self.checkbutton = Checkbutton(text="Any").grid(row=4,column=3,sticky=E)     


class Buttons:
   def __init__(self, root, popup):
      self.root = root
      self.button = Button(self.root)
      self.popup = popup
      #Search Button
      self.button = Button(text="Search", height=5).grid(row=15,column=3,sticky=W+E)
      #More Info Button
      self.button = Button(text="Click for more information", command = self.info).grid(row=1,column=5,sticky=W+E)     

   def info(self):
      self.popup("Click for more information", "Please fill in the desied search criteria sections in order to conduct a search")

   
def main():
	root = Tk()
	label = Labels(root)
	loc = StringVar(root)
	col = StringVar(root)
	sort = StringVar(root)
	drop = DropDownMenu(root, loc, col, sort)
	entry = Entrys(root)
	checkbutton = Checkbuttons(root)
	popup = tkMessageBox.showinfo
	button = Buttons(root, popup)
	
	root.mainloop()

if __name__ == '__main__':
	sys.exit(main())

#Map Animation
from Tkinter import *
import time

class Gui:
    def __init__(self, root):
        self.root = root

        self.frame1 = Frame(self.root)
        self.frame1.pack()

        self.button = Button(self.frame1,text="Move",command=self.movement)
        self.button.pack(side=LEFT)
        

        self.frame2 = Frame(self.root)
        self.frame2.pack()
        
        self.canvas = Canvas(self.frame2,width = 500, height = 640, bg = 'red')
        self.canvas.pack()

        self.gif1 = PhotoImage(file = 'Map.gif')

        self.gif2 = PhotoImage(file = 'Stickman.gif')
    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.canvas.create_image(0, 0, image = self.gif1, anchor = NW)
        self.robot = self.canvas.create_image(10, 590, image = self.gif2, anchor = NW)
        self.location = str(input("Please Specify the location of the garage."))    
        
    def animation(self, destX, destY):
        """ Code to animate travel between the different locations."""
        canvas = self.canvas
        robotX, robotY = canvas.coords(self.robot)
        while robotX != destX or robotY != destY:
            if robotX < destX and robotY < destY:
                canvas.coords(self.robot, robotX+1, robotY+1)
            elif robotX > destX and robotY < destY:
                canvas.coords(self.robot, robotX-1, robotY+1)
            elif robotX < destX and robotY > destY:
                canvas.coords(self.robot, robotX+1, robotY-1)
            elif robotX > destX and robotY > destY:
                canvas.coords(self.robot, robotX-1, robotY-1)
            elif robotX < destX:
                canvas.coords(self.robot, robotX+1, robotY)
            elif robotY < destY:
                canvas.coords(self.robot, robotX, robotY+1)
            elif robotX > destX:
                canvas.coords(self.robot, robotX-1, robotY)
            elif robotY > destY:
                canvas.coords(self.robot, robotX, robotY-1)
            canvas.update()
            robotX, robotY = canvas.coords(self.robot)
            time.sleep(0.005)
            
    def movement(self):
        """ Function that moves the robot to the specified locations."""
        if self.location == "London" or self.location == "london" or self.location == "Birmingham" or self.location == "birmingham" or self.location == "Manchester" or self.location == "manchester" or self.location == "Cardiff" or self.location == "cardiff" or self.location == "glasgow" or self.location == "Glasgow" or self.location == "Dublin" or self.location == "dublin":
            canvas = self.canvas
            # Move to Birmingham
            if self.location == "Birmingham" or self.location == "birmingham":
                self.animation(360,410)

            # Move to Manchester    
            elif self.location == "Manchester" or self.location == "manchester":
                self.animation(325,350)

            # Move to Cardiff
            elif self.location == "Cardiff" or self.location == "cardiff":
                self.animation(275,450)

            # Move to Dublin
            elif self.location == "Dublin" or self.location == "dublin":
                self.animation(150,360)

            # Move to London
            elif self.location == "London" or self.location == "london":
                self.animation(380,475)
                
            # Move to Glasgow
            elif self.location == "Glasgow" or self.location == "glasgow":
                self.animation(260,220)
        else:
              print("Not A Valid Location")
            
if __name__ == '__main__':
    root = Tk()
    g = Gui(root)

    root.mainloop()

#Searching
import sqlite3 as sql

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


#list of results from searching
resultList1=user
#list for prices to be sorted
priceList1=[]
#final sorted list
Sorted_Results_List1=[]
  
#putting prices for individual car in seperate list
for n in resultList1:
    priceList1.append(n[6])

def swap(i, j):                    
    rList[i], rList[j] = rList[j], rList[i] 

def heaping(end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and rList[i] < rList[l]:   
        max = l   
    if r < end and rList[max] < rList[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heaping(end, max)   

def heapSort():     
    end = len(rList)   
    start = end // 2 - 1
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heaping(i, 0)

rList = priceList1
heapSort()
'''comparing resultList and priceList and adding results in asending order to
sorted_Results_List'''
for x in priceList1:
    for y in resultList1:
        if x!=y[6]:
            pass
        else:
            Sorted_Results_List1.append(y)

for n in Sorted_Results_List1:
    print(n)

#Sorting high to low
#list of result from searching
resultList=user
#list for prices to be sorted
priceList=[]
#final sorted list
Sorted_Results_List=[]

for n in resultList:
    priceList.append(n[6])

def insertion_sort( seq ):
    for i in range( 1, len( seq ) ):
        t = seq[i]
        k = i
        while k > 0 and t < seq[k - 1]:
            seq[k] = seq[k - 1]
            k -= 1
        seq[k] = t

seq = priceList
insertion_sort( seq )

for x in priceList:
    for y in resultList:
        if x!=y[6]:
            pass
        else:
            Sorted_Results_List.append(y)

Sorted_Results_List.reverse()

for n in Sorted_Results_List:
    print(n)

import sys

def main():

    #list of result from searching
    resultList=user
    #list for prices to be sorted
    priceList=[]
    #final sorted list
    Sorted_Results_List=[]

    for n in resultList:
        priceList.append(n[6])

    def insertionsort( aList ):
        for i in range( 1, len( aList ) ):
            tmp = aList[i]
            k = i
            while k > 0 and tmp < aList[k - 1]:
                aList[k] = aList[k - 1]
                k -= 1
            aList[k] = tmp

    aList = priceList
    insertionsort( aList )

    for x in priceList:
        for y in resultList:
            if x!=y[6]:
                pass
            else:
                Sorted_Results_List.append(y)

    Sorted_Results_List.reverse()
    print(Sorted_Results_List)


if __name__ == '__main__':
    sys.exit(main()) 

#Sorting low to high
import sys

def main():

    #list of results from searching
    resultList1=user
    #list for prices to be sorted
    priceList1=[]
    #final sorted list
    Sorted_Results_List1=[]
      
    #putting prices for individual car in seperate list
    for n in resultList:
        priceList1.append(n[6])
    
    def swap(i, j):                    
        sqc[i], sqc[j] = sqc[j], sqc[i] 

    def heapify(end,i):   
        l=2 * i + 1  
        r=2 * (i + 1)   
        max=i   
        if l < end and sqc[i] < sqc[l]:   
            max = l   
        if r < end and sqc[max] < sqc[r]:   
            max = r   
        if max != i:   
            swap(i, max)   
            heapify(end, max)   

    def heap_sort():     
        end = len(sqc)   
        start = end // 2 - 1
        for i in range(start, -1, -1):   
            heapify(end, i)   
        for i in range(end-1, 0, -1):   
            swap(i, 0)   
            heapify(i, 0)

    sqc = priceList1
    heap_sort()
    '''comparing resultList and priceList and adding results in asending order to
    sorted_Results_List'''
    for x in priceList1:
        for y in resultList1:
            if x!=y[6]:
                pass
            else:
                Sorted_Results_List1.append(y)

    print(Sorted_Results_List1)                



if __name__ == '__main__':
    sys.exit(main())  


