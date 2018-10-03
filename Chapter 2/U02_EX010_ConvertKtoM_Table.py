# U02_EX010_ConvertKtoM_Table.py.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 31 Aug 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 10
#    Source: Python Programming
#   Chapter: 2
#
# Program Description
#
# Convert Kilometers to Miles
#
# Algorithm (pseudocode)
#
# Print Program introduction
#   Get K from user and assign to kilometers
#   Calculate M using kilometers * .621371 and assign to miles
#   Print both in a table
#
#
#
def main():
 print("This program converts distance from Kilometers to Miles")
 kilometers = eval(input("What is the Kilometer distance? "))
 miles = kilometers * .621371
 print ("Kilometers:", kilometers , "Miles:", miles)


main()
