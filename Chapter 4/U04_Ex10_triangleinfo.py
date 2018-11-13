# U04_Ex10_triangleinfo.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 4 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 10
#    Source: Python Programming
#   Chapter: 4
#
# Program Description
# This program allows the user to click on the screen to draw the vertices of a triangle. The program
# will draw this triangle and output the perimeter and area of the triangle. The perimeter will be calculated by
# adding all the sides together, and the area will be calculated by using Heron's Formula.
#
# Algorithm (pseudocode)
#  Introduce Program
#  get a mouse click
#  Make variables X1 and Y1 based off of mouse click
#  check for mouse movement before getting mouse click
#  get final mouse click
#  make a polygon named Tri based off of click1, click2, and click3
#  Get lengths of each side Ex. L1 = abs(X1 - X2)
#  Find perimeter by adding all sides together
#  Define s Ex. s = (L1 + L2 + L3)/2
#  Find area Ex. math.sqrt(s * (s-L1) * (s-L2) * (s-L3))
#  Print both area and perimeter
from graphics import *
from math import *


def main():
    width, height = 600, 600
    win = GraphWin("Triangle Information", width, height)
    win.setCoords(-10, -10, 10, 10)
    intro = introduction(0, 2, 12)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    instruction_1 = Text(Point(-5, 8), "Click to place first vertex")
    instruction_1.draw(win)
    p1 = win.getMouse()
    instruction_1.undraw()
    x1, y1 = p1.getX(), p1.getY()
    p1.draw(win)
    instruction_2 = Text(Point(-5, 8), "Click to place second vertex")
    instruction_2.draw(win)
    p2 = win.getMouse()
    instruction_2.undraw()
    x2, y2 = p2.getX(), p2.getY()
    p2.draw(win)
    instruction_3 = Text(Point(-5, 8), "Click to place third vertex")
    instruction_3.draw(win)
    p3 = win.getMouse()
    instruction_3.undraw()
    x3, y3 = p3.getX(), p3.getY()
    p3.draw(win)
    Polygon(p1, p2, p3).draw(win)
    p2.undraw()
    p1.undraw()
    p3.undraw()
    length1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    length2 = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    length3 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    perimeter = length1 + length2 + length3
    s = perimeter / 2
    area = sqrt(s * (s - length1) * (s - length2) * (s - length3))
    Text(Point(-5, 8), "Area: " + str(round(area, 2)) + "\nPerimeter: " + str(round(perimeter, 2))).draw(win)
    exit(5, -9, 5, win)


def introduction(x, y, size):
    intro = Text(Point(x, y),
                 "This program allows the user to click on the screen to draw the vertices of a triangle.")
    intro.setSize(size)
    return intro


def exit(x, y, size, window):
    exit_text = Text(Point(x, y), "click anywhere to close/exit")
    exit_text.size = size
    exit_text.draw(window)
    window.getMouse()


main()
