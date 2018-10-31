# U04_Ex2_DrawAnArcheryTarget.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 23 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 2
#    Source: Python Programming
#   Chapter: 4
#
# Program Description
#
# This program draws an archery target with a center yellow and with rings of blue, red, black
# and white. each ring has the same width.
#
# Algorithm (pseudocode)
# Import graphics
# Create a GraphWin
# Create 5 concentric circle of increasing radius( yellow, red, blue, black, white)
#           each outer ring has a radius greater than previous, in increments
# Draw circles from outside in

from graphics import *

def main(winSide):
    win = GraphWin("Target", winSide, winSide)
    radius = win.getWidth()/12
    center = Point(win.getWidth()/2, win.getHeight()/2)
    circles = [makeCircle(center, radius*5, "white"),
               makeCircle(center, radius*4, "black"),
               makeCircle(center, radius*3, "blue"),
               makeCircle(center, radius*2, "red"),
               makeCircle(center, radius, "yellow")]
    for circle in circles:
        circle.draw(win)


def makeCircle(c, r, color):
    """

    Creates a circle object centered at c with a radius r and filled with color
    Algortith: 1) step one 2) step two;...
    :param c: Point -> center point of circle
    :param r: int -> radius of circle
    :param color: str -> color for fill
    :return: Circle -> circle object

    """

    circ = Circle(c, r)
    circ.setOutline("black")
    circ.setFill(color)
    return circ

if __name__ == '__main__':
    main(600)
    input("Press <Enter> to close tab.")