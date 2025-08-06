from mimetypes import guess_type

theme_color = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("quiz game")
        self.window.config(padx= 20, pady=20, bg=theme_color)

        self.canvas = Canvas(width=300, height=250, bg= "white")
        self.question_text = self.canvas.create_text(150,125, text="Question", width= 250,font=("Arial", 25, "italic"), fill = theme_color)
        self.canvas.grid(row=1, column = 0, columnspan=2)

        # Label
        self.score_label = Label(text=f"Score: 0", fg= "white", bg= theme_color)
        self.score_label.grid(row=0, columns=1)

        # Buttons
        true_iamge = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_iamge, highlightthickness= 0, command=self.guess_true)
        self.true_button.grid(row=2, column= 0)
        self.false_button = Button(image = false_image, highlightthickness=0, command=self.guess_false)
        self.false_button.grid(row= 2, column = 1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas_color("white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
            self.canvas_color("white")
        else:
            self.canvas.itemconfig(self.question_text, text= "You have reached the end")
            self.true_button.config(state= "disabled")
            self.false_button.config(state= "disabled")

    def guess_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def guess_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")

            self.window.after(1000, self.get_next_question )
        else:
            self.canvas_color("red")
            self.window.after(1000, self.get_next_question)

    def canvas_color(self, color):
        self.canvas.config(bg=color)

