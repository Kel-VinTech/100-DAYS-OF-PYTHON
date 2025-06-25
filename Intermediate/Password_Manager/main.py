from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
# import pyperclip #insall this module using pip install pyperclip

window =  Tk()
window.title("Password Manager")
window.config(padx =50,pady = 50)

image = PhotoImage(file="Intermediate/Password_Manager/logo.png")


#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0,password)
    # pyperclip.copy(password)  # Copy the generated password to clipboard

def save():

    length_website = len(entry_website.get())
    length_email = len(entry_email.get())
    length_password = len(entry_password.get())

    if length_website == 0 or length_email == 0 or length_password == 0:
        messagebox.showerror(title="Error", message="Please fill in all fields.")
    else:

        is_ok = messagebox.askokcancel(title = "website", message = "Do you want to save the data?")


        if is_ok:
            website = entry_website.get()
            email = entry_email.get()
            password = entry_password.get()

            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, END)  # Clear the website entry field
                entry_password.delete(0, END)  # Clear the password entry field




canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

label_website  = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)


label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# "entries"

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()  # Set focus on the website entry field

entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "email@gmail.com")

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)


button_password = Button(text="Generate Password", command=generate_password)
button_password.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()