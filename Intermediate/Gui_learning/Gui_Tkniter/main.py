from tkinter import * 
"""This is a simple Tkinter application that creates a window with a title and a size."""

"""Adanced Arguments: 
(*args, **kwargs) allows you to pass a variable number of arguments to a function.
*(args- can be named anything)is used to pass a non-keyworded variable-length argument list(unlimited postional arguments)
**kwargs- can be named anything) is used to pass a keyworded variable-length argument list(unlimited keyword arguments).
This is useful when you want to create functions that can accept any number of arguments without explicitly defining them.
For example, you can use *args to pass a list of numbers to a function that calculates their sum,
or **kwargs to pass a dictionary of key-value pairs to a function that processes
"""

# we have 3 layout system, pack, grid, place

def button_clicked():
    label.config(text = input.get())


window = Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 300)
window.config(padx=20, pady=20)  # padding around the window

label = Label(text="Hello", font = ("Arial",24, "bold"))
label.grid(column = 0 , row = 0)


button = Button(text="Click Me!", command = button_clicked)
button.grid(column = 2, row = 0)

button = Button(text="Click Me!", command = button_clicked)
button.grid(column = 1, row = 1)

input = Entry(width=10)
input.grid(column=3, row=2)

""" for more widgets, check out the official documentation:
https://www.tcl-lang.org/man/tcl8.6/TkCmd/contents.htm"""
















window.mainloop()