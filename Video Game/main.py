# -*- coding = utf-8 -*-
# @Time : 6/2/2023 9:44 AM
# @Author : Lauren
# @File : main.py
# @Software : PyCharm

from EventHandler import *

def myMouse():
    print('oh no, the mouse was clicked.')

def myKey():
    print('A key has been pressed.')

def main():
    '''
     once the start method is called, the three original events are handled as
    before. However, with the run method executing in its own thread,
    we can now type additional Python statements that will
    be executed by the original thread. Also, because two threads
    are running simultaneously, you can see that the output of
    main Python read–eval–print loop overlaps the output from the
    event handler
    '''
    myEvent = EventHandler()
    myEvent.registerCallback('key', myKey)
    myEvent.registerCallback('mouse', myMouse)
    myEvent.addEvent('mouse')
    myEvent.addEvent('key')
    myEvent.addEvent('mouse')
    myEvent.start()

if __name__ == "__main__":
    main()