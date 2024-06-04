# -*- coding = utf-8 -*-
# @Time : 6/2/2023 10:54 AM
# @Author : Lauren
# @File : Etch.py
# @Software : PyCharm

import turtle

class Etch:
    def __init__(self):
        self.__myTurtle = turtle.Turtle()
        self.__myScreen = turtle.Screen()
        self.__myTurtle.color('blue')
        self.__myTurtle.pensize(2)
        self.__myTurtle.speed(0)

        self.__distane = 5
        self.__turn = 10

        self.__myScreen.onkey(self.forward, "Up")
        self.__myScreen.onkey(self.backward, "Down")
        self.__myScreen.onkey(self.left, "Left")
        self.__myScreen.onkey(self.right, "Right")
        self.__myScreen.onkey(self.quit, "q")

        self.__myScreen.listen()

    def forward(self):
        self.__myTurtle.forward(self.__distane)

    def backward(self):
        self.__myTurtle.backward(self.__distane)

    def left(self):
        self.__myTurtle.left(self.__turn)

    def right(self):
        self.__myTurtle.right(self.__turn)

    def quit(self):
        self.__myScreen.bye()

    def main(self):
        '''
        mainloop starts the event loop for the turtle so that the turtle
        can process events. This method call needs to be the last statement in
        a turtle graphics program.
        '''
        turtle.mainloop()

def main():
    draw = Etch()
    turtle.exitonclick()

if __name__ == "__main__":
    main()


