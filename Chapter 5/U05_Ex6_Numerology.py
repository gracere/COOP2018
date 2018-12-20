# U05_Ex6_Numerology.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 7 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 6
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
#  This program will take a full name as input, and will return the numeric value of that name.
#
# Algorithm (pseudocode)
# print intro
# get name from user
# count which letters the name has with a loop
# print the end result


def main():
    print('This program will take a full name as input, and will return the numeric value of that name.')
    name = input("Enter your full name: ")
    total = 0
    for word in (name.lower()).split():
        for letter in word:
            total = total + (ord(letter) - 96)
    print('The name, "{0}", has the numeric value of {1}.'.format(name, total))


main()
