# U03_Ex01_Volume+SurfaceAofSpere.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 1
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# This program computes the surface area and volume of a sphere
#
# Algorithm (pseudocode)
#
# surface area formula
# get input of the radius
#
import math
def main():
    print("This program find the surface area, and volume of spheres.")
    r = input("What is the radius of your sphere?")
    r = int(r)
    surface = 4 * math.pi * r
    print("Surface:", surface)
    volume = (4 / 3) * math.pi * r**3
    print("Volume:", volume)


main()



