from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Snake_game\data.txt", mode="r") as data:
          self.heigh_score1 = int(data.read())
           
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_screboard()
    
    def update_screboard(self):
        self.clear()
        self.write(f"Score: {self.score} Heigh Score: {self.heigh_score1}", align=ALIGNMENT, font=FONT)


    def collision(self):
        self.score += 1
        self.update_screboard()

    def heigh_score(self):
        if self.score > self.heigh_score1:
            self.heigh_score1 = self.score
            with open("Snake_game\data.txt", mode="w") as data:
                data.write(f"{self.heigh_score1}")
        self.score = 0
        self.update_screboard()
    # def collision_with_wall(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over!", align=ALIGNMENT, font=FONT)
