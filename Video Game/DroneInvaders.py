# -*- coding = utf-8 -*-
# @Time : 6/2/2023 11:02 PM
# @Author : Lauren
# @File : DroneInvaders.py
# @Software : PyCharm
from BoundedTurtle import *
from LaserCannon import *
from turtle import mainloop

class DroneInvaders:
    def __init__(self, xMin, xMax, yMin, yMax):
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax

    def play(self):
        self.__mainWin = LaserCannon(self.__xMin, self.__xMax, self.__yMin,
                                     self.__yMax).getscreen()
        self.__mainWin.bgcolor('light green')
        self.__mainWin.setworldcoordinates(self.__xMin, self.__yMin,
                                           self.__xMax, self.__yMax)
        self.__mainWin.ontimer(self.addDrone, 1000)
        self.__mainWin.listen()
        mainloop()

    def addDrone(self):
        if len(Drone.getDrones()) < 7:
            Drone(1, self.__xMin, self.__xMax, self.__yMin, self.__yMax)
        self.__mainWin.ontimer(self.addDrone, 1000)


def main():
    game = DroneInvaders(-200, 200, 0, 400)
    game.play()

if __name__ == "__main__":
    main()