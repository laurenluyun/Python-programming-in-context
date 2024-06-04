# -*- coding = utf-8 -*-
# @Time : 5/25/2023 2:09 PM
# @Author : Lauren
# @File : solarsystem.py
# @Software : PyCharm
import turtle
import math


class SolarSystem:
    def __init__(self, width, height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        # since the turtle will not actually draw anything, we will hide it
        # so that the shape cannot be seen.
        self.__ssTurtle. hideturtle()
        self.__ssScreen = turtle.Screen()
        # create a coordinate system that is equally distributed around the
        # position(0, 0)
        self.__ssScreen.setworldcoordinates(-width/2.0, -height/2.0,
                                            width/2.0, height/2.0)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def addSun(self, aSun):
        self.__theSun = aSun

    def showPlanets(self):
        for aPlant in self.__planets:
            print(aPlant)

    def freeze(self):
        # the method simply lets the user freeze the screen after the
        # animation has been completed
        self.__ssScreen.exitonclick()

    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.__planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt *
                     p.getYVel())
            # the distance between the planet and the sun in x
            rX = self.__theSun.getXPos() - p.getXPos()
            # the distance between the planet and the sun in y
            rY = self.__theSun.getYPos() - p.getYPos()
            r = math.sqrt(rX ** 2 + rY ** 2)

            accX = G * self.__theSun.getMass() * rX / r ** 3
            accY = G * self.__theSun.getMass() * rY / r ** 3

            # reset the XVel and YVel
            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY)

