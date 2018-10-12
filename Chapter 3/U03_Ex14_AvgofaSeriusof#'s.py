# U03_Ex14_AvgOfASeries#'s.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 14
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# to find the average of some numbers from the user
#
# Algorithm (pseudocode)
# Print a program introduction
# get the input of the amount of numbers that will be averaged from the user
# collect the actual numbers that need to be averaged
# inset numbers collected into formula to average them. (n1 + n2 + n3 + n4 ...) / amount of numbers averaged
# Print the average


def main():
    print("This program finds the average of a series of numbers.")
    amount = int(input("How many numbers do you want to average?: "))
    total = 0
    for i in range(amount):
        num = int(input("Please enter another number that you wish to be averaged:"))
        total = num + total
    average = total / amount
    print("The average of the numbers that you inputted: ", average)


main()
