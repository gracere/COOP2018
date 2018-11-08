# U04_Ex11_fiveclickhouse.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 2 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise:
#    Source: Python Programming
#   Chapter:
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
# create graphwin
# set window coordinates for graphing (-10, -10, 10, 10)
# Print introduction and instructions
#
#
import math

from graphics import *


def main():
    win = GraphWin("Five-Click House", 500, 500)
    win.setCoords(0, 0, 10, 10)

    message2 = Text(Point(5, 8.9), "Click one time at the bottom left and once at the\n"
                                   "top right to create the house frame.")
    message2.setSize(10)
    message2.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    x1 = p1.getX()
    y1 = p1.getY()
    p2 = win.getMouse()
    p2.draw(win)
    x2 = p2.getX()
    y2 = p2.getY()

    rect = Rectangle(p1, p2)
    rect.setOutline("black")
    rect.draw(win)

    message3 = Text(Point(x1 - 0.2, y1 - 0.2), "1")
    message3.setSize(10)
    message3.setTextColor("red")
    message3.draw(win)

    message4 = Text(Point(x2 + 0.2, y2 + 0.2), "2")
    message4.setSize(10)
    message4.setTextColor("red")
    message4.draw(win)

    p3 = Point(x1 + 2, y1)
    p4 = Point(x1 + 2, y1 + (0.8 * (y2 - y1)))
    x4 = p4.getX()
    y4 = p4.getY()
    p5 = Point(x1 + (0.2 * (x2 - x1)), y1 + (0.8 * (y2 - y1)))
    x5 = p5.getX()
    y5 = p5.getY()
    p6 = Point(x1 + (0.2 * (x2 - x1)), y1)
    x6 = p6.getX()
    y6 = p6.getY()

    message5 = Text(Point(5, 1.4), "Click once to create the door.")
    message5.setSize(10)
    message5.draw(win)

    win.getMouse()

    door = Polygon(p3, p4, p5, p6)
    door.setOutline("black")
    door.draw(win)

    door_top = Line(Point(x4, y4), Point(x5, y5))
    door_top.draw(win)
    x_mid_coord = float((x5 + x4) / 2)
    y_mid_coord = float((y5 + y4) / 2)
    p7 = Circle(Point(x_mid_coord, y_mid_coord), 0.03125)
    p7.setFill("cyan")
    p7.draw(win)

    message6 = Text(Point(x_mid_coord, y_mid_coord + 0.3), "3")
    message6.setSize(10)
    message6.setTextColor("red")
    message6.draw(win)

    message7 = Text(Point(5, 1.1), "Click once to create the window.")
    message7.setSize(10)
    message7.draw(win)

    p8 = win.getMouse()
    x8 = p8.getX()
    y8 = p8.getY()
    window = Rectangle(Point(x8, y8), (Point(x8 + 0.5 * (x5 - x4), y8 + 0.5 * (x5 - x4))))
    wc = window.getCenter()
    wc_x = wc.getX()
    wc_y = wc.getY()
    window.setOutline("black")
    window.draw(win)

    message8 = Text(Point(wc_x, wc_y), "4")
    message8.setSize(10)
    message8.setTextColor("red")
    message8.draw(win)

    message9 = Text(Point(5, 0.8), "Click once to create the roof.")
    message9.setSize(10)
    message9.draw(win)

    win.getMouse()

    p9 = Point(x1, y2)
    p10 = Point((x1 + x2) / 2, y2 + 0.33 * ((x2 + x1) / 2))
    x10 = p10.getX()
    y10 = p10.getY()
    roof_frame = Polygon(p2, p9, p10)
    roof_frame.setOutline("black")
    roof_frame.draw(win)

    message10 = Text(Point(x10, y10 + 0.3), "5")
    message10.setSize(10)
    message10.setTextColor("red")
    message10.draw(win)

    message11 = Text(Point(5, 0.5), "Click once to quit.")
    message11.setSize(10)
    message11.draw(win)

    win.getMouse()
    win.close()


main()
