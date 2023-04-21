
from tkinter import *

window = Tk()
window.title("Welcome")
window.geometry('720x360')
def hello():
    lbl = Label(window, text="WelloHorld")
    lbl.pack()

btn = Button(window, text="Click me", command=hello)
btn.pack()

window.mainloop()