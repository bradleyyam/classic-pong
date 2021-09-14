# Simple Pong in Python 3 for Beginners
# Adapted from @TokyoEdTech

import turtle
import time

width = 800
height = 600
max_width = width/2
min_width = -width/2
max_height = height/2 
min_height = -height/2
leftScore = 0
rightScore = 0

wn = turtle.Screen()
wn.title("Pong for Coral Academy")
wn.bgcolor("black")
wn.setup(width=width,height=height)
wn.tracer(0)

# Score

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("{}                               {}".format(leftScore, rightScore), align = "center", font=("Courier", 24, "normal"))

# Objects

## Left Paddle

leftPad = turtle.Turtle()
leftPad.speed(0)
leftPad.shape("square")
leftPad.color("white")
leftPad.shapesize(stretch_wid=5, stretch_len=1)
leftPad.penup()
leftPad.goto(-350, 0)

## Right Paddle

rightPad = turtle.Turtle()
rightPad.speed(0)
rightPad.shape("square")
rightPad.color("white")
rightPad.shapesize(stretch_wid=5, stretch_len=1)
rightPad.penup()
rightPad.goto(350, 0)

## Ball(s)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Actions

## Bounds Check

def bound_check(y):
    if y > max_height - 50:
        return max_height - 50
    elif y < min_height + 50:
        return min_height + 50
    else:
        return y

## Update Score

def update_score(left, right):
    score.clear()
    score.write("{}                               {}".format(left, right), align = "center", font=("Courier", 24, "normal"))

## Move Left Pad

def leftPad_up():
    y = leftPad.ycor()
    y+=20
    
    y = bound_check(y)
    leftPad.sety(y)

def leftPad_down():
    y = leftPad.ycor()
    y-=20
    y = bound_check(y)
    leftPad.sety(y)

def rightPad_up():
    y = rightPad.ycor()
    y+=20
    y = bound_check(y)
    rightPad.sety(y)

def rightPad_down():
    y = rightPad.ycor()
    y-=20
    y = bound_check(y)
    rightPad.sety(y)

# Key Binding

wn.listen()
wn.onkeypress(leftPad_up, "w")
wn.onkeypress(leftPad_down, "s")
wn.onkeypress(rightPad_up, "Up")
wn.onkeypress(rightPad_down, "Down")

# Main Game Loop

while True:
    wn.update()
    time.sleep(0.01)

    # move the ball
    ball.setx(ball.xcor() +  ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > max_height - 10:
        ball.dy *= -1

    if ball.ycor() < min_height + 10:
        ball.dy *= -1

    # win condition

    if ball.xcor() > max_width - 10:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        leftScore += 1
        update_score(leftScore, rightScore)

    if ball.xcor() < min_width + 10:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        rightScore += 1
        update_score(leftScore, rightScore)

    # collision

    ## collision with left pad

    if ball.xcor() < leftPad.xcor() + 20 and ball.xcor() > leftPad.xcor() - 20 and ball.ycor() < leftPad.ycor() + 50 and ball.ycor() > leftPad.ycor() - 50:
        ball.setx(leftPad.xcor() + 20)
        ball.dx *= -1

    ## collision with right pad

    if ball.xcor() > rightPad.xcor() - 20 and ball.xcor() < rightPad.xcor() + 20 and ball.ycor() < rightPad.ycor() + 50 and ball.ycor() > rightPad.ycor() - 50:
        ball.setx(rightPad.xcor() - 20 )
        ball.dx *= -1



