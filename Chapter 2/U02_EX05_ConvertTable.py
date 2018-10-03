# U02_EX05_ConvertTable.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 19 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 5
#    Source: Python Programming
#   Chapter: 2
#
# Program Description
#   This program converts temperature from Celsius to Fahrenheit and puts it into a table.
#
# Algorithm (pseudocode)
#   Print Program introduction
#   Print °F and °C in a table

def main():
 print("This program converts temperature to Celsius to Fahrenheit and puts it into a table.")
 for i in range(101):
     if i % 10 == 0:
         celsius = i
         fahrenheit = 9 / 5 * celsius + 32;
         print ("Fahrenheit:", fahrenheit ,"| Celsius:", celsius)


main()
