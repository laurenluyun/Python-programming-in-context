# -*- coding = utf-8 -*-
# @Time : 5/11/2023 8:11 PM
# @Author : Lauren
# @File : DoubleSize.py
# @Software : PyCharm
from image import *

def doubleImage(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW * 2, oldH * 2)

    for row in range(oldH):
        for col in range(oldW):
            oldPixel = oldImage.getPixel(col, row)

            newIm.setPixel(2 * col, 2 * row, oldPixel)
            newIm.setPixel(2 * col + 1, 2 * row, oldPixel)
            newIm.setPixel(2 * col, 2 * row + 1, oldPixel)
            newIm.setPixel(2 * col + 1, 2 * row + 1, oldPixel)
    return newIm

def doubleImage2(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW * 2, oldH * 2)

    for row in range(newIm.getHeight()):
        for col in range(newIm.getWidth()):
            originalCol = col // 2
            originalRow = row // 2
            oldPixel = oldImage.getPixel(originalCol, originalRow)

            newIm.setPixel(col, row, oldPixel)

    return newIm

def makeDoubleImage(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin(width * 2, height * 3, "Double Size")
    oldImage.draw(myWin)

    newImage = doubleImage2(oldImage)
    newImage.setPosition(0, height + 1)
    newImage.draw(myWin)

    myWin.exitonclick()

def main():
    makeDoubleImage("lineImage.gif")

if __name__ == "__main__":
    main()


