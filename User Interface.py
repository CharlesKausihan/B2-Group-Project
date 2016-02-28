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
	root.title("Virtual Robot Bargain Hunt")
	
	root.mainloop()

if __name__ == '__main__':
	sys.exit(main())
