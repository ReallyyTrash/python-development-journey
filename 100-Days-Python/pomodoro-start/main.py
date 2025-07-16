from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    title.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60

    global reps
    reps += 1
    if reps% 8 == 0:
        countdown(4)
        title.config(text= "Well Done")

    elif reps %2 == 0:
        countdown(3)
        title.config(text= "Rest")

    else:
        countdown(5)
        title.config(text= "WORK")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minute = math.floor(count/60)
    second = count% 60

    if second == 0:
        second = "00"
    canvas.itemconfig(timer_text, text= f"{minute}:{second}")

    if count> 0:
        global timer
        timer = window.after(1000, countdown, count-1 )
    else:
        start_timer()
        mark = ""
        sessions = math.floor(reps/2)
        print(sessions)
        for _ in range(sessions):
            mark += '✔'
        checkmark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer",fg= "green" , bg=YELLOW, font=(FONT_NAME, 50))
title.grid(row=0, column=1)

canvas = Canvas(width=202, height= 224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file= "tomato.png")
canvas.create_image(101, 112, image = image)
timer_text = canvas.create_text(101, 130, text= "00:00", fill= "white", font= (FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2,column=0)

reset_button=Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row = 2, column=2)

checkmark = Label(text= "", fg= GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)






window.mainloop()