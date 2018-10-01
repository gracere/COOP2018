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
# to find the average of some numbers
#
# Algorithm (pseudocode)
#
# get the input of user of numbers
#
#
def main():
    numbers = [0,1,2,3]
    numbers[0] = input("Please enter a number")
    numbers[1] = input("Please enter a second number")
    numbers[2] = input("Please enter a third number")
    numbers[3] = input("Please enter a fourth number")
    print (numbers)
    print ("Finding the Average")
    Average = int(numbers[0]) + int(numbers[1]) + int(numbers[2]) + int(numbers [3]) / 4
    print (Average)

main()
