from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flash Card")
window.config(padx = 50, pady = 50,bg=BACKGROUND_COLOR)


#------------------------images---------------------
front_image = PhotoImage(file="Capstone_Projects/Flashcard/images/card_front.png")
back_image = PhotoImage(file="Capstone_Projects/Flashcard/images/card_back.png")
wrong_image = PhotoImage(file= "Capstone_Projects/Flashcard/images/wrong.png")
right_image = PhotoImage(file= "Capstone_Projects/Flashcard/images/right.png")

try:
    data = pandas.read_csv("Capstone_Projects/Flashcard/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("Capstone_Projects/Flashcard/data/french_words.csv")


data_frame = data.to_dict(orient="records")



def new_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    
    current_card = random.choice(data_frame) 
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(language_text, text = "French" ,fill="black")
    canvas.itemconfig(word_text, fill="black", text = (current_card['French']))
    flip_timer = window.after(3000, flip_canvas)
    
def flip_canvas():
    canvas.itemconfig(card_image,image = back_image)
    canvas.itemconfig(language_text, text = "English", fill="white")
    canvas.itemconfig(word_text, fill="white",text = (current_card['English']))

flip_timer = window.after(3000, flip_canvas)



#-----remove known words from the list

def on_right():
    global data_frame

    # Remove the current card from the list
    data_frame.remove(current_card)

    # Save updated list to a new file
    new_data = pandas.DataFrame(data_frame)
    new_data.to_csv("Capstone_Projects/Flashcard/data/words_to_learn.csv", index=False)

    # Show next card
    new_card()






#-----canvas --------
canvas = Canvas(width=800, height=526)
card_image = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#------------button ----------
wrong_button = Button(image=wrong_image, highlightthickness=0,command=new_card)
wrong_button.grid(row = 1, column =0)

right_button = Button(image=right_image, highlightthickness=0,command=on_right)
right_button.grid(row = 1, column =1)

new_card()

window.mainloop()