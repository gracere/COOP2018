# U05_Ex15_ExamScores.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 17 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 15
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
# This program gets input from a file and plots the exam scores in a horizontal bar graph using graphics.
#
# Algorithm (pseudocode)
# Get input for the file
# Read the file and open it
# input is exam scores
# The output should be the final window (graphics)


from graphics import *


def main():
    file = input("Type the file name you want to word check: ") # I used a file I called "Practice File" to test this
    f = open(file, "r")
    y = int(f.readline(1))
    win = GraphWin("Exam Graph", 600, y*100)
    y = 75
    i = 1
    lines = 0
    Text(Point(300, 20), "Exam Scores").draw(win)
    for line in f:
        if lines > 0:
            words = line.split()
            z = words
            Text(Point(100, y*i+10), z[0]).draw(win)
            score = int(z[1])
            Rectangle(Point(score*6, y*i-20), Point(170, y*i+50)).draw(win)
            i = i+1
        lines = lines + 1
    win.getMouse()
    win.close()


main()
