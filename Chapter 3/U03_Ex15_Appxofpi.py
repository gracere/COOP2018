# U03_Ex15_Appxofpi.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 15
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# This program computes the approximation of pi
#
# Algorithm (pseudocode)
#
# import the math aprrox of pi, from directory
# get the imput of the aproxamation
#
def main():
    print("Input the number that you want to have pi approximation.")
    int("What is the Number?")
def piApprox(x):
    pi = 4.0
    y = 1.0
    est: = 1.0
    while 1 < x:
        y + x = 2
        est = est - (1/y) + 1 / (y+2)
        x = x - 1
        y + x = 2
    return pi*est