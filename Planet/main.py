

from Sun import *
from planetclass import *
from solarsystem import *

def createSSandAnimate():
    # an instance of SolarSystem is created with a width and height of 2 units
    ss = SolarSystem(2, 2)
    # a sun object created and added to the solar system
    sun = Sun("Sun", 5000, 10, 5800)
    ss.addSun(sun)

    # create and add below planets to the solar system
    mercury = Planet("Mercury", 19.5, 1000, .25, 0, 2, "blue")
    ss.addPlanet(mercury)

    earth = Planet("Earth", 47.5, 5000, .3, 0, 2.0, "green")
    ss.addPlanet(earth)

    mars = Planet("Mars", 50, 9000, .5, 0, 1.63, "red")
    ss.addPlanet(mars)

    jupiter = Planet("Jupiter", 100, 4900, .7, 0, 1, "black")
    ss.addPlanet(jupiter)

    numTimePeriods = 2000
    for aMove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()

def main():
    createSSandAnimate()

if __name__ == "__main__":
    main()