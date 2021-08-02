#Space Invaders
#Set up the screen
#home pc
import turtle
import os

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw Border

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create player 
turtle.pen(fillcolor="blue", pensize=3)
turtle.shape("triangle")
turtle.penup()
turtle.setposition(0, -250)
turtle.setheading(90)

#Player movement (speed)
turtlespeed = 25

#Create the enemy
enemy = turtle.Turtle()
enemy.pen(fillcolor="red", pensize=3)
enemy.shape("circle")
enemy.penup()
enemy.setposition(0,250)
enemy.setheading(270)

enemyspeed = 5


#Player movement left and right ((move_left) x is the difference between(-=) x and turtle speed.)
def move_left():
    x = turtle.xcor()
    x -= turtlespeed
    if x <-280:
        x = -280
    turtle.setx(x)
    
def move_right():
    x = turtle.xcor()
    x += turtlespeed
    if x > 280:
        x = 280
    turtle.setx(x)

    
#Player movement up and down (set up boundries with boundry checking (if))
def move_up():
    y = turtle.ycor()
    y += turtlespeed
    if y >280:
        y = 280
    turtle.sety(y)
    
def move_down():
    y = turtle.ycor()
    y -= turtlespeed
    if y < -280:
        y = -280
    turtle.sety(y)

#Create kyeboard bindings (left,right,up,down)
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")

#Main game loop
while True:
    
    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    
    #Move the enemy back and forth
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
        
        
    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
    












delay = input("Press enter to finish.")