# -*- coding = utf-8 -*-
# @Time : 5/25/2023 2:09 PM
# @Author : Lauren
# @File : planetclass.py
# @Software : PyCharm
import math
import turtle


class Planet:
    def __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        # add the two velocity components
        self.__velX = iVx
        self.__velY = iVy
        # the initial x value will be the distance from the sun
        self.__x = self.__distance
        # this means all the planets are initially lined up on the x-axis
        self.__y = 0
        self.__color = iC

        # each instance of planet will contain a Turtle
        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")

        # move the planet into its initial position
        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x, self.__y)
        self.__pTurtle.down()

    def moveTo(self, newX, newY):
        # moveto method to modify the coordinates of the planet
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def setName(self, newName):
        self.__name = newName

    def getName(self):
        return self.__name

    def getRadius(self):
        return self.__radius

    def getMass(self):
        return self.__mass

    def getDistance(self):
        return self.__distance

    def getVolume(self):
        v = 4 / 3 * math.pi * self.__radius ** 3
        return v

    def getSurfaceArea(self):
        sa = 4 * math.pi * self.__radius ** 2
        return sa

    def getDensity(self):
        d = self.__mass / self.getVolume()
        return d

    def __str__(self):
        return self.__name

    def __lt__(self, otherPlanet):
        # the distance is less than the distance of the other planet
        return self.__distance < otherPlanet.__distance

    def __gt__(self, otherPlanet):
        return self.__distance > otherPlanet.__distance







