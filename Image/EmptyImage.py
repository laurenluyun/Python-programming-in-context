# -*- coding = utf-8 -*-
# @Time : 5/11/2023 5:10 PM
# @Author : Lauren
# @File : EmptyImage.py
# @Software : PyCharm
from image import *
def main():
    # 300 pixels high and 300 pixels wide
    myImWin = ImageWin(300, 300, "Empty Image")
    # create an empty image with white background
    lineImage = EmptyImage(300, 300)
    # set up the black pixel
    blackPixel = Pixel(0, 0, 0)
    # draw the black line
    for i in range(lineImage.getHeight()):
        lineImage.setPixel(i, i, blackPixel)
    lineImage.draw(myImWin)
    # save the pic
    lineImage.save("lineImage.gif")
    # close the window on clicking the canvas
    myImWin.exitonclick()

if __name__ == "__main__":
    main()
