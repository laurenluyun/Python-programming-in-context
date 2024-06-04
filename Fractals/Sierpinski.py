# -*- coding = utf-8 -*-
# @Time : 5/24/2023 4:00 PM
# @Author : Lauren
# @File : Sierpinski.py
# @Software : PyCharm
import turtle
t = turtle.Turtle()

def drawTriangle(t, p1, p2, p3):
    t.up()
    t.goto(p1)
    t.down()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)

def midPoint(p1, p2):
    return ((p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0)

def sierpinski(t, p1, p2, p3, depth):
    if depth > 0:
        sierpinski(t, p1, midPoint(p1, p2), midPoint(p1, p3), depth - 1)
        sierpinski(t, p2, midPoint(p2, p3), midPoint(p2, p1), depth - 1)
        sierpinski(t, p3, midPoint(p3, p1), midPoint(p3, p2), depth - 1)
    else:
        # base case
        drawTriangle(t, p1, p2, p3)

def main():
    t.color('darkorange')
    sierpinski(t, [-225, -250], [225, -250], [0, 225], 5)
    t.hideturtle()

if __name__ == "__main__":
    main()