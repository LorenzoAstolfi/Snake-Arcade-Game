from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score: {self.score} - High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def updating(self):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_file()
        self.score = 0
        self.updating()

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_file(self):
        with open("data.txt", "w") as data:
            data.write(str(self.highscore))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)