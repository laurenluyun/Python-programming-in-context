# -*- coding = utf-8 -*-
# @Time : 6/2/2023 11:10 AM
# @Author : Lauren
# @File : Etch01.py
# @Software : PyCharm
'''
The inheritance view of this problem would say that an Etch “IS-A” special
kind of Turtle and, therefore, our Etch class would inherit from Turtle.

The main difference between this program and the previous one is that we do
not explicitly create a reference to a turtle inside the Etch class
'''

from turtle import Turtle, mainloop

class Etch(Turtle):
    def __init__(self):
        super().__init__()
        self.__screen = self.getscreen()
        self.color('blue')
        self.pensize(2)
        self.speed(0)

        self.__distane = 5
        self.__turn = 10

        # notce: the the name of forward, backward, left right should be
        # different from the methods of Turtle
        self.__screen.onkey(self.forward5, "Up")
        self.__screen.onkey(self.backward5, "Down")
        self.__screen.onkey(self.left10, "Left")
        self.__screen.onkey(self.right10, "Right")
        self.__screen.onkey(self.quit, "q")

        self.__screen.listen()
        self.main()

    def forward5(self):
        self.forward(self.__distane)

    def backward5(self):
        self.backward(self.__distane)

    def left10(self):
        self.left(self.__turn)

    def right10(self):
        self.right(self.__turn)

    def quit(self):
        self.screen.bye()

    def main(self):
        '''
        mainloop starts the event loop for the turtle so that the turtle
        can process events. This method call needs to be the last statement in
        a turtle graphics program.
        '''
        mainloop()

def main():
    draw = Etch()

if __name__ == "__main__":
    main()

