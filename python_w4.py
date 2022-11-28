import turtle
import random
# Function definition appears before the function is called

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
# Main program starts after all function definitions
win = turtle.Screen()
win.bgcolor("black")
tito = turtle.Turtle()
# Call the function to draw the square with actual values for turtle and side
# draw_square(tito, 150)
# win.exitonclick()
tito.speed(0)
tito.pensize(3)
def draw_colorful_square(t,sz):
    for i in range(4):
        t.color(random.random(),random.random(),random.random())
        t.forward(sz)
        t.left(90)

size = 100
for i in range(300):
    draw_colorful_square(tito,size)
    size = size + 10
    tito.forward(10)
    tito.right(18)
win.exitonclick()