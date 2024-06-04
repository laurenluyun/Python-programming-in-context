# -*- coding = utf-8 -*-
# @Time : 5/31/2023 6:02 PM
# @Author : Lauren
# @File : Canvas.py
# @Software : PyCharm
'''
The Canvas class is responsible in some way for drawing a
GeometricObject
'''
import turtle

class Canvas:
    def __init__(self, width, height):
        self.__visibleObjects = [] # a list of shapes to draw
        self.__turtle = turtle.Turtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width = width, height = height)
        self.__turtle.hideturtle()

    def drawAll(self):
        '''
        we can use this method to re-create whatever picture is visible on
        the canvas by calling a single method
        '''
        self.__turtle.reset() # this method creates a blank canvas by
        # erasing anything previously drawn by the turtle, and puts the
        # turtle in the center of the canvas again
        self.__turtle.up()
        self.__screen.tracer(0)
        for shape in self.__visibleObjects: # draw all shapes in order
            shape._draw(self.__turtle)
        self.__screen.tracer(1)
        self.__turtle.hideturtle()

    def addShape(self, shape):
        self.__visibleObjects.append(shape)

    def draw(self, gObject):
        '''
        notice: draw accepts a geometric object gObject as a parameter.
        '''
        gObject.setCanvas(self)
        gObject.setVisible(True)
        self.__turtle.up() # prepare to move turtle w/o trail
        self.__screen.tracer(0) # turn off animation
        # the draw method belongs to the Canvas, while the _draw method
        # belongs to the GeometricObject
        # We use _draw in this case to differentiate it from the draw
        # method in the Canvas class, and to prevent programmers
        # from inadvertently calling the draw method directly on a
        # GeometricObject. And the gObject will draw using the turtle of
        # the class Canvas
        gObject._draw(self.__turtle)
        self.__screen.tracer(1) # turn on animation
        self.addShape(gObject) # all objects that are visible on the canvas
        # are stored in the __visibleObjects list

