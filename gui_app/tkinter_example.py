
#import module
#creat GUI main window
#add widgets

# from tkinter import *
# from tkinter.ttk import *

# window = Tk()   # create window object
# window.title("Welcome")
# window.geometry('350x200')  # pixel

# valType = StringVar()
# rad1 = Radiobutton(window, text='First', value="first", variable=valType)
# rad2 = Radiobutton(window, text='Second', value="second", variable=valType)
# rad3 = Radiobutton(window, text='Third', value="third", variable=valType)

# rad1.grid(column=0, row=0)
# rad2.grid(column=1, row=0)
# rad3.grid(column=2, row=0)

# def clickEvent():
#    print(valType.get())

# btn = Button(window, text="Click me", command=clickEvent)
# btn.grid(column=3, row=0)

# window.mainloop()  # run endless loop

# from tkinter import *
# from tkinter import messagebox

# window = Tk()
# window.title("Welcome")
# window.geometry('350x200')

# def clicked():
#     # messagebox.showinfo('Message title', 'Message content')
#     # messagebox.showwarning('Message title', 'Message content')
#     # messagebox.showerror('Message title', 'Message content')
#     # res = messagebox.askyesno('Message title', 'Message content')
#     # print(res)
#     # res = messagebox.askokcancel('Message title', 'Message content')
#     # print(res)
#     # res = messagebox.askyesnocancel('Message title', 'Message content')
#     # print(res)
#     res = messagebox.askretrycancel('Message title', 'Message content')
#     print(res)

# btn = Button(window, text='Click here', command=clicked)

# btn.grid(column=0, row=0)
# window.mainloop()

# from tkinter import *

# window = Tk()
# window.title("Welcome")
# window.geometry('350x200')

# spin = Spinbox(window, values=(2,4,6,8,20), width=5)
# spin.grid(column=0, row=0)

# window.mainloop()


from tkinter import * 
windown = Tk()
windown.geometry("500x500")

btn_height = Button(windown, text="50px high")
btn_height.place(height=50, x=200, y=200)

btn_width = Button(windown, text="60px wide")
btn_width.place(width=60, x=300,y=300)

btn_relheight = Button(windown, text="Relheight of 0.6")
btn_relheight.place(relheight=0.6)

btn_relwidth = Button(windown, text="Relwidth of 0.2")
btn_relwidth.place(relwidth=0.2)

btn_x = Button(windown, text="X = 400px")
btn_x.place(x=400)

btn_y = Button(windown, text="Y = 321px")
btn_y.place(y=321)

windown.mainloop()

