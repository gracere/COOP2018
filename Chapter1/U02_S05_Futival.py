# U02_S05_Futival.py.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 17 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise:
#    Source: Python Programming
#   Chapter:
#
# Program Description
# A program to compute the value of an investment, carried 10 years into the future
# Algorithm (pseudocode)
#
#
def main():
    print("This program calculates the future value")
    print("of a 10 year investment.")

    principal = input("Enter the initial principal: ")
    str = input("Enter the annualized interest rate: ")

    for i in range(10):
        principal = principal * (1 + str)

    print("The value in 10 years is:", principal)
