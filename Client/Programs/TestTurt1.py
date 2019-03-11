import turtle
def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

for i in range(8):
    square(25)
    turtle.right(45)

turtle.exitonclick()