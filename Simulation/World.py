# -*- coding = utf-8 -*-
# @Time : 5/29/2023 6:23 PM
# @Author : Lauren
# @File : World.py
# @Software : PyCharm
import random
import turtle

class World:
    def __init__(self, mX, mY):
        self.__maxX = mX
        self.__maxY = mY
        self.__thingList = []
        self.__grid = []

        # set up a nested list and stored in __grid
        for aRow in range(self.__maxY):
            row = []
            for aCol in range(self.__maxX):
                row.append(None)
            self.__grid.append(row)

        self.__wTurtle = turtle.Turtle()
        self.__wScreen = turtle.Screen()
        self.__wScreen.setworldcoordinates(0, 0, self.__maxX - 1,
                                           self.__maxY - 1)
        # register shape on the screen replace the cursor with shape
        self.__wScreen.register_shape("Bear3.gif")
        self.__wScreen.register_shape("fish3.gif")
        self.__wScreen.register_shape("Plant.gif")
        self.__wTurtle.hideturtle()

    def draw(self):
        # draw the outline of the grid
        # The 0 passed as an argument indicates that the animation should be
        # turned off, and the screen should not update automatically.
        self.__wScreen.tracer(0)
        self.__wTurtle.forward(self.__maxX - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxY - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxX - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxY - 1)
        self.__wTurtle.left(90)

        # draw the grids inside
        for i in range(self.__maxY - 1):
            self.__wTurtle.forward(self.__maxX - 1)
            self.__wTurtle.backward(self.__maxX - 1)
            self.__wTurtle.left(90)
            self.__wTurtle.forward(1)
            self.__wTurtle.right(90)

        self.__wTurtle.forward(1)
        self.__wTurtle.right(90)

        for i in range(self.__maxX - 2):
            self.__wTurtle.forward(self.__maxY - 1)
            self.__wTurtle.backward(self.__maxY - 1)
            self.__wTurtle.left(90)
            self.__wTurtle.forward(1)
            self.__wTurtle.right(90)

        self.__wScreen.tracer(1)

    def addThing(self, aThing, x, y):
        aThing.setX(x) # from Fish / Bear
        aThing.setY(y)
        # add life-form to grid
        self.__grid[y][x] = aThing
        aThing.setWorld(self)
        # add tp list of life-forms
        self.__thingList.append(aThing)
        aThing.appear()

    def delThing(self, aThing):
        aThing.hide()
        self.__grid[aThing.getY()][aThing.getX()] = None
        self.__thingList.remove(aThing)

    def moveThing(self, oldX, oldY, newX, newY):
        self.__grid[newY][newX] = self.__grid[oldY][oldX]
        self.__grid[oldY][oldX] = None

    def getMaxX(self):
        return self.__maxX

    def getMaxY(self):
        return self.__maxY

    def liveALittle(self):
        if self.__thingList != [ ]:
            aThing = random.randrange(len(self.__thingList))
            randomThing = self.__thingList[aThing] # aThing is a random index
            # would be myFish.liveALitte or myBear.liveALittle
            randomThing.liveALittle()


    def emptyLocation(self, x, y):
        # tell if the current location is empty
        if self.__grid[y][x] == None:
            return True
        else:
            return False

    def lookAtLocation(self, x, y):
        return self.__grid[y][x]

    def freezeWorld(self):
        self.__wScreen.exitonclick()