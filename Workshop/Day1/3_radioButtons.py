from tkinter import *

def display_option():
    if var.get()==1:
        print("Option 1 selected.")
    elif var.get() ==2:
        print("Option 2 selected.")
root = Tk()
root.title("Radio Button Demo")
root.geometry("800x600")
var = IntVar()
radio1 = Radiobutton(root, text="Option 1", variable=var, value=1)        
radio1.pack()
radio2 = Radiobutton(root, text="Option 2",variable=var, value=2)
radio2.pack()
btn = Button(root, text="Submit", command=display_option)
btn.pack()
root.mainloop()