# U03_Ex03_MolecularWeightOfCarb.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 25 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 3
#    Source: Python Programming
#   Chapter: 3
#
# Program Description
#
# This program computes the pounds of a carb
#
# Algorithm (pseudocode)
# Print program description
# Get Input number of carbon, hydrogen and oxygen atoms from user
# Find total weights of each type of atom, and the weight of them combined together


def main():
    print("This program finds the total molecular weight of a combination of hydrogen, carbon and oxygen atoms.")
    h = eval(input("How many hydrogen atoms? "))
    c = eval(input("Carbon? "))
    o = eval(input("Oxygen? "))
    total = (h * 1.00794) + (c * 12.0107) + (o * 15.9994)
    print("The total molecular weight is:", total, "grams per mole.", o, "Oxygen", h, "Hydrogen, and", c, "Carbon.")


main()
