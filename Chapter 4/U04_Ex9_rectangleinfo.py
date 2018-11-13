# U04_Ex9_rectangleinfo.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 31 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 9
#    Source: Python Programming
#   Chapter: 4
#
# Program Description
# This program allows the user to click to points using the mouse
# and create a rectangle from those two points. The program will give
# the area (l * w) of the rectangle as well as the perimeter (2(l + w)).
#
# Algorithm (pseudocode)
# Introduce Program
# make graphics window
# Get first click and X and Y values of it
# Get second click and X and Y values of it
# Make Rectangle based off of both click's values
# Rectangle Length = X2 - X1
# Rectangle Width = Y1 - Y2
# Area: Rect length * Rect width
# Perimeter: length + width * 2
# Print both area and perimeter
from graphics import *


def main():
    width, height = 700, 700
    win = GraphWin("Rectangle Information", width, height)
    win.setCoords(-10, -10, 10, 10)
    intro = introduction(0, 2, 12)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    instruction_1 = Text(Point(-5, 8), "Click to place first corner")
    instruction_1.draw(win)
    p1 = win.getMouse()
    instruction_1.undraw()
    x1, y1 = p1.getX(), p1.getY()
    p1.draw(win)
    instruction_2 = Text(Point(-5, 8), "Click to place second corner")
    instruction_2.draw(win)
    p2 = win.getMouse()
    instruction_2.undraw()
    x2, y2 = p2.getX(), p2.getY()
    p2.draw(win)
    Rectangle(p1, p2).draw(win)
    p2.undraw()
    p1.undraw()
    length = abs(x2 - x1)
    width = abs(y2 - y1)
    area = length * width
    perimeter = 2 * (length + width)
    Text(Point(-5, 8), "Area: " + str(round(area, 2)) + "\nPerimeter: " + str(round(perimeter, 2))).draw(win)
    exit(5, -9, 5, win)


def introduction(x, y, size):
    intro = Text(Point(x, y),
                 "This program allows the user to click to points using the mouse and create a rectangle from "
                 "those two points.")
    intro.setSize(size)
    return intro


def exit(x, y, size, window):
    exit_text = Text(Point(x, y), "click anywhere to close/exit")
    exit_text.size = size
    exit_text.draw(window)

    window.getMouse()


main()
