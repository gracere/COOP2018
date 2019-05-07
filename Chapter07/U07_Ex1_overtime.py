# U07_Ex1_overtime.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 27 April 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 1
#    Source: Python Programming
#   Chapter: 7
#
# Program Description
#
# This program calculates if the employee receives the overtime pay.
#
# Algorithm (pseudocode)
# ask user for both pay in an hour and how much hours worked
# use an if statement


def main():
    hours = int("Enter hours that you worked this week: ")
    wage = int("What do you get paid an hour? ")
    income = wage * hours
    if hours < 40:
        print("You will not receive overtime pay. Your income is ", income)
    else:
        print("You will receive overtime pay. Your income is ", income)


if __name__ == '__main__':
    main()
