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


def sumN(n):
    sumN = 0
    while n > 0:
        sumN = sumN + n
        n = n - 1
        print("The sum of the first natural number is :{0}".format(sumN))


def sumNCubes(n):
    sumNCubes = 0
    if n == 1:
        return 1
    else:
        while n > 0:
            sumNCubes = sumNCubes + n
            (n ** 3) + sumNCubes(n - 1)
        print("The sum of the cubed first natural number is {0}".format(sumNCubes))


def main():
    n = int(input("Enter a number: "))
    sumN(n)
    sumNCubes(n)


if __name__ == '__main__':
    main()
