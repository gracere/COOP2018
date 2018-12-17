# U02_EX08_APRPeriodicCompounding.py.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 17 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 8
#    Source: Python Programming
#   Chapter: 2
#
# Program Description
#
# A program to compute the value of an investment, carried 10 years into the future with periods
#
# Algorithm (pseudocode)
#
# Print program description
# Get principal, APR, and periods per year from user
# Repeat (10 * periods) times:
#   Calculate new principal (principal = principal * (1 + (apr / periods)))
# Output value of principal
#
'''
def main():
    years = 10
    print("This program is to to compute the value of an investment, carried 10 years into the future with periods")
    principal, apr, periods = eval(input(print("What is the principal, APR, (as a decimal), and periods (separated by commas)?")
    for i in range(years * periods):
    principal = principal * (1 + (apr / periods))
    print(principal)

main()

'''
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter for how many years to calculate the future value: "))
    periods = eval(input("Enter the period of time at which the interest is compounded "))

    for i in range(years * periods):
        principal += principal * ((1 + (apr / periods))
        print("The value each successive period is:", principal)


main()
