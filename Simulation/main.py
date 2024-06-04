import random

from World import World
from Fish import Fish
from Bear import Bear
from Plants import Plants

def mainSimulation():
    numberOfBears = 10
    numberOfFish = 10
    numberOfPlants = 10
    worldLifeTime = 2500
    worldWidth = 50
    worldHeight = 25

    myWorld = World(worldWidth, worldHeight)
    myWorld.draw()

    for i in range(numberOfFish):
        newFish = Fish()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
        myWorld.addThing(newFish, x, y)

    for i in range(numberOfBears):
        newBear = Bear()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
        myWorld.addThing(newBear, x, y)

    for i in range(numberOfPlants):
        newPlant = Plants()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
        myWorld.addThing(newPlant, x, y)

    for i in range(worldLifeTime):
        myWorld.liveALittle()
    # puts the world into a wait mode so that we can observe the final
    # state of the simulation. When you click in the simulation window, it will
    # close and the function will exit.
    myWorld.freezeWorld()

def main():
    mainSimulation()

if __name__ == "__main__":
    main()
