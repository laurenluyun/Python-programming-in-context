# -*- coding = utf-8 -*-
# @Time : 5/11/2023 8:56 PM
# @Author : Lauren
# @File : FlipImage.py
# @Software : PyCharm
from image import *

def verticalFlip(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()
    newIm = EmptyImage(oldW, oldH)
    # actual maximum pixel
    maxP = oldW - 1

    for row in range(oldH):
        for col in range(oldW):
            oldPixel = oldImage.getPixel(maxP - col, row)

            newIm.setPixel(col, row, oldPixel)

    return newIm

def FlipImage(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin(width * 2, height, "Flip Image")
    oldImage.draw(myWin)

    newImage = verticalFlip(oldImage)
    newImage.setPosition(width + 1, 0)
    newImage.draw(myWin)

    myWin.exitonclick()

def main():
    FlipImage("lineImage.gif")

if __name__ == "__main__":
    main()
