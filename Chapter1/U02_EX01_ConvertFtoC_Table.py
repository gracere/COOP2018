# U02_EX01_ConvertFtoC_Table.py.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 31 Aug 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: Sample 1
#    Source: Python Programming
#   Chapter: 2
#
# Program Description
#   This program converts temperature from Fahrenheit to Celsius.
# Algorithm (pseudocode)
#   Print Program introduction
#   Get °F from user and assign to Fahrenheit
#   Calculate °C using (fahrenheit - 32) / 1.8 and assign to Fahrenheit
#   Print °C
def main():
 print("This program converts temperature to Fahrenheit to Celsius")
 fahrenheit = eval(input("What is the Fahrenheit temperature? "))
 celsius = (fahrenheit - 32) / 1.8
 print("The temperature is ", celsius, " degrees Celsius.")
 print (fahrenheit , celsius)


main()
