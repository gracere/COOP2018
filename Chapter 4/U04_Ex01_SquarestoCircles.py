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

import turtle


def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('blue')
    grace = turtle.Turtle()
    grace.color('black')
    grace.shape('arrow')
    grace.speed(2)

    for i in range(1, 36):
        draw_square(grace)
        grace.right(10)

    window.exitonclick()


draw_art()
