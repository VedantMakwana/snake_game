from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("D:\high_score.txt",mode="r") as f:
            self.high_score=int(f.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.count()

    def count(self):
        self.goto(0,270)
        self.clear()
        self.write(f"highestscore: {self.score} "
                   f"High Score: {self.high_score}",True,align="center",font=("",20,""))

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("D:\high_score.txt",mode="w") as f:
                f.write(str(self.high_score))
        self.score=0
        self.count()