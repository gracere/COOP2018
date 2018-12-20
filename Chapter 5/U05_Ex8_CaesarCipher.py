# U05_Ex8_CaesarCipher.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 30 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 8
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
# This program takes an message and encodes it through the caesar cipher.
#
# Algorithm (pseudocode)
# List the alphabet, where the code can pull from
# Get the input for the key value
# Get the input for the phrase they want to encode
# Make the phrase lowercase
# translate the letters into numbers
#      adding the key value to the numbers - converting back to letters
# if statement
#   convert the numbers back into letters


def print_intro():
    print("The program uses a Caesar cipher to encrypt or decrypt a phrase without special characters.")
    print("1. Encrypt")
    print("2. Decrypt")


def encrypt(phrase, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    phrase_list = (phrase.lower()).split()
    encrypted_string = ""
    for word in phrase_list:
        for letter in word:
            encrypted_string += alpha[(alpha.find(letter) + key) % 26]
        if word != phrase_list[len(phrase_list) - 1]:
            encrypted_string += " "
    return encrypted_string


def main():
    while True:
        print_intro()
        a = int(input("Enter a number that corresponds with your choice: "))
        if a == 2:
            phrase = input("Enter the phrase to decrypt using the Caesar Cipher Wheel (only letters and spaces): ")
            key = int(input("Enter the key (as an integer) to decrypt the phrase by: "))
            print('The encrypted phrase "{0}" using the key {1} is "{2}"'.format(phrase, key, encrypt(phrase, -key)))
        elif a == 1:
            phrase = input("Enter the phrase to encrypt using the Caesar Cipher Wheel (only letters and spaces): ")
            key = int(input("Enter the key (as an integer) to encrypt the phrase by: "))
            print('The phrase "{0}" encrypted with the key {1} is "{2}"'.format(phrase, key, encrypt(phrase, key)))


main()
