from tkinter import image_names
from turtle import Screen, Turtle
import turtle, pandas

# Screen, Image
screen = Screen()
screen.title("States Game")
image = "indiamap.gif"
screen.addshape(image)
turtle.shape(image)

# Data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
total_states = len(all_states)

guessed = []

score = 0

while len(guessed)  <= total_states:
    # Guessing screen
    answer_state = screen.textinput(f"{score}/{total_states}", "Whats the State Name").title()

    if answer_state in all_states:
        guessed.append(answer_state)
        score = score + 1
        t = Turtle()
        t.hideturtle()
        t.up()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

    elif answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed:
                missed_states.append(state)
                state_data = data[data.state == state]
                t = Turtle()
                t.hideturtle()
                t.penup()
                t.goto(state_data.x.item(), state_data.y.item())
                t.pencolor("Red")
                t.write(state_data.state.item())






screen.exitonclick()