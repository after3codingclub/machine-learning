import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Pole Position Clone")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Player car
car = turtle.Turtle()
car.shape("square")
car.color("red")
car.shapesize(stretch_wid=1, stretch_len=2)
car.penup()
car.speed(0)
car.goto(0, -250)

# Movement speed
car_speed = 15

# Enemy car
enemy = turtle.Turtle()
enemy.shape("square")
enemy.color("blue")
enemy.shapesize(stretch_wid=1, stretch_len=2)
enemy.penup()
enemy.speed(0)
enemy.goto(random.randint(-270, 270), 250)

# Enemy speed
enemy_speed = 10

# Functions
def move_left():
    x = car.xcor()
    x -= car_speed
    if x < -290:
        x = -290
    car.setx(x)

def move_right():
    x = car.xcor()
    x += car_speed
    if x > 290:
        x = 290
    car.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Main game loop
while True:
    # Move the enemy car
    y = enemy.ycor()
    y -= enemy_speed
    enemy.sety(y)

    # Check for collision with the player car
    if car.distance(enemy) < 20:
        print("Game Over!")
        break

    # Check if the enemy car is out of the screen
    if enemy.ycor() < -300:
        enemy.goto(random.randint(-270, 270), 250)

# Close the window on click
wn.exitonclick()
