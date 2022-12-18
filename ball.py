from turtle import Turtle

class Ball(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_vel = 10
        self.y_vel = 10

    def move(self):
        new_x = self.xcor() + self.x_vel
        new_y = self.ycor() + self.y_vel

        self.goto(new_x, new_y)

    def bounce(self):
        self.y_vel *= -1

    def bounce_paddle(self):
        self.x_vel *= -1

    def reset(self):
        self.goto(0, 0)
        self.x_vel = 10
        self.y_vel = 10
