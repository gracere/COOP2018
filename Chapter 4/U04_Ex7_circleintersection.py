# U04_Ex7_circleintersection.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 31 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 7
#    Source: Python Programming
#   Chapter: 4
#
# Program Description
#
# This program finds the intersection points of a circle and a line
#
# Algorithm (pseudocode)
# import all the things needed
# create a grid to place the circle and line in
# intro the program, and what needs to be inserted
# get radius from the user to create the circle.
# get the y intercept of the line
# make a while if, statement in case the line they put in does not intersect the circle.
from graphics import *
from math import *


def main():
    width, height = 700, 700
    win = GraphWin("Circle and Line Intersection", width, height)
    win.setCoords(-10, -10, 10, 10)
    intro = introduction(0, 4, 10)
    intro.draw(win)
    circle_text = Text(Point(-7.5, -8), "Circle Radius:")
    circle_entry = Entry(Point(-5.2, -8), 3)
    circle_entry.setText(0.0)
    circle_text.draw(win)
    circle_entry.draw(win)
    line_y_text = Text(Point(5.5, -8), "Line Y-Intercept:")
    line_y_entry = Entry(Point(8, -8), 3)
    line_y_entry.setText(0.0)
    line_y_text.draw(win)
    line_y_entry.draw(win)
    win.getMouse()
    intro.undraw()
    circle_text.undraw()
    circle_entry.undraw()
    line_y_text.undraw()
    line_y_entry.undraw()
    radius = float(circle_entry.getText())
    line_y = float(line_y_entry.getText())
    draw_grid_lines(win)
    draw_grid_labels(win)
    Circle(Point(0, 0), radius).draw(win)
    Line(Point(-10, line_y), Point(10, line_y)).draw(win)
    if abs(line_y) > radius:
        Text(Point(5, -5), "The line does not\n" +
                           "intersect with the circle.").draw(win)
    elif abs(line_y) == radius:
        line_x = 0
        p = Point(line_x, line_y)
        p.setOutline("red")
        p.draw(win)
        Text(Point(line_x - .25, line_y + .5), "(" + str(line_x) + ", " + str(line_y) + ")").draw(win)
    else:
        left_x = -1 * (sqrt((radius ** 2) - (line_y ** 2)))
        right_x = sqrt((radius ** 2) - (line_y ** 2))
        left = Point(left_x, line_y)
        left.setOutline("red")
        left.draw(win)
        right = Point(right_x, line_y)
        right.setOutline("red")
        right.draw(win)
        Text(Point(left_x - .5, line_y + .5), "(" + str(round(left_x, 2)) + ", " + str(line_y) + ")").draw(win)
        Text(Point(right_x + .5, line_y + .5), "(" + str(round(right_x, 2)) + ", " + str(line_y) + ")").draw(win)
    exit(5, -9, 5, win)


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


def introduction(x, y, size):
    intro = Text(Point(x, y), "This program takes the input of the radius of a circle centered at (0,0). To start, "
                              "enter the radius and y intercept below and click anywhere to begin!")
    intro.setSize(size)
    return intro


def exit(x, y, size, window):
    exit_text = Text(Point(x, y), "click anywhere to close/exit")
    exit_text.size = size
    exit_text.draw(window)
    window.getMouse()


main()
