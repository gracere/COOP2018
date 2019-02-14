# U06_Ex4_Cubes.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 23 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 4
#    Source: Python Programming
#   Chapter: 6
#
# Program Description
#
# This program gathers a number from the user and prints the sum of the first n natural numbers, and the sum of the
# cubes.
#
# Algorithm (pseudocode)
# create a main
# create function sets for sumN, and sumNCubes
# get the natural number from the user
# sumN formula is n = n - 1
# def other two functions


def sumN(n):
    nsum = 0
    for i in range(n):
        nsum += (i + 1)
    return nsum


def sumNcubes(n):
    cube_sum = 0
    for i in range(n):
        cube_sum += (i + 1) ** 3
    return cube_sum


def main():
    print("This program uses two functions to return the sum of the first n natural numbers and sum of the cubes of the"
          "first n natural numbers with n being user input")
    n = int(input("Enter how many of the first natural numbers to sum: "))
    print("The first {0} natural numbers have".format(n) +
          " a sum of {0} and their cubes sum to {1}.".format(sumN(n), sumNcubes(n)))


if __name__ == '__main__':
    main()
