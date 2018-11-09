# U04_Ex5_Draw5Dice.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 5
#    Source: Python Programming
#   Chapter: 4
#
# Program Description
#
# This program draws five dice
#
# Algorithm (pseudocode)
# used code from fun with graphics in class
# draw five squares, then place them a little bit off of the x axis
#           in square one, put a circle in middle
# in square two, put two circles
# in square three, put three circles
# in square four, put four circles
# in square five, put five circles
# print them
from graphics import *


def draw_die_face(x, y, window):
    d = Rectangle(Point(x - 1, y + 1), Point(x + 1, y - 1))
    d.setFill("white")
    d.setWidth(1 / 4)
    d.draw(window)


def draw_die_hole(x, y, window):
    c = Circle(Point(x, y), 1 / 8)
    c.setFill("black")
    c.draw(window)


def draw_die1(x, y, window):
    draw_die_face(x, y, window)
    draw_die_hole(x, y, window)


def draw_die2(x, y, window):
    draw_die_face(x, y, window)
    draw_die_hole(x + 1 / 2, y - 1 / 2, window)
    draw_die_hole(x - 1 / 2, y + 1 / 2, window)


def draw_die3(x, y, window):
    draw_die_face(x, y, window)
    draw_die_hole(x, y, window)
    draw_die_hole(x + 1 / 2, y - 1 / 2, window)
    draw_die_hole(x - 1 / 2, y + 1 / 2, window)


def draw_die4(x, y, window):
    draw_die2(x, y, window)
    draw_die_hole(x + 1 / 2, y + 1 / 2, window)
    draw_die_hole(x - 1 / 2, y - 1 / 2, window)


def draw_die5(x, y, window):
    draw_die4(x, y, window)
    draw_die_hole(x, y, window)


def main():
    win = GraphWin("5 Dice", 600, 600)
    win.setCoords(0.0, 0.0, 16.0, 16.0)
    width, height = 16.0, 16.0
    center = Point(width / 2, height / 2)
    intro = Text(center, "Click to start:")
    intro.setSize(19)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    win.setBackground("purple")
    draw_die1(2, height / 2, win)
    draw_die2(5, height / 2, win)
    draw_die3(8, height / 2, win)
    draw_die4(11, height / 2, win)
    draw_die5(14, height / 2, win)
    end = Text(Point(width / 2, height * 7 / 8), "Click to exit")
    end.setSize(20)
    end.draw(win)
    win.getMouse()
    win.close()


main()
