# smaple module.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 21 Sep 2018
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

# change.py
# A program to calculate the value of some change in dollars
def main():
 print("Change Counter")
 print()
 print("Please enter the count of each coin type.")
 quarters = int(input("Quarters: "))
 dimes = int(input("Dimes: "))
 nickels = int(input("Nickels: "))
 pennies = int(input("Pennies: "))
 total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
 print()
 print("The total value of your change is", total)