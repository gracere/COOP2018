# U06_Ex13_toNumbers.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 13
#    Source: Python Programming
#   Chapter: 6
#
# Program Description
#
# This program allows the user to enter numbers into a list where the numbers are strings. The program will return the
# list as numbers instead of strings.
#
# Algorithm (pseudocode)
# print introduction
# get user input of length of list
# set the list to have nothing in it but has the length
# of what the user put in
# start a for loop using the list with i
#     set i equal to user input (as string)
# print output with original list
# use toNumbers function on list
# print output with the new list


def main():
    sampleList = ['1', '2.0', '3', '4', '5', '6', '7', '8', '9', '10']
    listTypes = getTypes(sampleList)
    print('Before List: {0}; Types: {1}'.format(sampleList, listTypes))
    toNumbers(sampleList)
    listTypes = getTypes(sampleList)
    print(' After List: {0}; Types: {1}'.format(sampleList, listTypes))


def toNumbers(numlist):
    for i in range(len(numlist)):
        numlist[i] = float(numlist[i])


def main():
    numlist = int(input("length of list: ")) * [None]
    for i in range(len(numlist)):
        numlist[i] = str(input("Enter a number in entree #{0} of the list: ".format(i + 1)))
    print("For each string in the list {0},".format(numlist,), end=" ")
    toNumbers(numlist)
    print("is numbers: {0}.".format(numlist))


if __name__ == '__main__':
    main()