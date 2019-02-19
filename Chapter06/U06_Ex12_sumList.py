# U06_Ex12_sumList.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 12
#    Source: Python Programming
#   Chapter: 6
#
# Program Description
#
# This program allows the user to enter values in a list.The program will return the sum of all the numbers in the list.
#
# Algorithm (pseudocode)
# print introduction
# - get user input of length of list
# - set the list to have nothing in it but has the length
# of what the user put in
# - start a for loop using the list with i
#     - set i equal to user input
# - print output with original list and sumList(list)
#


def sumList(numlist):
    acc = 0
    for i in numlist:
        acc += i
    return acc


def main():
    numlist = int(input("length of list: ")) * [None]
    for i in range(len(numlist)):
        numlist[i] = float(input("Enter a number in entree #{0} of the list: ".format(i + 1)))
    print("The sum of all numbers in {0} is {1}.".format(numlist, sumList(numlist)))


if __name__ == '__main__':
    main()