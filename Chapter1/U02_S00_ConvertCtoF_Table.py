# U02_S00_ConvertCtoF_Table.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: Aug 29 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: Sample 0
#    Source: Python Programming
#   Chapter: 2
#
# Program Description
#   This program converts temperature from Celsius to Fahrenheit.
#
# Algorithm (pseudocode)
#   Print Program introduction
#   Get °C from user and assign to celsius
#   Calculate °F using 9/5 * °C + 32 and assign to Fahrenheit
#   Print °F

def main():
 print("This program converts temperature to Celsius to Fahrenheit")
 celsius = eval(input("What is the Celsius temperature? "))
 fahrenheit = 9/5 * celsius + 32
 print("The temperature is ", fahrenheit, " degrees Fahrenheit.")
 print (fahrenheit , celsius)


main()