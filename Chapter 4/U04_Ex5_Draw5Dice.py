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
#
from graphics import *


def main():
    win_width = 1024
    win_height = 768
    win = GraphWin("Fun with graphics.py", win_width, win_height)
    gut_wi = win_width * 0.1
    gut_hi = win_height * 0.1
    but_wi = win_width * 0.1
    but_hi = win_height * 0.1
    rect1 = Rectangle(Point(gut_wi, gut_hi),
                      Point(gut_wi + but_wi,
                            gut_hi + but_hi))

    rect2 = Rectangle(Point(win_width - gut_wi, gut_hi),
                      Point(win_width - gut_wi - but_wi,
                            gut_hi + but_hi))

    rect4 = Rectangle(Point(gut_wi,
                            win_height - gut_hi - but_hi),
                      Point(gut_wi + but_wi,
                            win_height - gut_hi))

    rect3 = Rectangle(Point(win_width / 2 - but_wi / 2,
                            win_height / 2 - but_hi / 2),
                      Point(win_width / 2 + but_wi / 2,
                            win_height / 2 + but_hi / 2))

    rect5 = Rectangle(Point(win_width - gut_wi,
                            win_height - gut_hi - but_hi),
                      Point(win_width - gut_wi - but_wi,
                            win_height - gut_hi))
    rect1.draw(win)
    rect2.draw(win)
    rect3.draw(win)
    rect4.draw(win)
    rect5.draw(win)
    win.getMouse()


main()
