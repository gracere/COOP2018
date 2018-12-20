# U05_Ex16_QuizScoreHistogram.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 17 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 16
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
# This program takes a file name and counts the quiz scores, then it displays a graphics of a histogram.
#
# Algorithm (pseudocode)
# Import graphics and create a GraphWin
# Get input file name
# Read the file
# Create a title
# Output numbers 0-10 spanning across the bottom
# count numbers and output a rectangle
from graphics import *


def main():
    file = input("Type the file name you want to word check: ")
    f = open(file, "r")
    win = GraphWin("Quiz Histogram", 1100, 600)
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    Text(Point(550, 20), "Quiz Histogram").draw(win)
    var = 0
    ch = []
    fill = ""
    for i in range(11):
        Text(Point(100*i+50, 550), i).draw(win)
        for line in f:
            num = int(line)
            ch = chr(num+97)
            fill += ch
        letters1 = letters[i]
        count = fill.count(letters1)
        Rectangle(Point(100*i+75, 500-count*30), Point(100*i+25, 500)).draw(win)
    win.getMouse()
    win.close()


main()
