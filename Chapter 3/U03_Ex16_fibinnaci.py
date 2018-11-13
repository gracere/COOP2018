# U03_Ex16_fibinnaci.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 16
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# finds a number in the fibonacci sequence
#
# Algorithm (pseudocode)
# Print program description
# find user number for n
# input into equation (first number is 1, which is 1+1, and so on)
# print out input


def main():
    print("This is a program for the Fibonacci number for a value you input.")
    n = eval(input("Please insert the value of n:"))
    sum1 = 1
    sum2 = 1
    total = 0
    if n > 2:
        for i in range(n - 3):
            if i % 2 == 0:
                sum1 = sum1 + sum2
            else:
                sum2 = sum2 + sum1
        total = sum1 + sum2
        print("The", n, "spot in the sequence is", total)
    else:
        print("The", n, "spot in the sequence is 1")


main()
