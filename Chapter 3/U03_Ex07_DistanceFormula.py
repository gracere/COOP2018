# U03_Ex07_DistanceFormula.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 7
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# This program calculates the distance formula
#
# Algorithm (pseudocode)
#
# (x1 + x2 / 2) + (y1 + y2 / 2))
# insert distance formula into code, input list
#
import math # math needed for sqrt

# distance function
def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# run through input and reorder in [(x, y), (x,y) ...] format
input = ["9.5 7.5", "10.2 19.1", "9.7 10.2"] # original input list (entered by spacing the two points)
points = [map(float, point.split()) for point in input] # final list