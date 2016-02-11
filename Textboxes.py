from Tkinter import *

root = Tk()
label = Label(text='Min Price')
label.pack()
T = Text(root, height=2, width=10)
T.pack()
T.insert(END, unichr(163))

label = Label(text='Max Price')
label.pack()
T = Text(root, height=2, width=10)
T.pack()
T.insert(END, unichr(163))
mainloop()
