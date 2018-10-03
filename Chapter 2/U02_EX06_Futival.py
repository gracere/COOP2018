# U02_EX06_Futival.py.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 17 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 6
#    Source: Python Programming
#   Chapter: 2
#
# Program Description
#
# A program to compute the value of an investment, carried 10 years into the future
#
# Algorithm (pseudocode)
#
# Print program description
# Get principal and APR from user
# Repeat 10 times:
#    Calculate new principal (principal = principal * (1 + apr)
#  Output value of principal
#
def main():
    print("This program calculates the future value")
    print("of a 10 year investment.")

    principal = float(input("Enter the initial principal: "))
    str = float(input("Enter the annualized interest rate: "))

    for i in range(10):
        principal = principal * (1 + str)

    print("The value in 10 years is:", principal)


main()
