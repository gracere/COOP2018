# U04_Ex01_SquaresToCircles.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 17 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 1
#    Source: Python Programming
#   Chapter: 4
#
# Program Description
#
# This program draws squares into circles
#
# Algorithm (pseudocode)
# print program description
# import graphics
# create a graph
# get the parameters of the square
from graphics import *


def main():
    win = GraphWin("Square Draw", 1280, 720)

    intro = Text(Point(600, 300),"This program allows you to place 10 30x30 red squares."
                                 "\ndraw each square by clicking on the window."
                                 "\nTo remove this message left click on the window.")
    intro.setSize(25)
    intro.draw(win)
    win.getMouse()
    intro.undraw()

    p1 = Point(0, 0)
    p2 = Point(p1.getX() - 30, p1.getY() - 30)
    square = Rectangle(p1, p2)
    square.setOutline("red")
    square.setFill("red")
    square.draw(win)

    for i in range(10):
        p = win.getMouse()
        center = square.getCenter()
        dx = p.getX() - center.getX()
        dy = p.getY() - center.getY()
        clone = square.clone()
        clone.move(dx, dy)
        clone.draw(win)

    conc = Text(Point(600, 300), "Click again to quit")
    conc.setSize(25)
    conc.draw(win)
    win.getMouse()
    win.close()


main()
