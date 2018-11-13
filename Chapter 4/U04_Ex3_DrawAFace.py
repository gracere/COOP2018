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
    drawMouth(win)
    input("press RETURN to exit.")
    win.close()


def drawHead(win):
    makeCircle(Point(400, 400), 350, "yellow").draw(win)


def drawEyes(win):
    makeCircle(Point(550, 200), 50, "black").draw(win)
    makeCircle(Point(250, 200), 50, "black").draw(win)


def drawNose(win):
    makeCircle(Point(410, 320), 30, "orange").draw(win)


def drawMouth(win):
    makeCircle(Point(400, 500), 120, "pink").draw(win)


main()
