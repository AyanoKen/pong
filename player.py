from turtle import Turtle

class Player:

    def __init__(self, color= "white", position= (0, 0), speed= 20):
        
        self.paddle = Turtle(shape= "square")
        self.paddle.color(color)
        self.paddle.shapesize(stretch_wid= 5, stretch_len= 1)
        self.paddle.penup()
        self.paddle.goto(position)
        self.speed = speed

    def up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + self.speed)

    def down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - self.speed)
