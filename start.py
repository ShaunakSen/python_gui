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










