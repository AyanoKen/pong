from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, location= (0, 0)):
        super().__init__()
        self.leftscore = 0
        self.rightscore = 0
        self.hideturtle()
        self.penup()
        self.goto(location)
        self.pendown()
        self.color("white")
        self.write(f"{self.leftscore} :: {self.rightscore}", align= "center", font= ("Arial", 24, "normal"))

    def increase_leftscore(self):
        self.leftscore += 1
        self.clear()
        self.write(f"{self.leftscore} :: {self.rightscore}", align= "center", font= ("Arial", 24, "normal"))

    def increase_rightscore(self):
        self.rightscore += 1
        self.clear()
        self.write(f"{self.leftscore} :: {self.rightscore}", align= "center", font= ("Arial", 24, "normal"))