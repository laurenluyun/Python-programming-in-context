# -*- coding = utf-8 -*-
# @Time : 5/24/2023 3:30 PM
# @Author : Lauren
# @File : Recursion.py
# @Software : PyCharm

# draw the tree
import turtle
t = turtle.Turtle()

def countList(aList):
    if aList == []:
        return 0
    else:
        return 1 + countList(aList[1:])

def tree(t, trunkLength):
    if trunkLength < 5:
        return
    else:
        t.forward(trunkLength)
        t.right(30)
        tree(t, trunkLength - 15)
        t.left(60)
        tree(t, trunkLength - 15)
        t.right(30)
        t.backward(trunkLength)

def main():
    t.up()
    t.goto(0, -225)
    t.down()
    t.color("green", "green")
    t.left(90)
    tree(t, 115)
    t.hideturtle()

if __name__ == "__main__":
    main()