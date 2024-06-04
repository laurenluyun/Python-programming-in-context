# -*- coding = utf-8 -*-
# @Time : 6/2/2023 9:24 PM
# @Author : Lauren
# @File : BoundedTurtle.py
# @Software : PyCharm

'''
The BoundedTurtle class is an abstract class that will be the superclass of
both the Drone and Bomb classes. The difference between a regular Turtle and a
BoundedTurtle is that the BoundedTurtle knows when it is outside the window.
When the turtle is outside the window, it disappears.
'''
import math
import random
from abc import *
from turtle import Turtle

class BoundedTurtle(Turtle):
    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__speed = speed

    def outOfBounds(self):
        xPos, yPos = self.position()
        out = False
        if xPos < self.__xMin or xPos > self.__xMax:
            out = True
        if yPos < self.__yMin or yPos > self.__yMax:
            out = True
        return out

    def getSpeed(self):
        return self.__speed

    def getXMin(self):
        return self.__xMin

    def getXMax(self):
        return self.__xMax

    def getYMin(self):
        return self.__yMin

    def getYMax(self):
        return self.__yMax

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Drone(BoundedTurtle):
    droneList = [] # static variable
    #  It is a method that can be called directly on the class itself, without
    #  the need to create an object (instance) of the class.  It is associated
    #  with the class and not with any specific instance of the class.
    # Static methods can directly access static variables of the class without the need for an instance.

    @staticmethod
    def getDrones():
        # list comprehension provides a concise way to create a list w.o
        # using a for loop with an append inside it
        # it also filters out the dead drones every time a new drone is
        # created. This performance improvement keeps the list nice and short.
        return [x for x in Drone.droneList if x.__alive] # use static variable

    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.getscreen().tracer(0)
        self.up()

        '''
        checks whether the 'Drone.gif' file has been loaded. If it has been 
        loaded once, it is not necessary to load it again because the 
        addshape method just loads a list of shapes that works for all the 
        turtles in the same window.
        '''
        if 'Drone.gif' not in self.getscreen().getshapes():
            self.getscreen().addshape('Drone.gif')

        self.shape('Drone.gif')
        self.goto(random.randint(xMin - 1, xMax - 1), yMax - 20)
        self.setheading(random.randint(250, 290))
        self.getscreen().tracer(1)
        # returns all the live drones by constructing a new list created
        # from the instances of Drone
        Drone.droneList = Drone.getDrones() # use static method
        Drone.droneList.append(self)
        self.__alive = True
        self.getscreen().ontimer(self.move, 200)

    def move(self):
        '''
        The move method checks whether the drone is out of bounds.
        If the drone stays in bounds, the timer is reset so that the drone
        will move again in 200 milliseconds. If the drone is out of
        bounds, the drone is removed and the timer is not reset.
        '''
        self.forward(self.getSpeed())
        if self.outOfBounds():
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 200)

    def remove(self):
        '''
        The remove method marks the drone as dead and hides it so
        it is no longer seen.
        '''
        self.__alive = False
        self.hideturtle()

class Bomb(BoundedTurtle):
    def __init__(self, initHeading, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.resizemode('user')
        self.color('red', 'red')
        self.shape('circle')
        self.turtlesize(.25)
        self.setheading(initHeading)
        self.up()
        self.getscreen().ontimer(self.move, 100)

    def move(self):
        exploded = False
        self.forward(self.getSpeed())
        for a in Drone.getDrones(): # use static method
            if self.distance(a) < 5:
                # remove the drone
                a.remove()
                exploded = True

        if self.outOfBounds() or exploded: # remove the bomb
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 100)

    def distance(self, other):
        p1 = self.position()
        p2 = other.position()
        return math.dist(p1, p2)

    def remove(self):
        self.hideturtle()



