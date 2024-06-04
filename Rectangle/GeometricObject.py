# -*- coding = utf-8 -*-
# @Time : 6/1/2023 12:02 PM
# @Author : Lauren
# @File : GeometricObject.py
# @Software : PyCharm

from abc import * # abc is Abstract Base Class

class GeometricObject(ABC): # inherit from Abstract Base Class
    def __init__(self):
        self.__linecolor = 'black' # default drawing color
        self.__lineWidth = 1 # default line size
        self.__visible = False
        self.__myCanvas = None

    def getColor(self):
        # need the get method to access the instance variable
        return self.__linecolor

    def getWidth(self):
        # need the get method to access the instance variable
        return self.__lineWidth

    def setColor(self, color): # modified to redraw visible shapes
        self.__linecolor = color
        if self.__visible:
            self.__myCanvas.drawAll()


    def setWidth(self, width): # modified to redraw visible shapes
        # same for set width
        self.__lineWidth = width
        if self.__visible:
            self.__myCanvas.drawAll()

    # indicate that method is abstract
    @abstractmethod
    def _draw(self, someTurtle):
        pass   #do nothing

    def setVisible(self, vFlag):
        self.__visible = vFlag

    def getVisible(self):
        return self.__visible

    def setCanvas(self, theCanvas):
        self.__myCanvas = theCanvas

    def getCanvas(self):
        return self.__myCanvas

class Point(GeometricObject):
    '''
    Child Class of GeometricObject
    '''
    def __init__(self, x, y):
        # makes sure the instance variables inherited from Geo are given
        # their proper initial values
        # The super function returns a special super object that knows how
        # to properly call the _ _init_ _ method for the superclass.
        super().__init__()
        self.__x = x
        self.__y = y

    def getCoordinate(self):
        return (self.__x, self.__y)

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def _draw(self, turtle):
        turtle.goto(self.__x, self.__y)
        # Once the turtle is in position, a dot is drawn
        # using the instance variables for the line width and color.
        turtle.dot(self.getWidth(), self.getColor())


class Line(GeometricObject):
    def __init__(self, point1, point2):
        super().__init__()
        self.__point1 = point1
        self.__point2 = point2

    def getPoint1(self):
        return self.__point1

    def getPoint2(self):
        return self.__point2

    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.goto(self.__point1.getCoordinate())
        turtle.down()
        turtle.goto(self.__point2.getCoordinate())
        turtle.up()


class Shape(GeometricObject):
    '''
    another abstract class
    '''
    def __init__(self):
        super().__init__()
        self.__fillColor = None

    def setFillColor(self, aColor):
        self.__fillColor = aColor
        if self.getVisible():
            self.getCanvas().drawAll()

    def getFillColor(self):
        return self.__fillColor

class Polygon(Shape):
    def __init__(self, pList):
        super().__init__()
        self.__corners = pList

    def _draw(self, aTurtle):
        aTurtle.color(self.getColor())
        aTurtle.width(self.getWidth())
        aTurtle.goto(self.__corners[0].getCoordinate())
        aTurtle.down()

        if self.getFillColor() != None:
            aTurtle.fillcolor(self.getFillColor())
            aTurtle.begin_fill()

        for cIndex in range(1, len(self.__corners)):
            aTurtle.goto(self.__corners[cIndex].getCoordinate())

        aTurtle.goto(self.__corners[0].getCoordinate())
        if self.getFillColor() != None:
            aTurtle.end_fill()


    def addPoint(self, aPoint):
        self.__corners.append(aPoint)

    def getPoints(self):
        return self.__corners

class Rectangle(Polygon):
    def __init__(self, lowerLeft, upperRight):
        self.__cornerList = []
        self.__cornerList.append(lowerLeft)
        self.__cornerList.append(Point(lowerLeft.getX(), upperRight.getY()))
        self.__cornerList.append(upperRight)
        self.__cornerList.append(Point(upperRight.getX(), lowerLeft.getY()))
        super().__init__(self.__cornerList)