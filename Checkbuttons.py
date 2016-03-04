from Tkinter import *

root = Tk()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()

noOfSeatsLabel = Label(root, text ="No Of seats:    "). grid(row = 1, column = 1, sticky = W)
noOfDoorsLabel = Label(root, text ="No Of seats:    "). grid(row = 2, column = 1, sticky = W)


noOfSeats2 = Checkbutton (root, text= "2", variable = var1).grid (row=1,column =2 , sticky = W)
noOfSeats5 = Checkbutton (root, text= "5", variable = var2).grid (row=1,column =3 , sticky = W)
noOfSeats7 = Checkbutton (root, text= "7", variable = var3).grid (row=1,column =4 , sticky = W)
noOfSeatsAny = Checkbutton (root, text= "Any", variable = var4).grid (row=1,column =5 , sticky = W)



noOfDoors3 = Checkbutton (root, text= "3", variable = var5).grid (row=2,column =2 , sticky = W)
noOfDoors5 = Checkbutton (root, text= "5", variable = var6).grid (row=2,column =3 , sticky = W)
noOfDoorsAny = Checkbutton (root, text= "Any", variable = var7).grid (row=2,column =4 , sticky = W)

# make sure this is put function is placed before it is called else the'll be an error
def UserInput():
    if var1.get():
        print(2)
    else:
        print("no")
    if var2.get():
        print(5)
    else:
        print("no")
    if var3.get():
        print(7)
    else:
        print("no")

    if var4.get():
        print("Any")
    else:
        print("no")
    if var5.get():
        print(3)
    else:
        print("no")
    if var6.get():
        print(5)
    else:
        print("no")
    if var5.get():
        print("Any")
    else:
        print("no")
    


button1 = Button(root, text = "submit", command = UserInput).grid(row = 4, column = 2,sticky = W)



root.mainloop()
