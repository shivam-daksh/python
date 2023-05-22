from tkinter import *
from tkinter import ttk
def display_text():
    t=text_area.get("1.0", END)
    print("Entered text: ", t)
root = Tk()
root.title("Text Input Field")   
root.geometry("800x600")
text_area=Text(root)
text_area.pack()
button = Button(root, text="Submit", command=display_text)
button.pack()
root.mainloop()
