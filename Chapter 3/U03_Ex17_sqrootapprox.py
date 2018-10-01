# U03_Ex17_sqrootapprox.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 17
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# is the apporx of a square root
#
# Algorithm (pseudocode)
#
# find user number
# input into equation
# print out input
#
def main():
    x = int('Enter a perfect square : ')
    guess = 0
    while guess**2 < x:
        guess += 1
    print('Square root of ' + str(x) + ' is ' + str(guess))

main()
