# U05_Ex14_WordCount.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 17 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 14
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
# This program takes a user file name and counts the lines, words, and characters it has.
#
# Algorithm (pseudocode)
# Get input of the file name
# Open the file to a variable
# Create a loop that reads each line
# use program code for the counting
# Detect both upper and lower case


def main():
    file = input("Type the file name you want to word check: ")
    f = open(file, "r")
    low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    cap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
    total = 0
    count = 0
    lines = 0
    for line in f:
        lines = lines+1
        for i in range(26):
            low1 = low[i]
            cap1 = cap[i]
            ch = line.count(low1)
            ch1 = line.count(cap1)
            total = total + ch + ch1
        words = line.split()
        for word in words:
            count = count + 1
    print("There are {2} lines, {0} characters, and {1} words.".format(total, count, lines))


main()
