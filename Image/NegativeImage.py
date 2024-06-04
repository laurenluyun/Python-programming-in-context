# -*- coding = utf-8 -*-
# @Time : 5/11/2023 5:59 PM
# @Author : Lauren
# @File : NegativeImage.py
# @Software : PyCharm
from image import *
def negativePixel(oldPixel):
    newRed = 255 - oldPixel.getRed()
    newGreen = 255 - oldPixel.getGreen()
    newBlue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newRed, newGreen, newBlue)
    return newPixel

def greyPixel(oldPixel):
    intensitySum = oldPixel.getRed() + oldPixel.getGreen() + oldPixel.getBlue()
    aveRGB = intensitySum // 3
    newPixel = Pixel(aveRGB, aveRGB, aveRGB)
    return newPixel

# improve the whole program by adding another helper function to
# transform the image
def pixelMapper(fileImage, rgbFunction):
    width = fileImage.getWidth()
    height = fileImage.getHeight()
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = fileImage.getPixel(col, row)
            newPixel = rgbFunction(oldPixel)
            newIm.setPixel(col, row, newPixel)
    return newIm


def generalTransform(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin(width * 2, height, "General Transform")
    oldImage.draw(myImageWindow)

    newIm = pixelMapper(oldImage, negativePixel)

    newIm.set_postion(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitonclick()

def main():
    generalTransform("lineImage.gif")

if __name__ == "__main__":
    main()
