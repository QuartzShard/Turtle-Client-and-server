import turtle
class yurtle(turtle.Turtle):
    def __init__(self):
        super(yurtle, self).__init__()

yurt = yurtle() #can also assign variables to newly clasified turtle, if they get that far
#yurtle.fd() This doesn't want to work and I'm usure why, claims it's missing an argument
yurt.fd(60)

turtle.exitonclick()