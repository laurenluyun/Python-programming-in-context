# -*- coding = utf-8 -*-
# @Time : 6/2/2023 9:18 PM
# @Author : Lauren
# @File : LaserCannon.py
# @Software : PyCharm
from turtle import Turtle
from BoundedTurtle import *

class LaserCannon(Turtle):
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__screen = self.getscreen()
        self.__screen.onclick(self.aim)
        self.__screen.onkey(self.shoot, 's')
        self.__screen.onkey(self.quit, 'q')

    def aim(self, x, y):
        heading = self.towards(x, y)
        self.setheading(heading)

    def shoot(self):
        Bomb(self.heading(), 5, self.__xMin, self.__xMax, self.__yMin,
             self.__yMax)

    def quit(self):
        self.__screen.bye()

