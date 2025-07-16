theme_color = "#375362"
from tkinter import *


window = Tk()
window.title("quiz game")
window.config(padx= 50, pady=50, bg=theme_color)

canvas = Canvas(width=300, height=414, bg= "white", highlightthickness=0)
question = canvas.create_text(400,400, text="hi")
canvas.grid(row=1, column = 0, columnspan=2)
# Label
score_label = Label(text=f"Score: ")
score_label.grid(row=0, columns=2)
# Buttons
true_button = Button()
true_button.grid(row=2, column= 0)
false_button = Button()
false_button.grid(row= 2, column = 1)

window.mainloop()