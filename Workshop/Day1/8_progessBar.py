from tkinter import *
from tkinter.ttk import Progressbar
root = Tk()
root.title("Progress Bar")
root.geometry("800x600")
p = Progressbar(root, orient=VERTICAL, length=1000, mode="determinate")
p.pack()
def update_p():
    for i in range(101):
        progess['value'] = i
        root.update_idletasks()
        time.sleep(0.1)
button = Button(root, text="Start", command=update_p)
button.pack()
root.mainloop()
