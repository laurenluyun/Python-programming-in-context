# -*- coding = utf-8 -*-
# @Time : 6/2/2023 11:52 AM
# @Author : Lauren
# @File : TurtlePlace.py
# @Software : PyCharm

from turtle import Turtle, mainloop
import random

class TurtlePlace:
    def __init__(self, maxTurtles, hWall = 200, vWall = 200):
        self.__bigT = Turtle()
        self.__bigTscreen = self.__bigT.getscreen()
        self.__bigT.color('blue')
        self.__turtleList = []
        # execute placeTurtle method when clicks
        self.__bigTscreen.onclick(self.placeTurtle)
        self.__bigT.hideturtle()
        self.__numTurtles = 0 # keep track of how many turtles created
        self.__maxTurtles = maxTurtles
        self.__hWall = hWall
        self.__vWall = vWall
        # execute the drawField method
        self.drawField()
        mainloop()

    def placeTurtle(self, x, y):
        '''
        creates a new turtle at position (x, y)
        '''
        newT = AnimatedTurtle(self.__hWall, self.__vWall)
        newT.hideturtle()
        newTscreen = newT.getscreen()
        newTscreen.tracer(1)

        newT.up()
        newT.goto(x, y)
        newT.shape('turtle') # gives turtle a fancy shape
        newT.showturtle() # gives the turtle a random heading
        newT.setheading(random.randint(1, 359))
        newTscreen.tracer(1)

        self.__numTurtles = self.__numTurtles + 1 # count turtle
        self.__turtleList.append(newT)

        if self.__numTurtles >= self.__maxTurtles:
            # if the limit on turtles is reached, pass None to the onclick
            # function, which will cancel the callback mechanism -
            # placeTurtle will no longer be called when the mouse is clicked
            self.__bigTscreen.onclick(None) # remove event handler
            # newTscreen.bye()

    def drawField(self):
        '''
        draws a rectangle for the turtles to live in
        '''
        self.__bigTscreen.tracer(0)
        self.__bigT.up()
        self.__bigT.goto(-(self.__hWall), -(self.__vWall))
        self.__bigT.down()
        for i in range(4):
            self.__bigT.forward(2 * self.__hWall)
            self.__bigT.left(90)
        self.__bigTscreen.tracer(1)

class AnimatedTurtle(Turtle):
    '''
    it automatically begins to wander around the box, bouncing off the
    walls and the other turtles.
    '''

    # static variable - a variable that is shared by all instances of a
    # class and is available to all the methods in the class.
    __allTurtles = []

    def __init__(self, hWall, vWall):
        super().__init__()
        self.__screen = self.getscreen()
        self.__xMin = -vWall + 10
        self.__xMax = vWall - 10
        self.__yMin = -hWall + 10
        self.__yMax = hWall - 10
        # calls the ontimer method to set up a callback for the moveOneStep
        # method, causing the method to execute after 100 milliseconds
        self.__screen.ontimer(self.__moveOneStep, 100)
        # use the static variable
        AnimatedTurtle.__allTurtles.append(self)

    def __moveOneStep(self):
        # calls computeNewHeading to check whether the turtle has run into
        # one of the boundary walls
        self.__computeNewHeading()
        self.forward(5)
        self.__checkCollisions()
        # a timer callbck is good for only one interval; it does not repeat.
        # Therefore, the last thing we do in the _ _moveOneStep method is
        # reset the timer callback to execute again after another 100 milliseconds.
        self.__screen.ontimer(self.__moveOneStep, 100)

    def __computeNewHeading(self):
        xPos, yPos = self.position()
        oldHead = self.heading()
        # set the new head as the old head to proceed
        newHead = oldHead

        # if the turtle is out of the range, update the new head to turn
        # around, and then set the newhead as the current head
        if xPos > self.__xMax or xPos < self.__xMin:
            newHead = 180 - oldHead
        if yPos > self.__yMax or yPos < self.__yMin:
            newHead = 360 - oldHead
        if newHead != oldHead:
            self.setheading(newHead)

    def __checkCollisions(self):
        # the beauty of the static variable approach is that it keeps the
        # accounting of all the animated turtles inside the AnimatedTurtle
        # class.
        for otherT in AnimatedTurtle.__allTurtles:
            # we do not compute the distance between the same turtle using
            # two different references
            if self != otherT:
                # use the distance method provided by the turtle modules,
                # this method calculates the distance between the center
                # points of two turtles
                if self.distance(otherT) < 20: # if close, swap headings,
                    # to mimic the collision process. If the turtles are
                    # too close, then they bounce off each other by
                    # exchanging their headings
                    tempHeading = self.heading()
                    self.setheading(otherT.heading())
                    otherT.setheading(tempHeading)
                    # and then move away
                    while self.distance(otherT) < 20:
                        self.forward(1)
                        otherT.forward(1)

# def main():
#     myTurtleSpace = TurtlePlace(5, 200, 200)
#
# if __name__ == "__main__":
#     main()