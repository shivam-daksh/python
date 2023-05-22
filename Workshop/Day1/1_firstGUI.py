from tkinter import *
m = Tk()
m.title("First Graphic UI Program")
w = Label(m, text="Hello, Welcome to My First GUI Program!") # Create a label with words
w.pack()
def kuch():
    print("Hi there! I am clicked. (check IDLE)")
def kuch1():
    messagebox.showinfo("Warning!","""Oh hell! Get out of here ASAP!
    Un elefante, muy elegante
    la trompa muy larga, la trompa gigante
    uuuuuuuuuu, muy larga,
    uuuuuuuu, (gigante)

""")
    
m.geometry("800x600")
def on_enter(event):
    b2.config(foreground='white', background="#6E8389")

def on_leave(event):
    b2.config(foreground='white', background="#4A646C")
b1 = Button(m,text = "Mera Button",command = m.destroy, activebackground="grey",)  
b1.pack()
b2 = Button(m,text = "Mam Ka Button",
            command = kuch,
            padx=30,
            pady=10,
            activeforeground="white",
            activebackground="#253236",
            background="#4A646C",
            foreground="#ffffff",
            border=0,
            cursor="hand2",
            relief="solid",
            font="Poppins")  
b2.bind("<Enter>",on_enter)
b2.bind("<Leave>", on_leave)
b2.pack()

m.mainloop()
