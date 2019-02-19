# U06_Ex11_squareEach.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 11
#    Source: Python Programming
#   Chapter: 6
#
# Program Description
#
# This program will allow the user to create a list, and the program will use a function to square each term and return
# them to the the user.
#
# Algorithm (pseudocode)
# print introduction
# get user input of length of list
# set the list to have nothing in it but has the length
# of what the user put in
# start a for loop using the list with i
#     set i equal to user input
# print output with original list
# use squareEach function on list
# print output with the list


def squareEach(numlist):
    for i in range(len(numlist)):
        numlist[i] = round(numlist[i] ** 2, 5)


def main():
    print("This program will allow the user to create a list, and the program will use a function to square each term "
          "and return them to the the user.")
    numlist = int(input("length of list: ")) * [None]
    for i in range(len(numlist)):
        numlist[i] = float(input("Enter a number in entree #{0} of the list: ".format(i + 1)))
    print("For each term in the list {0},".format(numlist,), end=" ")
    squareEach(numlist)
    print("squared is {0}.".format(numlist))


if __name__ == '__main__':
    main()
