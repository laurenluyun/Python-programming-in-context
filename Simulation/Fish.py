# -*- coding = utf-8 -*-
# @Time : 5/29/2023 6:23 PM
# @Author : Lauren
# @File : Fish.py
# @Software : PyCharm
import random
import turtle
from Plants import Plants

class Fish:
    def __init__(self):
        self.__turtle = turtle.Turtle()
        self.__turtle.up()
        self.__turtle.hideturtle()
        # change the cursor as fish pic
        self.__turtle.shape("fish3.gif")

        self.__xPos = 0
        self.__yPos = 0
        self.__world = None

        self.__starveTick = 0
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

    def move(self, newX, newY):
        self.__world.moveThing(self.__xPos, self.__yPos, newX, newY)
        self.__xPos = newX
        self.__yPos = newY
        self.__turtle.goto(self.__xPos, self.__yPos)

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
            childThing = Fish()
            self.__world.addThing(childThing, nextX, nextY)
            self.__breedTick = 0 # reset breedTick

    def tryToMove(self):
        # first pick a random adjacent location
        offsetList = [(-1, 1), (0, 1), (1, 1),
                      (-1, 0),         (1, 0),
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
        # state that it must be empty for moving.
        if self.__world.emptyLocation(nextX, nextY):
            self.move(nextX, nextY)

    def tryToEat(self):
        offsetList = [(-1, 1), (0, 1), (1, 1),
                      (-1, 0),         (1, 0),
                      (-1, -1), (0, -1), (1, -1)]
        adjPrey = []  # create a list of adjacent prey
        for offset in offsetList:
            # new x and y values are computed from the current (x,
            # y) location and the current offset tuple
            newX = self.__xPos + offset[0]
            newY = self.__yPos + offset[1]
            # check whether this new location is actually a legal location
            if 0 <= newX < self.__world.getMaxX() and 0 <= newY < \
                    self.__world.getMaxY():
                # check for a life-form - False; check if an object is an
                # instance of a particular class Fish
                if (not self.__world.emptyLocation(newX, newY)) and \
                        isinstance(self.__world.lookAtLocation(newX, newY),
                                   Plants):
                    adjPrey.append(self.__world.lookAtLocation(newX, newY))

        # if any Plant are adjacent, pick random Plant to eat
        if len(adjPrey) > 0:
            randomPrey = adjPrey[random.randrange(len(adjPrey))]
            preyX = randomPrey.getX()
            preyY = randomPrey.getY()

            self.__world.delThing(randomPrey) # delete the Plant
            self.move(preyX, preyY) # move to the Plant's location
            self.__starveTick = 0
        else:
            # if there no Plant adjacent to the Fish, increase the starveTick
            self.__starveTick += 1

    def liveALittle(self):
        # below is for self regulation
        offsetList = [(-1, 1), (0, 1), (1, 1),
                      (-1, 0),         (1, 0),
                      (-1, -1), (0, -1), (1, -1)]
        adjFish = 0 # count adjacent fish
        for offset in offsetList:
            # new x and y values are computed from the current (x,
            # y) location and the current offset tuple
            newX = self.__xPos + offset[0]
            newY = self.__yPos + offset[1]
            # check whether this new location is actually a legal location
            if 0 <= newX < self.__world.getMaxX() and 0 <= newY < \
                    self.__world.getMaxY():
                # check for a life-form - False; check if an object is an
                # instance of a particular class Fish
                if (not self.__world.emptyLocation(newX, newY)) and \
                        isinstance(self.__world.lookAtLocation(newX, newY),
                                   Fish):
                    adjFish += 1
        # if 2 or more adjacent Fish, delete the fish(self)
        if adjFish >= 2:
            self.__world.delThing(self)

        # below is for breed, eat and move
        else:
            # If no overcrowding is taking place, the next activity is to check
            # whether the fish has been active for enough time units to try to
            # breed. According to the rules, a fish must wait 12 time units
            # before trying to breed
            self.__breedTick += 1
            if self.__breedTick >= 12: # if alive 12 or more ticks, breed
                self.tryToBreed()

            self.tryToEat()

            if self.__starveTick == 20:  # if no eaten for 10 ticks, die
                self.__world.delThing(self)
            else:
                # Regardless of whether the fish is successful in breeding,
                # it then tries to move to a new location
                self.tryToMove() # try to move







