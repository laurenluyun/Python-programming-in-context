# -*- coding = utf-8 -*-
# @Time : 5/8/2023 12:28 PM
# @Author : Lauren
# @File : histogram.py
# @Software : PyCharm
'''
bar chart - the vertical line presents the frequency for
each key using turtle
'''
import turtle

def frequencyChart(aList):
    # get the frequency of each element in the dictionary
    countDict = {}
    for each in aList:
        if each in countDict:
            countDict[each] += 1
        else:
            countDict[each] = 1

    # convert keys and values in lists respectively
    key_list = list(countDict.keys())
    # sort the key list
    key_list.sort()
    # get the minimum and maximum value of the key list
    key_minimum = min(key_list)
    key_maximum = max(key_list)

    frequency_list = list(countDict.values())
    # get the minimum and maximum value of the frequency list
    frequency_minimum = min(frequency_list)
    frequency_maximum = max(frequency_list)

    # set up the turtle and screen
    screen = turtle.Screen()
    chartT = turtle.Turtle()
    screen.setworldcoordinates(-1, -1, key_maximum + 1, frequency_maximum + 1)
    chartT.hideturtle()

    # draw the x-axis
    chartT.up()
    chartT.goto(0, 0)
    chartT.down()
    chartT.goto(key_maximum - 1, 0)
    chartT.up()

    # draw y-axis and the label
    chartT.goto(-1, 0)
    chartT.write("0", font=("Helvetica", 16, "bold"))
    chartT.goto(-1, frequency_maximum)
    chartT.write(str(frequency_maximum), font=("Helvetica", 16, "bold"))

    # write the label for x-axis
    for index in range(len(key_list)):
        chartT.goto(index, -1)
        chartT.write(str(key_list[index]), font=("Helvetica", 16, "bold"))

        # draw the frequency line
        chartT.goto(index, 0)
        chartT.down()
        chartT.goto(index, countDict[key_list[index]])
        chartT.up()

    screen.exitonclick()

def main():
    list = [3, 3, 5, 7, 1, 2, 5, 2, 3, 4, 6, 3, 4, 6, 3, 4, 5, 6, 6]
    frequencyChart(list)

if __name__ == "__main__":
    main()
















