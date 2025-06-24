from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50 ,bg = YELLOW)

image_dir = "Intermediate/Pomodoro/tomato.png"


label = Label(text = "Timer", font = (FONT_NAME,30, "bold"),fg = GREEN,bg = YELLOW)
label.grid(column = 1, row = 0)
label.config(padx = 0, pady =10)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
image_file = PhotoImage(file = image_dir)
canvas.create_image(100, 112, image=image_file)
canvas.create_text(100, 133, text="00:00", font = (FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column = 1,row =1 )


button = Button(text = "Start", font = (FONT_NAME,10, "bold"), bg = YELLOW,highlightthickness=0)
button.grid(column = 0, row = 2)
# label.config(padx = 0, pady =10)

button = Button(text = "Reset", font = (FONT_NAME,10, "bold"), bg = YELLOW, highlightthickness=0)
button.grid(column = 2, row = 2)

label = Label(text = "✔", font = (FONT_NAME,10, "bold"), fg = GREEN, bg = YELLOW)
label.grid(column = 1, row = 3)
label.config(padx = 0, pady =5)

window.mainloop()
