# -*- coding = utf-8 -*-
# @Time : 5/31/2023 5:58 PM
# @Author : Lauren
# @File : House.py
# @Software : PyCharm
import turtle
from Canvas import Canvas
from GeometricObject import *

def drawHouse():
    myCanvas = Canvas(500, 500)
    # line1 = Line(Point(-100, -100), Point(100, 100))
    # line2 = Line(Point(-100, 100), Point(100, -100))
    # line1.setWidth(4)
    # myCanvas.draw(line1)
    # myCanvas.draw(line2)
    # line1.setColor('red')
    # line2.setWidth(4)


    house = Rectangle(Point(-100, -100), Point(100, 100))
    house.setFillColor('blue')

    door = Rectangle(Point(-50, -100), Point(0, 50))
    door.setFillColor('brown')

    roof1 = Line(Point(-100, 100), Point(0, 200))
    roof2 = Line(Point(0, 200), Point(100, 100))
    roof1.setWidth(3)
    roof2.setWidth(3)

    # sun = Circle(Point(150, 250), 20)
    # sun.setFill('yellow')

    myCanvas.draw(house)
    myCanvas.draw(door)
    myCanvas.draw(roof1)
    myCanvas.draw(roof2)
    # myCanvas.draw(sun)

    turtle.exitonclick()

def main():
    drawHouse()

if __name__ == "__main__":
    main()