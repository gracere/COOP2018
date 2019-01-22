# U06_Ex3_AreaVolumeSpace.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 18 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 3
#    Source: Python Programming
#   Chapter: 6
#
# Program Description
#
# This program creates two new functions: sphere_area, and sphere_volume, which calculate the area, and volume of a
# sphere with a given radius from the user.
#
# Algorithm (pseudocode)
# create two definitions for the functions
#       sphere_area, and sphere_volume
# (Sphere_Area) Collect radius from user
#       area of a sphere = 4 times pi times radius squared
#           Calculate and print
# (Sphere_Volume) Collect radius from user
#       volume of a sphere = 4 dived by 3 times pi times radius cubed
#           Calculate and print
# Create a main function
#       put new functions in and end program
from math import pi


def main():
    sphere_area()
    sphere_volume()


def sphere_area():
    radius = float(input("What is the radius of sphere? "))
    s_area = 4 * pi * radius ** 2
    print("The surface area of the sphere is: ", s_area)


def sphere_volume():
    radius = float(input("What is the radius of sphere? "))
    volume = (4 / 3) * (pi * radius ** 3)
    print("The volume of the sphere is: ", volume)
