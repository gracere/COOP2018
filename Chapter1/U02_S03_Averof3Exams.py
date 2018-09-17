# U02_S03_Averof3Exams.py.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 5 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 3
#    Source: Python Programming
#   Chapter: 2
#
# Program Description
# to get the average of three exams
# Algorithm (pseudocode)
#
# get the number of exams
# do a loop to get grades
# do an equation to get sum
# print sum
#
n=int(input("Enter the number of grades to be averaged: "))
a=[]
for i in range(0,n):
        grade=int(input("Enter Grade: "))
        a.append(grade)
avg=sum(a)/n
print("Average of grades in the list",round(avg,2))
