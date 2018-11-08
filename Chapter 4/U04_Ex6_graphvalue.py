# U04_Ex6_graphvalue.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 31 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 6
#    Source: Python Programming
#   Chapter: 4
#
# Program Description
#
# This program plots the growth of a 10 year investment.
#
# Algorithm (pseudocode)
# import graphics
# add entry boxes and prompts/instructions
# add getMouse to input the values in the entry into the calculation
# draw axis and y-values
# draw initial bar
# end close statement
#
from graphics import *


def main():

    win = GraphWin("Graphical Future Value Chart", 965, 530)
    win.setBackground("white")

    make_rect1(win)

    amount_box_text = Text(Point(790, 100), "What is the value of money being compounded?")
    amount_box_text.draw(win)
    amount_box = Entry(Point(790, 120), 20)
    amount_box.setText("0.0")
    amount_box.draw(win)

    pr_box_text = Text(Point(790, 140), "What is the percentage rate in percent?")
    pr_box_text.draw(win)
    pr_box = Entry(Point(790, 160), 20)
    pr_box.setText("0.0")
    pr_box.draw(win)

    calc_box_text = Text(Point(790, 185), "Click the window to calculate.")
    calc_box_text.draw(win)

    make_rect2(win)

    win.getMouse()

    calc_box_text.undraw()

    amount = float(amount_box.getText())
    pr = float(pr_box.getText())

    intro_text = Text(Point(480, 505), "This program plots the growth of a 10 year investment.")
    intro_text.setSize(20)
    intro_text.setStyle("bold")
    intro_text.draw(win)

    ppr = (int(pr) / 100)

    Text(Point(20, 460), ' 0.0K').draw(win)
    Text(Point(20, 360), ' 2.5K').draw(win)
    Text(Point(20, 260), ' 5.0K').draw(win)
    Text(Point(20, 160), ' 7.5k').draw(win)
    Text(Point(20, 60), '10.0K').draw(win)

    draw_border(win)

    height = amount * 0.04
    bar = Rectangle(Point(50, 460), Point(90, 460-height))
    bar.setFill("green")
    bar.draw(win)

    for year in range(1, 10):
        amount = amount * (1 + ppr)
        xll = year * 50 + 40
        height = amount * 0.04
        bar = Rectangle(Point(xll + 5, 460), Point(xll + 50, 460-height))
        bar.setFill("green")
        bar.draw(win)

    conc_box_text = Text(Point(790, 185), "Click the window to close.")
    conc_box_text.draw(win)

    win.getMouse()
    win.close()


def draw_border(win):
    """
    makes the border lines for the graph
    :param win:
    :return:
    """
    line1 = Line(Point(45, 10), Point(45, 461))
    line2 = Line(Point(44, 461), Point(545, 461))
    line1.setWidth(3)
    line2.setWidth(3)
    line1.draw(win)
    line2.draw(win)


def make_rect1(win):
    """
    Makes a box for styling
    :param win:
    :return:
    """
    rect1 = Rectangle(Point(620, 90), Point(960, 175))
    rect1.setOutline("Black")
    rect1.draw(win)


def make_rect2(win):
    """
    Makes a box for styling
    :param win:
    :return:
    """
    rect2 = Rectangle(Point(620, 90), Point(960, 195))
    rect2.setOutline("Black")
    rect2.draw(win)


main()
