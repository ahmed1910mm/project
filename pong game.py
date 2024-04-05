import turtle
import pygame
import time

# Initialize pygame
pygame.mixer.init()

# Load sound effects
score_sound = pygame.mixer.Sound("./sounds/score.wav")  # Replace "score.wav" with the path to your scoring sound effect file
collision_sound = pygame.mixer.Sound("./sounds/collision.wav")  # Replace "collision.wav" with the path to your collision sound effect file

wind = turtle.Screen()
wind.title("Ping Pong Game")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# racket 1
racket1 = turtle.Turtle()
racket1.speed(0)
racket1.shape("square")
racket1.color("red")
racket1.shapesize(stretch_wid=5, stretch_len=1)
racket1.penup()
racket1.goto(-350, 0)

# racket 2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("yellow")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.penup()
racket2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.22
ball.dy = -0.22

# Score
score1 = 0
score2 = 0
max_score = 5  # Set your desired maximum score here
score = turtle.Turtle()
score.speed(0)
score.color("#d3d3d3")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def racket1_up():
    y = racket1.ycor()
    y += 20
    racket1.sety(y)

def racket1_down():
    y = racket1.ycor()
    y -= 20
    racket1.sety(y)

def racket2_up():
    y = racket2.ycor()
    y += 20
    racket2.sety(y)

def racket2_down():
    y = racket2.ycor()
    y -= 20
    racket2.sety(y)

# Keyboard bindings
wind.listen()
wind.onkeypress(racket1_up, "w")
wind.onkeypress(racket1_down, "s")
wind.onkeypress(racket2_up, "Up")
wind.onkeypress(racket2_down, "Down")

# Main game loop
while True:
    wind.update()  # Update the screen
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        collision_sound.play()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        collision_sound.play()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        score_sound.play()
        
        if score1 >= max_score:
            score.clear()
            score.write("Player 1 wins!", align="center", font=("Courier", 24, "normal"))
            wind.update()  # Update the screen
            time.sleep(3)  # Show the end screen for 3 seconds
            break

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        score_sound.play()
        
        if score2 >= max_score:
            score.clear()
            score.write("Player 2 wins!", align="center", font=("Courier", 24, "normal"))
            wind.update()  # Update the screen
            time.sleep(3)  # Show the end screen for 3 seconds
            break
   
    # Ball collides with the racket
    if (ball.xcor() > 340 and ball.xcor() < 350) and (racket2.ycor() - 50 < ball.ycor() < racket2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        collision_sound.play()

    if (ball.xcor() < -340 and ball.xcor() > -350) and (racket1.ycor() - 50 < ball.ycor() < racket1.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        collision_sound.play()
