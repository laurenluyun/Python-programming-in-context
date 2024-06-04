# -*- coding = utf-8 -*-
# @Time : 5/24/2023 5:24 PM
# @Author : Lauren
# @File : L-system.py
# @Software : PyCharm
import turtle


def drawLS(aTurtle, instructions, angle, distance):
    stateSaver = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            pos = aTurtle.position()
            head = aTurtle.heading()
            stateSaver.append((pos, head))
        elif cmd == ']':
            pos, head = stateSaver.pop()
            aTurtle.up()
            aTurtle.setposition(pos)
            aTurtle.setheading(head)
            aTurtle.down()
        else:
            print('Error', cmd, 'is an unknown command.')

def applyProduction(axiom, rules, n):
    for i in range(n):
    # the outer loop allows us to apply the production rules to the string
    # n times
        newString = ""
        for ch in axiom:
        # the inner loop is a simple accumulator pattern that allows us to
        # construct a new string by applying the production rules one ch at
        # a time when character ch has no production rule, we simply leave the
        # character in place.
            newString += rules.get(ch, ch)
        axiom = newString
    return axiom

def lSystem(axiom, rules, depth, initialPosition, heading, angle, length):
    aTurtle = turtle.Turtle()
    win = turtle.Screen()
    aTurtle.up()
    aTurtle.setposition(initialPosition)
    aTurtle.down()
    aTurtle.setheading(heading)
    newRules = applyProduction(axiom, rules, depth)
    drawLS(aTurtle, newRules, angle, length)
    win.exitonclick()

def main():
    axiom = 'X'
    myRules = {'X': 'F[-X]+X', 'F': 'FF'}
    lSystem(axiom, myRules, 7, (0, -200), 90, 30, 2)

if __name__ == "__main__":
    main()