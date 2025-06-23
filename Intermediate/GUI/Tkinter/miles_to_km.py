from tkinter import *

"""This is a simple Tkinter application that converts miles to kilometers."""

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=0)
window.config(padx = 10, pady =20)



def calculate_km():
    miles = float(input_miles.get())
    km_score = miles * 1.60934
    label_km.config(text = km_score)

km_score = 0

input_miles = Entry(width = 10)
input_miles.grid(column=1, row=0, padx = 10, pady =0)


label = Label(text= "Miles", font = ("Arial", 10, "bold"))
label.grid (column=2, row=0)


label = Label(text= "is equal to", font = ("Arial", 10, "bold"))
label.grid (column=0, row=1)

label_km = Label(text= km_score, font = ("Arial", 10, "bold"))
label_km.grid (column=1, row=1)

label = Label(text= "Km", font = ("Arial", 10, "bold"))
label.grid (column=2, row=1)

button = Button(text= "Calculate", font = ("Arial", 10, "bold"), command = calculate_km)
button.grid (column=1, row=3)

window.mainloop()