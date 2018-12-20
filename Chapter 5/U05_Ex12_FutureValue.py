# U05_Ex12_FutureValue.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 7 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 12
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
# A program that takes user input for a future investment and calculates over user inputted years what the investment
# will be and formats it into a table for every year.
#
# Algorithm (pseudocode)
# get principal and APR from user
# repeat 10 times:
# calculate new principal (principal = principal * (1 + apr)
# output value of principal
# put the print statement in the loop
# print statement to make a table


def main():
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the number of years: "))
    print("")
    print("{0:10}{1:10}".format("Year", "Value"))
    for i in range(year):
        principal = principal * (1 + apr)
        print("{0:>3}       {1:<20}".format(i+1, principal))


main()
