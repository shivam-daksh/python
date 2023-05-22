from tkinter import *
from tkinter import ttk
def display_options():
    if var1.get():
        print("Option   1 selected.")
    if var2.get():
        print("Ooption 2 selected.")
root = Tk()
root.title("Check Button Demo")
root.geometry("800x600")
var1 = IntVar()
var2 = IntVar()
chckbutton1 = Checkbutton(root, text="Option 1", variable=var1)
chckbutton1.pack()
chckbutton2 = Checkbutton(root, text="Option 2", variable=var2)
chckbutton2.pack()
btn = Button(root, text="Submit", command=display_options)
btn.pack()
root.mainloop()
