# U06_Ex6_AreaofTriangle.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 23 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 6
#    Source: Python Programming
#   Chapter: 6
#
# Program Description
#
# This program finds the area and the perimeter of a triangle by three points that the user creates.
#
# Algorithm (pseudocode)
# Introduce Program
# get a mouse click
# Make variables X1 and Y1 based off of mouse click
# check for mouse movement before getting mouse click
# get final mouse click
# make a polygon named Tri based off of click1, click2, and click3
# Get lengths of each side Ex. L1 = abs(X1 - X2)
# Find perimeter by adding all sides together
# Define s Ex. s = (L1 + L2 + L3)/2
# Find area Ex. math.sqrt(s * (s-L1) * (s-L2) * (s-L3))
# Print both area and perimeter
import math
from graphics import *


def square(x):
    return x * x


def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist


def area(p1, p2, p3):

    s = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)

    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def main():
    win = GraphWin("Draw a Triangle", 500, 500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("pink")
    triangle.setOutline("purple")
    triangle.draw(win)
    per = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    message.setText("The perimeter is: {0:0.2f}".format(per))
    message.setText2(Point(5, 0.5), "Click to find Area.")
    area = distance(p1,p3)
    message.setText3("The Area is: {0:0.2f}".format(area))
    message.setText4("Click again to end program")
    win.getMouse()
    win.close()


main()
