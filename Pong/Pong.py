import turtle
import winsound

#wn=window
wn=turtle.Screen()
wn.title("Pong by Zero")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #Stops window from updating

#Score
score_P1=0
score_P2=0

#Paddle P1
paddleP1 = turtle.Turtle()
paddleP1.speed(0)
paddleP1.shape("square")
paddleP1.color("white")
paddleP1.shapesize(stretch_wid=5, stretch_len=1)
paddleP1.penup()
paddleP1.goto(-350, 0)

#Paddle P2
paddleP2 = turtle.Turtle()
paddleP2.speed(0)
paddleP2.shape("square")
paddleP2.color("white")
paddleP2.shapesize(stretch_wid=5, stretch_len=1)
paddleP2.penup()
paddleP2.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Pen (Scoreboard with default score)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0           player 2: 0", align="center", font=("Courier", 20, "normal"))

#moving ball
ball.dx = 0.27
ball.dy = 0.27

#Moving paddles
def P1up():
    y=paddleP1.ycor()
    y+=20
    paddleP1.sety(y)
def P1down():
    y=paddleP1.ycor()
    y-=20
    paddleP1.sety(y)

def P2up():
    y=paddleP2.ycor()
    y+=20
    paddleP2.sety(y)
def P2down():
    y=paddleP2.ycor()
    y-=20
    paddleP2.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(P1up, "w")
wn.onkeypress(P1down, "s")
wn.onkeypress(P2up, "Up")
wn.onkeypress(P2down, "Down")

#Main game loop
while True:
    wn.update()
    #move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Boarder checking
    #top
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1 # reverses direction of ball
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    #bottom
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1 # reverses direction of ball
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    #right
    if ball.xcor() >= 390:
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        score_P1 += 1
        pen.clear()
        pen.write("Player 1: {}           player 2: {}".format(score_P1, score_P2), align="center", font=("Courier", 20, "normal"))

    #left
    if ball.xcor() <= -390:
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        score_P2 += 1
        pen.clear()
        pen.write("Player 1: {}           player 2: {}".format(score_P1, score_P2), align="center", font=("Courier", 20, "normal"))
    #Paddle and ball collions
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor()<paddleP2.ycor()+50 and ball.ycor() > paddleP2.ycor()-50:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor()<paddleP1.ycor()+50 and ball.ycor() > paddleP1.ycor()-50:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)