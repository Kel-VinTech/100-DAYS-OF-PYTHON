from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def rest_timer():
    window.after_cancel(timer)
    timer_label.config(text = "Timer", fg = GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    check_label.config(text= "")
    global rep
    rep =0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global rep
    rep += 1 
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Break",fg = RED,)
    elif rep % 2 ==0:
        count_down(short_break_sec)
        timer_label.config(text = "Break",fg = PINK,)
    else:
        count_down(work_sec)
        timer_label.config(text = "Work",fg = GREEN,)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):


    minutes = math.floor(count / 60)

    canvas.itemconfig(timer_text, text = f"{minutes:02d}:{count % 60:02d}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sesssions = math.floor(rep/2)
        for _ in range(work_sesssions):
            marks += "✔"
            check_label.config(text= marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50 ,bg = YELLOW)

image_dir = "Intermediate/Pomodoro/tomato.png"


timer_label = Label(text = "Timer", font = (FONT_NAME,30, "bold"),fg = GREEN,bg = YELLOW)
timer_label.grid(column = 1, row = 0)
timer_label.config(padx = 0, pady =10)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
image_file = PhotoImage(file = image_dir)
canvas.create_image(100, 112, image=image_file)
timer_text = canvas.create_text(100, 133, text="00:00", font = (FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column = 1,row =1 )


button = Button(text = "Start", font = (FONT_NAME,10, "bold"), command = start_timer, bg = YELLOW,highlightthickness=0)
button.grid(column = 0, row = 2)
# label.config(padx = 0, pady =10)

button = Button(text = "Reset", font = (FONT_NAME,10, "bold"), command = rest_timer, bg = YELLOW, highlightthickness=0)
button.grid(column = 2, row = 2)

check_label = Label( font = (FONT_NAME,10, "bold"), fg = GREEN, bg = YELLOW)
check_label.grid(column = 1, row = 3)
check_label.config(padx = 0, pady =5)

window.mainloop()
