from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import ScoreBoard
import time

WIDTH = 1000
HEIGHT = 600

screen = Screen()
screen.bgcolor("black")

screen.setup(width= WIDTH, height= HEIGHT)
screen.tracer(0)

player1 = Player(color= "white", position= (WIDTH/2 - 50, 0), speed= 20)
player2 = Player(color= "white", position= (-WIDTH/2 + 50, 0), speed= 20)
ball = Ball()
scoreboard = ScoreBoard(location= (0, HEIGHT/2 - 50))

screen.listen()
screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")

screen.onkeypress(player2.up, "w")
screen.onkeypress(player2.down, "s")


run_game = True
while run_game:
    screen.update()
    ball.move()

    if abs(ball.ycor()) > HEIGHT/2 - 20:
        ball.bounce()

    if ball.distance(player1.paddle) < 50 and ball.xcor() > WIDTH/2 - 50:
        ball.bounce_paddle()

    if ball.distance(player2.paddle) < 50 and ball.xcor() < -WIDTH/2 + 50:
        ball.bounce_paddle()

    if ball.xcor() > WIDTH/2:
        ball.reset()
        scoreboard.increase_leftscore()

    if ball.xcor() < -WIDTH/2:
        ball.reset()
        scoreboard.increase_rightscore()


    time.sleep(0.1)


screen.exitonclick()