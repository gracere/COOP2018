# U03_Ex14_AvgofaSeriusof#'s.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 14
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# to find the average of some numbers from the user
#
# Algorithm (pseudocode)
# Print a program introduction
# get the input of the amount of numbers that will be averaged from the user
# collect the actual numbers that need to be averaged
# inset numbers collected into formula to average them. (n1 + n2 + n3 + n4 ...) / amount of numbers averaged
# Print the average
def main():
    print("This program finds the average of a series of numbers.")
    amount = int("How many numbers do you want to average?: (The limit of number to average is 10.) ")
    while True:
        if amount == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            n1 = input("Please enter a number that you wish to be averaged: ")
            n2 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n3 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n4 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n5 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n6 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n7 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n8 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n9 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n10 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            if input == "zero":
                break
            average = int(n1) + int(n2) + int(n3) + int(n4) + int(n5) + int(n6) + int(n7) + int(n8) + int(n9) + int(n10) / amount
            print ("The average of the numbers that you inputted: ", average)
        if amount is not == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            amount = int("Please enter an amount of numbers that you wish to be averaged less than or equal to 10:")
            n1 = input("Please enter a number that you wish to be averaged: ")
            n2 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n3 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n4 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n5 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n6 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n7 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n8 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n9 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            n10 = input("Please enter another number that you wish to be averaged: (If no other number needs averaged, enter zero)")
            if input == "zero":
                break
            average = int(n1) + int(n2) + int(n3) + int(n4) + int(n5) + int(n6) + int(n7) + int(n8) + int(n9) + int(n10) / amount
            print("The average of the numbers that you inputted: ", average)

main()
