from turtle import *
def Rectangle():


    for i in range(2):
        forward(150)
        left(90)
        forward(75)
        left(90)

    exitonclick()

def ColorRectangle():
    bgcolor("lightgreen")
    color("blue")
    pensize(3)
    for i in range(2):
        forward(150)
        left(90)
        forward(75)
        left(90)
    exitonclick()
def ColorfulSquare():
    bgcolor("black")
    color("Red")
    forward(200)
    left(90)
    color("blue")
    forward(200)
    left(90)
    color("Yellow")
    forward(200)
    left(90)
    color("Green")
    forward(200)
    left(90)

ColorfulSquare()
