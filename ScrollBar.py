from Tkinter import *

root = Tk()
#fame created to group listbox and scroll widgets
frame1 = Frame(root)
frame1.pack(side = BOTTOM)

label = Label(root, text = "***\\\TEXT///***")
label.pack(side = LEFT)


scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill= Y)

listbox = Listbox(frame1, yscrollcommand=scrollbar.set)

#can be deleted. used to show the scroll function 
for i in range(1000):
    listbox.insert(END, str(i))


listbox.pack(side=LEFT, fill= BOTH)
scrollbar.config(command=listbox.yview)

mainloop()
