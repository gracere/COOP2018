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
    line_count, word_count, character_count = 0, 0, 0
    for line in f.readlines():
        for word in (line[:-1].split()):
            word_count += 1
            character_count += len(word.strip(""))
            line_count += 1
            print("The file {0}.txt has {1} lines, {2} words, and {3} characters.".format(file, line_count, word_count,+
            character_count))
            f.close()


main()
