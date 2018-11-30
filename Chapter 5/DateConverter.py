# DateConverter.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 29 Nov 2018
#     IDE: PyCharm
#
# Program Description
#
# Converts day month and year numbers into two date formats
#
# Algorithm (pseudocode)
#
# Given By Instructor
#


def main():
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    month = months[month-1]
    date2 = month+" " + str(day) + ", " + str(year)

    print("The date is", date1, "or", date2+".")


main()
