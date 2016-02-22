import Tkinter
from Tkinter import *
import tkMessageBox

root = Tkinter.Tk(  )

Tkinter.Label(root, text='Search Criteria').grid(row=1,column=1,sticky=W)

Tkinter.Label(root, text='Colour').grid(row=2,column=1,sticky=W)

var = StringVar(root)
var.set("")
Tkinter.OptionMenu(root, var, "Any", "-","Black", "Blue", "Green", "Red", "Silver", "White").grid(row=2,column=2,sticky=W+E)


Label(root, text='Number of Seats: ').grid(row=3,column=1,sticky=W)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
Checkbutton(root, text = "2", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 5).grid(row=3,column=3)
Checkbutton(root, text = "5", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 5).grid(row=3,column=4)
Checkbutton(root, text = "7", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 5).grid(row=3,column=5)
Checkbutton(root, text = "Any", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 5).grid(row=3,column=6)


Label(root, text='Number of Doors: ').grid(row=4,column=1,sticky=W)

CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()

Checkbutton(root, text = "3", variable = CheckVar5, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 5).grid(row=4,column=3)
Checkbutton(root, text = "5", variable = CheckVar6, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 5).grid(row=4,column=4)
Checkbutton(root, text = "Any", variable = CheckVar7, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 5).grid(row=4,column=5)

Tkinter.Label(root, text='Location').grid(row=5,column=1,sticky=W)

var = StringVar(root)
var.set("")
Tkinter.OptionMenu(root, var, "Any", "-","Birmingham", "Cardiff", "Dublin", "Glasgow", "London", "Manchester").grid(row=5,column=2,sticky=W+E)

Tkinter.Label(root, text='Min Price').grid(row=6,column=1,sticky=W)
T = Text(root, height=2, width=10)
T.grid(row=6,column=2,sticky=W)
T.insert(END, unichr(163))

Tkinter.Label(root, text='Max Price').grid(row=6,column=4,sticky=W)
T = Text(root, height=2, width=10)
T.grid(row=6,column=5,sticky=W)
T.insert(END, unichr(163))

root.mainloop()
