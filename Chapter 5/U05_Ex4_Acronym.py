# U05_Ex4_Acronym.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 4
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
# A program that inputs a phrase and outputs its acronym.
#
#
# Algorithm (pseudocode)
# Print Program Description
# Print what Information I will need from the user
# Gather information from user
# split them from the string
# And Get the first Letter from each word, and put them together
# print letters, and a description of the information given.
import string


def main():
    print("This program generates acronyms.")
    print("I will ask you to Enter a phrase, and I will give you its acronym.")
    phrase = int("Enter a phrase : ")
    words = string.split(phrase)
    acronym = ""
    for w in words:
        acronym = acronym + w[0]
    acronym = string.upper(acronym)
    print("The acronym is : ", acronym)


main()
