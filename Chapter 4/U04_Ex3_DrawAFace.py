# U04_Ex3_DrawAFace.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 23 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 3
#    Source: Python Programming
#   Chapter: 4
#
# Program Description
#
# This program draws a face
#
# Algorithm (pseudocode)
# import graphics
# Draw a circle for head
# draw eyes
# draw nose
# draw mouth
from graphics import *
from utility.U04_Ex2_DrawAnArcheryTarget import makeCircle


def main():
    win = GraphWin("Face", 800, 800)
    drawHead(win)
    drawEyes(win)
    drawNose(win)
    drawMouth()
    input("Press RETURN to exit.")
    win.close()


def drawHead(win):
    makeCircle(Point(400, 400), 350, "yellow").draw(win)

def drawEyes(win):
    """
    make right eye
    clone right eye
    move clone to left
    : return:
    """
    rightEye = makeCircle(Point(250, 267), 20, "black")
    leftEye = rightEye.clone()
    leftEye.move(300, 0)
    leftEye.draw(win)
    rightEye.draw(win)


def drawNose(win):
    nose = Circle(center, size * 3)
    nose.setOutline('yellow')
    nose.setFill('yellow')
    nose.draw(win)


def drawMouth():
    makeCircle(Point())


main()
