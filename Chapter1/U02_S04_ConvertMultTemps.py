# U02_S04_ConvertMultTemps.py.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 5 Sep 2018
#     IDE: PyCharm
#
# Assignment Info
#  Exercise:
#    Source: Python Programming
#   Chapter:
#
# Program Description
#
#
#
#
# Algorithm (pseudocode)
#
#
#
#
#
def main():
 print("This program converts multiple temperatures: Fahrenheit to Celsius and vise versa.")
 print("What is the unit that your temperature is in?")
 if < eval = "fahrenheit" > :
     < fahrenheit if true >
 elif : [ < fahrenheit = eval(input("What is the temperature?"))
          celsius = (fahrenheit - 32) / 1.8
          print("The temperature is ", celsius, " degrees Celsius.") >]:
 else : < celsius = eval(input("What is the temperature? "))
     fahrenheit = 9/5 * celsius + 32
     print("The temperature is ", fahrenheit, " degrees Fahrenheit.")if not else fahrenheit >
 if range(5):
    print(fahrenheit, celsius)
'''    
 if <condition>:
  <statements if true>
 elif [<condition>]:
  <statements if elif is true>
 else:
  <statements if nothing else was true>
'''
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")


main()
