# U05_Ex3_GradingScale.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Nov 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 3
#    Source: Python Programming
#   Chapter: 5
#
# Program Description
#
# This program will divide scores into different groups 100-90 = A, 80-89 = B, 70-79 = C
# # 60-69 = D, and <60 = F
#
# Algorithm (pseudocode)
#
# Print what the program is about (use a version of the program description)
# use a variable for an eval input to get what the student got on the exam
# Make a grade String with A,B,C,D,F, make F * 60 + D * 10 + C * 10 + B * 10 + A * 11 to get the grade to record
#       correctly
# Have that variable subtract by one to account that the computer counts zero
# print what the students grade was


def main():
    print("This program will put grades into the A, B, C, D, and F buckets")
    grade = input("What grade did the student get? (Please write the grade with the capital letter.) ")
    grades = ("F" * 50, "D" * 60, "C" * 70, "B" * 80, "A" * 90)
    grade = grades[input(grade) + 1]
    print("The student got an {0}".format(grade))


main()
