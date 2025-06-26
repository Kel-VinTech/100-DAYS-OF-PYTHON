from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
# import pyperclip #insall this module using pip install pyperclip
import json

window =  Tk()
window.title("Password Manager")
window.config(padx =50,pady = 50)

image = PhotoImage(file="Intermediate/Password_Manager/logo.png")


#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_new_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0,password)
    # pyperclip.copy(password)  # Copy the generated password to clipboard

def save():

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    new_data = {
        website:{
            "email": email,
            "password":password
    
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill in all fields.")
    else:
            try:
                with open("data.json", "r") as data_file:
                    # json.dump(new_data,data_file,indent=4)
                    data = json.load(data_file) # how to read data from json file
            
            except FileNotFoundError:
                with open("data,json", "w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:     
                data.update(new_data)   
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent =4)
            finally:
                    entry_website.delete(0, END)  # Clear the website entry field
                    entry_password.delete(0, END)  # Clear the password entry field



def find_password():
    website = entry_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file) 
    except FileNotFoundError:
            messagebox.showinfo(title = "Error", message = "Data not found")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title = website, message =f"Email: {email}\n password: {password}")
            else:
                messagebox.showinfo(title = "Error", mesage =f"No details for {website} exits")



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

entry_website = Entry(width=21)
entry_website.grid(column=1, row=1, columnspan=1)
entry_website.focus()  # Set focus on the website entry field

entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "email@gmail.com")

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)


button_password = Button(text="Generate Password", width=13, command=generate_new_password)
button_password.grid(column=2, row=3)

button_add = Button(text="Add", width=40, command=save)
button_add.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width =13 ,command=find_password)
search_button.grid(row=1,column=2)

window.mainloop()