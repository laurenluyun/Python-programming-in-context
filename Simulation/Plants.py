# -*- coding = utf-8 -*-
# @Time : 5/30/2023 6:11 PM
# @Author : Lauren
# @File : Plants.py
# @Software : PyCharm
import turtle
import random

class Plants:
    def __init__(self):
        self.__turtle = turtle.Turtle()
        self.__turtle.up()
        self.__turtle.hideturtle()
        # change the cursor as plant pic
        self.__turtle.shape("Plant.gif")

        self.__xPos = 0
        self.__yPos = 0
        self.__world = None

        self.__breedTick = 0

    def setX(self, newX):
        self.__xPos = newX

    def setY(self, newY):
        self.__yPos = newY

    def getX(self):
        return self.__xPos

    def getY(self):
        return self.__yPos

    def setWorld(self, aWorld):
        self.__world = aWorld

    def appear(self):
        self.__turtle.goto(self.__xPos, self.__yPos)
        # makes the turtle cursor visible on the screen. When called, it
        # displays the turtle cursor if it was previously hidden.
        self.__turtle.showturtle()

    def hide(self):
        self.__turtle.hideturtle()


    def liveALittle(self):
        self.__breedTick += 1
        if self.__breedTick >= 5:
            self.tryToBreed()

    def tryToBreed(self):
        # first pick a random adjacent location
        offsetList = [(-1, 1), (0, 1), (1, 1),
                      (-1, 0), (1, 0),
                      (-1, -1), (0, -1), (1, -1)]
        randmOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randmOffsetIndex]
        nextX = self.__xPos + randomOffset[0]
        nextY = self.__yPos + randomOffset[1]

        # once we compute the new position, we must be sure it is in the
        # actual range of legal coordinates. If not, we must try again with
        # the while loop. - it continues to choose random offset pairs
        # until a legal result is obtained
        while not (0 <= nextX < self.__world.getMaxX() and 0 <= nextY < \
                    self.__world.getMaxY()):
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            nextX = self.__xPos + randomOffset[0]
            nextY = self.__yPos + randomOffset[1]

        # Once a new random location has been determined, the rules
        # state that it must be empty for breeding to take place.
        if self.__world.emptyLocation(nextX, nextY):
            # if empty, a new fish is created and added to the world at
            # that location
            childThing = Plants()
            self.__world.addThing(childThing, nextX, nextY)
            self.__breedTick = 0 # reset breedTick
