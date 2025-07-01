from tkinter import *
from quiz_brain import QuizBrain



THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):

        self.quiz = quiz_brain 
        self.window = Tk()
        self.window.title = ("Quizzler")
        self.window.config(padx =20,pady =20, bg =THEME_COLOR)


        true_image = PhotoImage(file="Intermediate/Quiz App/images/true.png")
        false_image = PhotoImage(file="Intermediate/Quiz App/images/false.png")


        self.score = Label(text = "Score:0", bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score.grid(row=0, column=1,)


        self.canvas = Canvas(width=300, height = 250, bg ="white")
        self.question_text = self.canvas.create_text(
            150,
            125, 
            width =260,
            text = "text", 
            font=("Arial",20,"italic") ,
            fill=THEME_COLOR
        )
        self.canvas.grid(row= 1, column = 0, columnspan=2, pady= 50)

        self.good_tick = Button(image = true_image,command = self.true_pressed, highlightthickness=0)
        self.good_tick.grid(row=2,column=0)

        self.bad_tick = Button(image =false_image,command =self.false_pressed, highlightthickness=0)
        self.bad_tick.grid(row=2,column=1)


        self.get_next_question()


        self.window.mainloop()

        
    def get_next_question(self):
        self.canvas.config(bg ="white")
        if self.quiz.still_has_questions():
            
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You have reached the end of the quiz")
            self.good_tick.config(state="disabled")
            self.bad_tick.config(state = "disabled")
    def true_pressed(self):
        self.give_feedack(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedack(is_right)
        
    def give_feedack(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)