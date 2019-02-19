# U06_Ex1_OldMcdonald.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date: 14 Jan 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 1
#    Source: Python Programming
#   Chapter: 6
#
# Program Description
#
# This program sings old macdonald had a farm with multiple animals and sounds.
#
# Algorithm (pseudocode)
# create a main to store the functions
# build the verses/chorus's
# separate into three functions- (went back and had to add some more)
# create animal and noise foe repeated verses
# create song func w/ the verse funcs
# in main print a description, then the song func


def main():
    print("Let's sing Old MacDonald had a farm.")
    old1()
    old2()
    old3()
    old4()
    old5()


def hadafarm():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")


def onfarm():
    animal = "cow"
    print("And on that farm he had a ", animal, ". Ee-igh, Ee-igh, Oh!")


def onfarm1():
    animal = "dog"
    print("And on that farm he had a ", animal, ". Ee-igh, Ee-igh, Oh!")


def onfarm2():
    animal = "cat"
    print("And on that farm he had a ", animal, ". Ee-igh, Ee-igh, Oh!")


def onfarm3():
    animal = "pig"
    print("And on that farm he had a ", animal, ". Ee-igh, Ee-igh, Oh!")


def onfarm4():
    animal = "chicken"
    print("And on that farm he had a ", animal, ". Ee-igh, Ee-igh, Oh!")


def noiseinsong():
    noise = "moo"
    print("With a ", noise, ", ", noise, "here and a ", noise, ", ", noise, "there.")
    print("Here a ", noise, ", ", "there a ", noise, ", everywhere a ", noise, ", ", noise, ".")


def noiseinsong1():
    noise = "woof"
    print("With a ", noise, ", ", noise, "here and a ", noise, ", ", noise, "there.")
    print("Here a ", noise, ", ", "there a ", noise, ", everywhere a ", noise, ", ", noise, ".")


def noiseinsong2():
    noise = "meow"
    print("With a ", noise, ", ", noise, "here and a ", noise, ", ", noise, "there.")
    print("Here a ", noise, ", ", "there a ", noise, ", everywhere a ", noise, ", ", noise, ".")


def noiseinsong3():
    noise = "oink"
    print("With a ", noise, ", ", noise, "here and a ", noise, ", ", noise, "there.")
    print("Here a ", noise, ", ", "there a ", noise, ", everywhere a ", noise, ", ", noise, ".")


def noiseinsong4():
    noise = "cluck"
    print("With a ", noise, ", ", noise, "here and a ", noise, ", ", noise, "there.")
    print("Here a ", noise, ", ", "there a ", noise, ", everywhere a ", noise, ", ", noise, ".")


def old1():
    hadafarm()
    onfarm()
    noiseinsong()
    hadafarm()


def old2():
    hadafarm()
    onfarm1()
    noiseinsong1()
    hadafarm()


def old3():
    hadafarm()
    onfarm2()
    noiseinsong2()
    hadafarm()


def old4():
    hadafarm()
    onfarm3()
    noiseinsong3()
    hadafarm()


def old5():
    hadafarm()
    onfarm4()
    noiseinsong4()
    hadafarm()
