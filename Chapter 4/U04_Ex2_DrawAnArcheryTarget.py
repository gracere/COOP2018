# U04_Ex2_DrawAnArcheryTarget.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 23 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise:
#    Source: Python Programming
#   Chapter:
#
# Program Description
#
# This program draws an archery target
#
#
# Algorithm (pseudocode)
# import turtle drawing routines
# import the time routines
# define a function to draw a target at a location on the screen.
# draw the largest red circle
# move to the starting location
# create an radius
# set the color
# set the pen width
# create a title for the drawing window
# create a turtle to draw the target with
# set the location of the center of the target
# Create an arrow as a turtle shape
# draw the target
from turtle import *
from time import sleep


def draw_target(turtle, targetx, targety):
    turtle.speed("fast")
    turtle.up()
    turtle.goto(targetx, targety + 50)
    turtle.sety(targety - 150)
    turtle.down()
    turtle.color("red")
    turtle.width(2)
    turtle.fill(1)
    turtle.circle(150)
    turtle.fill(0)
    turtle.up()
    turtle.sety(targety - 100)
    turtle.down()
    turtle.color("blue")
    turtle.fill(1)
    turtle.circle(100)
    turtle.fill(0)
    turtle.up()
    turtle.sety(targety - 50)
    turtle.down()
    turtle.color("green")
    turtle.fill(1)
    turtle.circle(50)
    turtle.fill(0)
    turtle.hideturtle()
    return


def erase_target(turtle, targetx, targety):
    sleep(1)
    turtle.goto(targetx, targety - 150)
    turtle.down()
    turtle.color("white")
    turtle.width(2)
    turtle.fill(1)
    turtle.circle(150)
    turtle.fill(0)


def move_arrow(arrow, ax, ay, targetx, targety):
    arrow.goto(ax, ay)
    arrow.setheading(arrow.towards(targetx, targety))
    arrow.showturtle()
    sleep(1)
    steps = 100
    dx = (targetx - ax) / float(steps)
    dy = (targety - ay) / float(steps)
    for x in range(steps):
        ax = ax + dx
        ay = ay + dy
        arrow.goto(ax, ay)

    return
setup()
title("archery target program")
turtle = Turtle()
targetx = 0
targety = 0
arrow = Turtle()
arrow.hideturtle()
arrow.penup()
register_shape("myarrow", ((-6, -96), (-6, 0), (-18, 0), (0, 18), (18, 0), (6, 0), (6, -96), (-6, -96)))
arrow.shape("myarrow")
draw_target(turtle, targetx, targety)
ax = -200
ay = 0
move_arrow(arrow, ax, ay, targetx, targety)
erase_target(turtle, targetx, targety)
targetx = 100
targety = 100
draw_target(turtle, targetx, targety)
move_arrow(arrow, ax, ay, targetx, targety)
done()