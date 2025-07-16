from turtle import Turtle
high_score =0



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.write(f"Score : {self.score} Highscore: {self.highscore}", align= "center", font= ("Arial", 14, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore: {self.highscore}", align= "center", font= ("Arial", 14, "normal"))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()

