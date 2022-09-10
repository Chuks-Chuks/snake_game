from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.count = 0
        self.update_score()

    def update_score(self):
        self.count += 1
        real_score = self.count - 1
        self.goto(0, 280)
        self.clear()
        self.write(f"SCORE:{real_score}", False, "center", ("Arial", 12, "bold"))
        self.hideturtle()

    def game_over_update(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER.", False, "center", ("Arial", 12, "bold"))
        self.hideturtle()

    def big_meal(self):
        self.count += 5
        self.goto(0, 280)
        self.clear()
        self.write(f"SCORE:{self.count}", False, "center", ("Arial", 12, "bold"))
        self.hideturtle()
