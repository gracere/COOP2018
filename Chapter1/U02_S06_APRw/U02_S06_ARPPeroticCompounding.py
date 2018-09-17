# U02_S06_ARPPeroticCompounding.py.py
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
#
#
#
#
# Algorithm (pseudocode)
#
#
#
#
#
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    x = eval(input("Enter for how many years to calculate the future value: "))
    compound = eval(input("Enter the period of time at which the interest is compounded "))

    for i in range(x * compound):
        principal = principal * ((1 + apr) / (12 / compound))
        print("The value each successive period is:", principal)