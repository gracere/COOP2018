# U04_Ex8_lineSegmentinfo.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 31 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 8
#    Source: Python Programming
#   Chapter: 4
#
# Program Description
#
# This program prints a line segment and its info(slope)
#
# Algorithm (pseudocode)
# import all the things needed
# intro the program, and how the user is needed
# connect the mouse to program to use
# create a grid to place the line in
# ask them to click on the grid to create a point
#       repeat the same thing but assign that data to the second point
# have a line draw connecting the two dots
# print the slope of the line
# ask them to exit the program with another click
from graphics import *
from math import *


def main():
    width, height = 700, 700
    win = GraphWin("Line Segment Information", width, height)
    win.setCoords(-10, -10, 10, 10)
    intro = introduction(0, 2, 16)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    draw_grid_lines(win)
    draw_grid_labels(win)
    instruction_1 = Text(Point(-5, 8), "Click to place first point")
    instruction_1.draw(win)
    p1 = win.getMouse()
    instruction_1.undraw()
    x1, y1 = p1.getX(), p1.getY()
    p1.draw(win)
    instruction_2 = Text(Point(-5, 8), "Click to place second point")
    instruction_2.draw(win)
    p2 = win.getMouse()
    instruction_2.undraw()
    x2, y2 = p2.getX(), p2.getY()
    p2.draw(win)
    Line(p1, p2).draw(win)
    m = Point((x1 + x2)/2, (y1 + y2)/2)
    m.setOutline("cyan")
    m.draw(win)
    dx = x2 - x1
    dy = y2 - y1
    slope = dy / dx
    length = sqrt(dx ** 2 + dy ** 2)
    Text(Point(-5, 8), "Line length: " + str(round(length, 2)) + "\n   Slope: " + str(round(slope, 2))).draw(win)
    exit(5, -9, 5, win)


def introduction(x, y, size):
    intro = Text(Point(x, y),
                 "This program allows the user to draw a line segment with two clicks. Click anywhere to begin!")
    intro.setSize(size)
    return intro


def exit(x, y, size, window):
    exit_text = Text(Point(x, y), "click anywhere to close/exit")
    exit_text.size = size
    exit_text.draw(window)
    window.getMouse()


def draw_grid_labels(window):
    Text(Point(-.25, 5), "5").draw(window)
    Text(Point(-.25, -5), "-5").draw(window)
    Text(Point(5, -.3), "5").draw(window)
    Text(Point(-5, -.3), "-5").draw(window)
    Text(Point(-.25, -.3), "0").draw(window)


def draw_grid_lines(window):
    y_axis = Line(Point(0, 10), Point(0, -10))
    y_axis.setOutline("blue")
    x_axis = Line(Point(-10, 0), Point(10, 0))
    x_axis.setOutline("blue")
    y_axis.draw(window)
    x_axis.draw(window)


main()
