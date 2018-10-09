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
# import math
# Print program description/ introduction
# Get the input of the radius of the sphere from the user
# surface area formula( 4 * pi * r)
# input the radius into the surface area equation
# Then print the surface area
# Get the input of the radius of the sphere from the user
# volume formula((4/3) * pi * r**3)) (r to the third power)
# Then print the Volume
#
import math
def main():
    print("This program find the surface area, and volume of spheres.")
    r = input("What is the radius of your sphere?")
    r = int(r)
    surface = 4 * math.pi * r
    print("The Surface Area of a sphere with a radius of",  r, "is :" , surface)
    volume = (4 / 3) * math.pi * r**3
    print("The Volume of a sphere with a radius of",  r, "is :" , volume)


main()



