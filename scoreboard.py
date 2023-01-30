from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def increase_score(self):
        self.clear()    
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score = {self.score} High score: {self.high_score}", False, align="center", font=("Arial", 20, "normal"))

    def reset(self):
        with open("data.txt", mode="w") as file:
            if self.score > self.high_score:
                print(f"{self.score} e")
                file.write(f"{self.score}")
                self.high_score = self.score
                self.score = 0
                self.update()




