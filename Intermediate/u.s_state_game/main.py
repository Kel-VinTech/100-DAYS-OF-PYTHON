import turtle
import csv
import pandas



image = "Intermediate/u.s_state_game/blank_states_img.gif"
csv_file = "Intermediate/u.s_state_game/50_states.csv"

screen = turtle.Screen()
screen.title("u.s State Game")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(csv_file)
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    

    if user_answer == "Exit":
        break

    if user_answer in all_state:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == user_answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_answer, align="center")
    

screen.exitonclick()