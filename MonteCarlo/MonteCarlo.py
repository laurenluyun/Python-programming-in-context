# -*- coding = utf-8 -*-
# @Time : 4/28/2023 3:22 PM
# @Author : Lauren
# @File : MonteCarlo.py
# @Software : PyCharm

import random
import math
import turtle

def montePi(numDarts):

    wn = turtle.Screen()
    drawingT = turtle.Turtle()
    turtle.tracer(0)
    drawingT.speed(0)
    # adjusts the window coordinates so that the point in the lower-left
    # corner of the window is -2, -2, and the point in the upper-right
    # corner of the window is 2, 2
    wn.setworldcoordinates(-2, -2, 2, 2)

    # draw the horizontal axis
    drawingT.up()  # lift the tail
    drawingT.goto(-1, 0)  # move to -1 on the left
    drawingT.down()  # put down the tail
    drawingT.goto(1, 0)  # draw line from left to +1 on the right

    # draw the vertical axis
    drawingT.up()  # lift the tail
    drawingT.goto(0, 1)  # move up to 1
    drawingT.down()  # put down the tail
    drawingT.goto(0, -1)  # draw line down to -1

    inCircle = 0
    drawingT.up()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x ** 2 + y ** 2)
        drawingT.goto(x, y)
        if distance <= 1:
            inCircle += 1
            drawingT.color("blue")
        else:
            drawingT.color("red")

        # draw a dot on the screen at the turtle's current position.
        drawingT.dot()

    pi = inCircle / numDarts * 4
    # tells the drawing window to freeze until the user clicks
    # somewhere inside the window
    turtle.update()
    wn.exitonclick()

    return pi

def main():
    print(montePi(1000))

if __name__ == "__main__":
    main()