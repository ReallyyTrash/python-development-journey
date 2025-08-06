import pandas, random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn={}
# --------- Read Data----------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Next Card Function
def next_card():
    global current_card, flip_timer # global flip timer??
    window.after_cancel(flip_timer) # doubt??
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image= card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text = current_card["French"])
    flip_timer = window.after(3000, flip_card) # doubt


# Flip card
def flip_card():
    canvas.itemconfig(card_image, image=card_back_img, fill="white")
    canvas.itemconfig(card_title, text= "English", fill= "white")
    canvas.itemconfig(card_word, text = current_card["English"], )

def is_known():
    to_learn.remove(current_card)
    data= pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ------------UI-----------

# Window
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, pady= 50, padx=50)

flip_timer  = window.after(3000, flip_card) # doubt


# Images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image= PhotoImage(file="images/right.png")

# Card
canvas = Canvas(width=800, height=526, highlightthickness=  0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text= "title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text= "word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row = 0, columnspan=2)


# Buttons
wrong_button= Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row= 1, column=0)

right_button = Button(image = right_image,highlightthickness=0, command=is_known)
right_button.grid(row=1, column =1)

next_card()

window.mainloop()