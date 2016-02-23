from Tkinter import *

root = Tk()

label_1 = Label(root, text='Minimum Price:').grid(row=0)
label_2 = Label(root, text='Maximum Price:').grid(row=1)
entry_1 = Entry(root)
entry_2 = Entry(root)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

entry_1.insert(END, unichr(163))
entry_2.insert(END, unichr(163))

root.mainloop()
