from tkinter import *

from tkinter import ttk

# root will be the main window

root = Tk()

# Give window a title
root.title("First Mini App :)")

# ttk.Button(root, text="Hii Mini").grid()

# ---------- MULTIPLE COMPONENTS  ----------
# Some of the different Widgets : Button, Label,
# Canvas, Menu, Text, Scale, OptionMenu, Frame,
# CheckButton, LabelFrame, MenuButton, PanedWindow,
# Entry, ListBox, Message, RadioButton, ScrollBar,
# Bitmap, SpinBox, Image

# Use a frame
# Frame is a widget that surrounds other widgets


frame = Frame(root)

labelText = StringVar()
label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click Me!!")
labelText.set("I am a label")

label.pack()
button.pack()
frame.pack()

root.mainloop()

# Pack

# pack position widgets by defining positions as: top, bottom, right and left

# they also let them define their fill direction i.e how they will be stretched: X, Y, Both or None

root = Tk()

frame = Frame(root)

Label(frame, text="A bunch of buttons!").pack()

Button(frame, text="B1").pack(side=LEFT, fill=Y)
Button(frame, text="B2").pack(side=TOP, fill=X)
Button(frame, text="B3").pack(side=RIGHT, fill=X)
Button(frame, text="B4").pack(side=LEFT, fill=X)

frame.pack()

root.mainloop()

# Grid Geometry manager
# Lines up widgets using rows and cols

root = Tk()
# N, NE, NW, W, E, etc : directions where the widget will extend
# padx: padding around the widget on left and right
# pady: padding around the widget on top and bottom

Label(root, text="First Name").grid(row=0, sticky=W, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)


Label(root, text="Last Name").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1, column=1, sticky=E, pady=4)

Button(root, text="Submit").grid(row=3)
root.mainloop()

# Creating a more complex UI

root = Tk()

Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="Submit").grid(row=0, column=8)


Label(root, text="Quality").grid(row=1, column=0, sticky=W)
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)

Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)
Checkbutton(root, text="Warranty").grid(row=4, column=1, sticky=W)

root.mainloop()


# Events

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sumValue = num1 + num2
    sumEntry.delete(0, "end")
    sumEntry.insert(0, sumValue)


root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
# Button-1: signifies left most mouse button
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()




