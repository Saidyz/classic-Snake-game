from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")

        self.update_scoreboard()
 

    def update_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score is : {self.score}", align="center", font=('Courier', 16, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=('Courier', 25, 'bold'))



