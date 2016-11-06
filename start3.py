from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# Message Box

def open_message_box():
    messagebox.showwarning(
        "Event Triggered",
        "Button CLicked"
    )


root = Tk()

# Style the widgets

# Size on window and position on screen

# widthxheight + xoffset + yoffset

root.geometry("400x400+300+300")
root.resizable(width=False, height=False)

frame = Frame(root)

style = ttk.Style()

style.configure("TButton", foreground="midnight blue", font="Times 20 bold italic", padding=20)

print(ttk.Style().theme_names())

print(style.lookup("TButton", "font"))
print(style.lookup("TButton", "foreground"))
print(style.lookup("TButton", "padding"))


theButton = ttk.Button(frame, text="Important Button", command=open_message_box)

theButton['state'] = 'disabled'
theButton['state'] = 'normal'
theButton.pack()

frame.pack()

root.mainloop()
