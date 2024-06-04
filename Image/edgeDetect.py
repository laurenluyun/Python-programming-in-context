# -*- coding = utf-8 -*-
# @Time : 5/11/2023 9:28 PM
# @Author : Lauren
# @File : edgeDetect.py
# @Software : PyCharm

from image import *
import math
from NegativeImage import pixelMapper, greyPixel

def convolve(anImage, pixelRow, pixelCol, kernel):
    kernelColumnBase = pixelCol - 1
    kernelRowBase = pixelRow - 1

    sum = 0
    # 3 * 3
    for row in range(kernelRowBase, kernelRowBase + 3):
        for col in range(kernelColumnBase, kernelColumnBase + 3):
            kColIndex = col - kernelColumnBase
            kRowIndex = row - kernelRowBase

            aPixel = anImage.getPixel(col, row)
            intensity = aPixel.getRed()

            sum = sum + intensity + kernel[kRowIndex][kColIndex]

    return sum

def edgeDetect(theImage):
    grayImage = pixelMapper(theImage, greyPixel)
    newIm = EmptyImage(grayImage.getWidth(), grayImage.getHeight())
    black = Pixel(0, 0, 0)
    white = Pixel(255, 255, 255)
    XMask = [[-1, -2, -2], [0, 0, 0], [1, 2, 2]]
    YMask = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]

    for row in range(1, grayImage.getHeight() -1 ):
        for col in range(1, grayImage.getWidth() -1 ):
            gX = convolve(grayImage, row, col, XMask)
            gY = convolve(grayImage, row, col, YMask)
            g = math.sqrt(gX ** 2 + gY ** 2)

            if g > 175:
                newIm.setPixel(col, row, black)
            else:
                newIm.setPixel(col, row, white)
    return newIm

def DetectImageEdge(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin(width * 2, height, "Detect Edge")
    oldImage.draw(myWin)

    newImage = edgeDetect(oldImage)
    newImage.setPosition(width + 1, 0)
    newImage.draw(myWin)

    myWin.exitonclick()

def main():
    DetectImageEdge("lineImage.gif")

if __name__ == "__main__":
    main()

