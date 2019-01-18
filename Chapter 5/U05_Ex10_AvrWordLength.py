# U05_Ex10_AvrWordLength.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 7 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 10
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
# This program takes a sentence as input and will return the average word length of that sentence.
#
# Algorithm (pseudocode)
# Print intro
# set up all of the letters of the alphabet
# set the variable for words in a sentence, by splitting the length of the sentence
# get sentence from user
# count words with a loop of of the words
# count characters with a loop of the counting letters
# print the end result


def main():
    sentence = input("Enter a sentence: ")
    sentence = sentence.lower()
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    total = 0
    for i in range(26):
        letters1 = letters[i]
        ch = sentence.count(letters1)
        total = total + ch
    words = sentence.split()
    count = 0
    for word in words:
        count = count+1
    print("There are {0} words and {1} characters in the sentence, making the average word length {2} characters."
          .format(count, total, total/count))


main()
