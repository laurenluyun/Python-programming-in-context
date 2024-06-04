# -*- coding = utf-8 -*-
# @Time : 5/25/2023 1:53 PM
# @Author : Lauren
# @File : Sun.py
# @Software : PyCharm
'''
this program is to build our solar system, which will consist
of a sun and a collection of planets, with each planet defined to
be some distance away from the sun.
'''
import turtle

class Sun:
    def __init__(self, iName, iRad, iM, iTemp):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__temp = iTemp
        self.__x = 0
        self.__y = 0

        self.__sTurtle = turtle.Turtle()
        # we change the shape of the turtle from the default triangle to a
        # circle
        self.__sTurtle.shape("circle")
        self.__sTurtle.color("yellow")

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def getMass(self):
        return self.__mass

    def __str__(self):
        return self.__name


