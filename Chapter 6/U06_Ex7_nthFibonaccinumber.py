# U06_Ex7_nthFibonaccinumber.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 7
#    Source: Python Programming
#   Chapter: 6
#
# Program Description
#
# Determines the nth term in the Fibonacci sequence with n being given by user input using a function to determine the
# term.
#
# Algorithm (pseudocode)
# get term from user input
# use function fibonacci to return number to total
# Check if term is equal to 1, 2, 3, or anything else and say that the 1st, 2nd, 3rd, or xth term in the sequence is
# equal to total.


def fibonacci(term):
    total, a, b = 0, 0, 0
    for i in range(term - 1):
        if a == 0 and b == 0:
            total = 1
            a = b
            b = total
        else:
            total = b + a
            a = b
            b = total
    return total


def main():
    term = int(input("Enter term in the fibonacci sequence to see: "))
    total = fibonacci(term)
    if term == 1:
        print("The 1st term in the fibonacci sequence is", total)
    elif term == 2:
        print("The 2nd term in the fibonacci sequence is", total)
    elif term == 3:
        print("The 3rd term in the fibonacci sequence is", total)
    else:
        print("The", str(term) + "th term in the fibonacci sequence is", total)


if __name__ == '__main__':
    main()
