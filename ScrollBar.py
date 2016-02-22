from Tkinter import *


root = Tk()



scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)


mylist = Listbox(root, yscrollcommand = scrollbar.set )


#Prints string to the box within the List
for line in range(25):
   mylist.insert(END, "This is line number " + str(line))



mylist.pack(side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )



mainloop()
