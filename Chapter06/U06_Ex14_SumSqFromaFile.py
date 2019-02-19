# U06_Ex14_SumSqFromaFile.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 14
#    Source: Python Programming
#   Chapter: 6
#
# Program Description
#
# This program will take a file name as input and return the sum of the squares of numbers read from the file. It uses
# previous programs and functions to do this.
#
# Algorithm (pseudocode)
# import sumlist(), squareEach(), and toNumbers() from past three
# exercises.
# print introduction
# ask for file name as input and save into <name>
# set <file> to open(name, "r")
# set filelines to file.readlines()
# close file
# initialize a variable for storing the original
# characters of the file (this is the only way to do this)
# strip newline character from each line
#     append the current character about to be stripped to the original line list
# save original characters in list
# use toNumbers() on filelines
# use squareEach() on file lines
# print output with original file and the sum of each entree in filelines

from Chapter06.U06_Ex11_squareEach import squareEach
from Chapter06.U06_Ex12_sumList import sumList
from Chapter06.U06_Ex13_toNumbers import toNumbers


def main():
    filename = input('Enter name of file as well as .txt extension on end: ')
    file = open(filename, 'r')
    filelines = file.readlines()
    file.close()
    original_file_lines = []
    for i in filelines:
        original_file_lines.append(i)
        i.strip('')
    toNumbers(filelines)
    squareEach(filelines)
    print('The file with characters {0}, made into numbers,'.format(original_file_lines)+
          '\nsquared, and each entree added is the number: {0}'.format(sumList(filelines)))


if __name__ == '__main__':
    main()
