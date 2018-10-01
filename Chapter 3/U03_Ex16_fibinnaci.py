# U03_Ex16_fibinnaci.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 1 Oct 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 16
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# finds a number in the fibonacci sequence
#
# Algorithm (pseudocode)
#
# find user number
# input into equation
# print out input
#
def main():
    cache = {1:1, 2:1}
def fib(n, cache):
    if n not in cache:
        cache[n] = fib(n-1, cache) + fib(n-2, cache)
    return cache[n]
assert([fib(i, cache) for i in range(1,10)] == [1,1,2,3,5,8,13,21,34])

main()
