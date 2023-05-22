from tkinter import *
from tkinter import ttk
def display_selection():
    selected_items = [listbox.get(i) for i in listbox.curselection()]
    print("Selected Items: ", selected_items)
root = Tk()
root.title("List Selection")
root.geometry("800x600")
listbox = Listbox(root, selectmode=SINGLE)
listbox.pack()
listbox.insert(END, "Item 1")
listbox.insert(END, "Item 2")
listbox.insert(END, "Item 3")
listbox.insert(END, "Item 4")
button = Button(root, text="Submit", command=display_selection)
button.pack()
root.mainloop()
