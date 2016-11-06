from tkinter import *
from tkinter import messagebox


# Functions

def get_data(event=None):
    print("String:", strVar.get())
    print("Integer:", intVar.get())
    print("Double:", dblVar.get())
    print("Boolean:", boolVar.get())


def bind_button(event=None):
    if boolVar.get():
        print(boolVar.get())
        getDataButton.unbind("<Button-1>")
    else:
        print(boolVar.get())
        getDataButton.bind("<Button-1>", get_data)

root = Tk()

# Types of variables

strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

# Set default values which will show up in the interface

strVar.set("Enter string...")
intVar.set("Enter integer...")
dblVar.set("Enter double...")
boolVar.set(True)

# textVariable implies the variable these entries are tied to

strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)

theCheckButton = Checkbutton(root, text="Switch", variable=boolVar)
theCheckButton.bind("<Button-1>", bind_button)
theCheckButton.pack(side=LEFT)

getDataButton = Button(root, text="Get Data")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)

root.mainloop()
