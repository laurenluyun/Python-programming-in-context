# -*- coding = utf-8 -*-
# @Time : 6/2/2023 9:31 AM
# @Author : Lauren
# @File : EventHandler.py
# @Software : PyCharm
from threading import Thread
import time

class EventHandler(Thread): # inherit from Thread class
    '''
    When a class inherits from the Thread class, it has two
options for specifying which code to run when a new thread is
created. The first option is to provide a run method that
contains the code. The second option is to pass a function to
the constructor of the Thread class. We already have defined
the event handler code in a method called run, so we will use
the first option here.

    '''
    def __init__(self):
        super().__init__()
        self.__queue = [] # holds events
        self.__eventKeeper = {} # dict of event types and callbacks

    def addEvent(self, eventName):
        self.__queue.append(eventName)

    # specify function to call when event occurs
    def registerCallback(self, event, func):
        self.__eventKeeper[event] = func

    def run(self): # start calls this method
        while (True): #endless loop
                if len(self.__queue) > 0:
                    nextEvent = self.__queue.pop(0) # pop out the first
                    # event in the queue
                    callBack = self.__eventKeeper[nextEvent] # run the
                    # respective call back function
                    callBack()
                else:
                    time.sleep(1) # pause for 1 second


