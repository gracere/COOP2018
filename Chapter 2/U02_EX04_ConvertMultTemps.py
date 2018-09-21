# U02_EX04_ConvertMultTemps.py.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 5 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 4
#    Source: Python Programming
#   Chapter: 2
#
# Program Description
#
# This program converts multiple temperatures: Fahrenheit to Celsius and vise versa
#
# Algorithm (pseudocode)
#
#   Print Program introduction
#   Get °C from user and assign to celsius, or Get °F from user and assign to Fahrenheit
#   If °C, Calculate °F using 9/5 * °C + 32 and assign to Fahrenheit
#   Print °F
#   elif °F, Calculate °C using (fahrenheit - 32) / 1.8 and assign to Fahrenheit
#   Print °C
#   else ask for correct input
#   print final temperature converted
#   repeat 5 times
#

def main():
 print("This program converts multiple temperatures: Fahrenheit to Celsius and vise versa.")
 temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) Please answer with F or C. : ")
 degree = int(temp[:-1])
 y = temp[-1]

 if   y.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    x = "Fahrenheit"
 elif y.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    x = "Celsius"
 else:
    print("Input proper convention.")
    quit()
 print("The temperature in", x , "is", result , "degrees. (answer may be rounded)")
 for i in range(5):


main()

'''
      if range(5):
          print("The temperature in", x, "is", result, "degrees. (answer may be rounded)")
'''

'''
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
y = temp[-1]

if y.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  x = "Fahrenheit"
elif y.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  x = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", x , "is", result, "degrees. (answer may be rounded)")
'''