from tkinter import *
def dispay_value(value):
    print('Selected Value: ', value)
root = Tk()
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL)