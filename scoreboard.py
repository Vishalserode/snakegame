from turtle import Turtle
ALINGMENT = "center"
FONT =("Arial",15,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def game_over(self):
        self.color("white")
        self.goto(0,0)
        self.write("GAME OVER", align=ALINGMENT, font=FONT)

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)

    def score_reset(self):
        self.score +=1
        self.clear()
        self.update_score()


