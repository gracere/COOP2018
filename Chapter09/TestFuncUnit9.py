# TestFuncUnit9.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date:  Apr 2019
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

import traceback, sys

# from misc.my_sum import *
# from fractions import Fraction
from Chapter09.U09_Ex1_simulateMatch import *

COLOR_BLUE = '\x1b[1;34m'
COLOR_RED  = '\x1b[6;31m'
COLOR_OFF  = '\x1b[0m'


def runTest(testStr, answer):
    """
    DO NOT CHANGE THIS FUNCTION
    Evaluates (runs) testStr (your function in your program, with parameters); records result; tests validity of result
    :param testStr: str -> the call to your function in your program
    :param answer: any type -> the correct answer your function should return
    :return: list -> [testStr, answer, actual result from your function, correctness of your result]
    """
    tb = ''     # traceback info
    try:
        result = eval(testStr)
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        result = 'ERROR: ' + str(e)
        tb = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
    return [testStr, answer, result, (result == answer) if answer != 'null' else 'n/a', tb]


def printResults(results):
    """
    DO NOT CHANGE THIS FUNCTION
    Prints results
    :param results: list -> returned by runTest()
    :return: None
    """
    maxLen = [0, 0, 0, 0, 0]        # max lengths of output fields
    for i in range(len(results)):
        # determine lengths of fields based on data type
        for j in range(len(results[i])):
            thisType = type(results[i][j])
            if thisType == str:
                thisLen = len(results[i][j])
            elif thisType == int or thisType == float:
                thisLen = len(str(results[i][j]))
            elif thisType == bool:
                thisLen = 5
            elif thisType == tuple:
                results[i][j] = str(results[i][j])
                thisLen = len(results[i][j])
            elif thisType == list:
                results[i][j] = str(results[i][j])
                thisLen = len(results[i][j])

            if thisLen > maxLen[j]:
                maxLen[j] = thisLen
    # print(results)        # debug
    # print(maxLen)         # debug

    # add 2 to each element of maxLen
    for i in range(len(maxLen)):
        maxLen[i] += 2

    # print results
    print('\nRESULTS:\n========')
    for result in results:
        print("{0:{4}} --> {1:>{5}} | {2:>{6}} | [ {3} ]".
              format(result[0], result[1], result[2], COLOR_BLUE + "Pass" + COLOR_OFF if result[3] else COLOR_RED + "FAIL" + COLOR_OFF,
                     maxLen[0], maxLen[1], maxLen[2]))

        # if error occured, print traceback
        if result[4]:
            for line in eval(result[4]):
                print('{}    {}{}'.format(COLOR_RED, line, COLOR_OFF), end='')
    print('========')


def testTemplate():
    results = []        # list to hold tests

    # replace   'function(params)' with str version of call to function to test (in quotes);
    #           'expected results (properly typed)' with expected results (doesn't have to be str;
    #               should be correct data type)
    # copy line multiple times to run multiple tests (with different parameters)
    results.append(runTest('function(params)', 'expected results (properly typed)'))
    printResults(results)


def testgameOver():
    results = []  # list to hold tests

    # replace   'function(params)' with str version of call to function to test (in quotes);
    #           'expected results (properly typed)' with expected results (doesn't have to be str;
    #               should be correct data type)
    # copy line multiple times to run multiple tests (with different parameters)
    results.append(runTest('gameOver(0,0)', False))
    results.append(runTest('gameOver(0,15)', True))
    results.append(runTest('gameOver(15,0)', True))
    results.append(runTest('gameOver(7,8)', False))
    results.append(runTest('gameOver(14,15)', True))
    results.append(runTest('gameOver(15,14)', True))
    results.append(runTest('gameOver(14,3)', False))
    results.append(runTest('gameOver(3,14)', False))
    printResults(results)


def testmatchOver():
    results = []  # list to hold tests

    # replace   'function(params)' with str version of call to function to test (in quotes);
    #           'expected results (properly typed)' with expected results (doesn't have to be str;
    #               should be correct data type)
    # copy line multiple times to run multiple tests (with different parameters)
    results.append(runTest('matchOver(0,0,5)', False))
    results.append(runTest('matchOver(1,0,5)', False))
    results.append(runTest('matchOver(2,0,5)', False))
    results.append(runTest('matchOver(3,0,5)', True))
    results.append(runTest('matchOver(0,1,5)', False))
    results.append(runTest('matchOver(0,2,5)', False))
    results.append(runTest('matchOver(0,3,5)', True))
    results.append(runTest('matchOver(1,1,5)', False))
    results.append(runTest('matchOver(2,2,5)', False))
    results.append(runTest('matchOver(2,3,5)', True))
    results.append(runTest('matchOver(3,2,5)', True))
    results.append(runTest('matchOver(3,4,7)', True))
    results.append(runTest('matchOver(3,3,7)', False))
    results.append(runTest('matchOver(3,2,6)', False))
    results.append(runTest('matchOver(3,3,6)', False))
    results.append(runTest('matchOver(3,4,6)', True))
    printResults(results)

def testsimulateOneGame():
    results = []  # list to hold tests

    # replace   'function(params)' with str version of call to function to test (in quotes);
    #           'expected results (properly typed)' with expected results (doesn't have to be str;
    #               should be correct data type)
    # copy line multiple times to run multiple tests (with different parameters)
    results.append(runTest('simulateOneGame(0,0)', False))
    results.append(runTest('simulateOneGame(0,0)', False))
    results.append(runTest('simulateOneGame(0,0)', False))
    results.append(runTest('simulateOneGame(0,0)', False))
    results.append(runTest('simulateOneGame(0,0)', False))
    results.append(runTest('simulateOneGame(0,0)', False))
    results.append(runTest('simulateOneGame(0,0)', False))
    results.append(runTest('simulateOneGame(0,0)', False))
    printResults(results)


if __name__ == '__main__':
    # Replace 'function_to_call' with the name of the function you created above
    # test_my_sum()
    # testSphereArea()
    # testSphereVolume()
    # testMany()
    testgameOver()
    testmatchOver()
    testsimulateOneGame()
