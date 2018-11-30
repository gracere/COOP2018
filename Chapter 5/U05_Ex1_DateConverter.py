# U05_Ex1_DateConverter.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 1
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
# This program will take the day, month, and year and put it into a simplifier and simplify it to month/day/year, then
# it will give you the actual month, day, and year
#
# Algorithm (pseudocode)
# Print program description
# Use a string to get month, day, and year = date
# print a blank line to make the code easier to read
# print month/day/year
# Make a list with every month in order
# Subtract the value by 1 to make the months and what the user input to line up
# Print the date using a string
#


def main():
    print("This program will take your birthday and then it will convert it into a nice form")
    date = input("Enter a date mm/dd/yyyy ")
    month, day, year = date.split("/")
    print("You where born on", month, "/", day, "/", year)
    months = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December")
    month = months[int(month)-1]
    print("The converted date is", month, day, year)


main()
