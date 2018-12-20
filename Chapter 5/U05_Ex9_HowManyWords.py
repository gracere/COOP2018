# U05_Ex9_HowManyWords.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 7 Dec 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 9
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
# This program allows the user to enter a sentence  and see how many words are in the sentence. This is done using
# string manipulation and for loops.
#
# Algorithm (pseudocode)
# print intro
# gather the sentence from the user
# make everything lowercase
# use the split function to separate words
# loop to count words


def print_intro():
    print("This program allows the user to enter a sentence and see how many words are in the sentence.")


def main():
    while True:
        print_intro()
        sentence = input("Enter the sentence to count all the words in: ")
        print('The sentence "{0}" has {1} word(s) in it.'.format(sentence, len(sentence.split())))


main()
