# Tri_Exam.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 14 Nov 2018
#     IDE: PyCharm
#
# Trimester 1 Exam
#
# Program Description
#
# This Program tests if three lengths gathered from the user can or cannot form a triangle. The user will input the
# numbers for the variables of the the three sides of a triangle, and the program will tell them if their lengths do or
# do not make a triangle.
#
# Algorithm (pseudocode)
# Main:
# Import math
# Print introduction
# ask the user to input a number for a stick length(variable a)
# ask the user to input a number for a stick length(variable b)
# ask the user to input a number for a stick length(variable c)
# print either if user's lengths make or do not make a triangle(include the lengths that they gave)
#
# is_Triangle:
# take variables a,b,c from input collected from user
# create an true, false statement,
#       with true being all three lengths can form an triangle
#                   (sum of variable a + variable b is less than or equal to variable c), or
#                   (sum of variable a + variable c is less than or equal to variable b).
# If false then,
#       with true being all three lengths cannot form an triangle
#               (variable a is greater than the sum of variable b + variable c), or
#               (variable b is greater than the sum of variable a + variable c), or
#               (variable c is greater than the sum of variable b + variable a).


def is_Triangle(a, b, c):
    while a + b <= c:
        return True
    if c > a + b:
        return False


def main():
    print("This Program tests if three lengths gathered from the user can or cannot form a triangle. The user will "
          "input the numbers for the variables of the the three sides of a triangle, and the program will tell them if "
          "their lengths do or do not make a triangle.")
    print("Next I wil ask you to input in numbers for each side. Remember that side a and b can be any number, but side"
          "c has to be the larger than a and b. Ex: a = 2 b = 5 c = 7.")
    a = input("Please enter a number for one stick length of the triangle: ")
    b = input("Please enter a number for the second stick length of the triangle: ")
    c = input("Please enter a number for the final stick length of the triangle: ")
    if is_Triangle(a, b, c) is True:
        print("With the lengths that you inputted, you ARE able to create a triangle:", a + b <= c)
    else:
        if is_Triangle(a, b, c) is False:
            print("With the lengths that you inputted, you ARE NOT able to create a triangle:", c > a + b)


if __name__ == '__main__':
    main()
