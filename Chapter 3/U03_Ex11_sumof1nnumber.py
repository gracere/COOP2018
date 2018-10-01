# U03_Ex11_sumof1nnumber.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise:
#    Source: Python Programming
#   Chapter:
#
# Program Description
#
# find sum of a number
#
# Algorithm (pseudocode)
#
# find user number
# input into equation
# print out input
#
def main():
    n=int(input("Enter a number: "))
    sum1 = 0
    while(n > 0):
        sum1=sum1+n
        n=n-1
    print("The sum of first n natural numbers is:",sum1)

main()
