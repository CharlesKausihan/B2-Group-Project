from Tkinter import *

master = Tk()

label = Label(text='Colour')
label.pack(side=LEFT)

var = StringVar(master)
var.set("")

option = OptionMenu(master, var, "Any", "-","Black", "Blue", "Green", "Red", "Silver", "White")
option.pack(side=RIGHT)

def select():
    print "Value is", var.get()
    master.quit()


label = Label(text='Location')
label.pack(side=LEFT)

var = StringVar(master)
var.set("")

option = OptionMenu(master, var, "Any", "-","Birmingham", "Cardiff", "Dublin", "Glasgow", "London", "Manchester")
option.pack(side=RIGHT)

def select():
    print "Value is", var.get()
    master.quit()

def main():
	root = Tk()
	# set the starting size of the window
	root.geometry('%dx%d' % (100,100))
	gui = Gui(root)
	root.mainloop()

mainloop()
