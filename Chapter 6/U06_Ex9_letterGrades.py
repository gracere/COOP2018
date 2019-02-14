# U06_Ex9_letterGrades.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 9
#    Source: Python Programming
#   Chapter: 6
#
# Program Description
#
# This program takes an exam score as integer input and will return the letter grade of that score on the scale that
# 90-100 is an A, 80-89 is a B, 70-79 is a C, 60-69 is a D, and below 60 is an F.
#
# Algorithm (pseudocode)
# print introduction
# get <raw_score> as input
# divide <raw_score> by 10 and save it into <exam_score> as an integer
# print output in a complete sentence listing the input(s) and stating what was returned and what it means
# (using string format)


def grade(score):
    letter_grades = "f" * 5 + "DCBAA"
    letter_score = letter_grades[score - 1]
    return letter_score


def main():
    print("This program takes an exam score as integer input and will return the letter grade of that score on the "
          "scale that 90-100 is an A, 80-89 is a B, 70-79 is a C, 60-69 is a D, and below 60 is an F. This program uses"
          " a grade function.")
    raw_score = int(input("Enter exam score as integer input: "))
    exam_score = raw_score // 10
    print("The exam score {0} is the letter grade {1}".format(raw_score, grade(exam_score)))


if __name__ == '__main__':
    main()
