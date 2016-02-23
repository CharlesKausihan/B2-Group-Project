from Tkinter import *

root = Tk()

Label(root, text='Number of Seats: ').grid(row=0,column=0,sticky=E)

c = Checkbutton(root, text="2  ")
c.grid(row=0,column=1)
c = Checkbutton(root, text="5  ")
c.grid(row=0,column=2)
c = Checkbutton(root, text="7  ")
c.grid(row=0,column=3)
c = Checkbutton(root, text="Any  ")
c.grid(row=0,column=4)

Label(root, text='Number of Doors: ').grid(row=1,column=0,sticky=E)

c = Checkbutton(root, text="3  ")
c.grid(row=1,column=1)
c = Checkbutton(root, text="5  ")
c.grid(row=1,column=2)
c = Checkbutton(root, text="Any  ")
c.grid(row=1,column=3)

root.mainloop()
