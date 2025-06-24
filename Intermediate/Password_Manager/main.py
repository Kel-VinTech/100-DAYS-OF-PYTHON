from tkinter import *


window =  Tk()
window.title("Password Manager")
window.config(padx =20,pady = 20)

image = PhotoImage(file="Intermediate/Password_Manager/logo.png")

canvas = Canvas(width=400, height=400)
canvas.create_image(200, 200, image=image)
canvas.grid(column=0, row=0)




window.mainloop()