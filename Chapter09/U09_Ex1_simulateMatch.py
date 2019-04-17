# U09_Ex1_simulateMatch.py
#
#  Author: Grace Ritter
#  Course: Coding for OOP
# Section: A2
#    Date:  Apr 2019
#     IDE: PyCharm
#
# Assignment Info
#  Exercise: 1
#    Source: Python Programming
#   Chapter: 9
#
# Program Description
#
# This program simulates N racquetball matches and returns results based off user input.
#
# Algorithm (pseudocode)


from random import random
from math import ceil


def main():
    intro()
    probA, probB, numMatches, matchGames = getInput()
    matchesA, matchesB = simulateNMatches(numMatches, matchGames, probA, probB)
    summary(matchesA, matchesB, numMatches, matchGames, probA, probB)


def intro():
    print('\nThis program simulates N racquetball matches and returns results based off user input')


def getInput():
    m = input('\nHow many matches do you wish to simulate? ')
    g = 2
    while g % 2 == 0:
        g = int(input('How many games per match? (must be odd) '))
    a = input('Probability for player A (greater than 0 and less than 1): ')
    b = input('Probability for player B (greater than 0 and less than 1): ')
    m = int(m)  # ; g = int(g)
    a = float(a); b = float(b)
    return a, b, m, g


def simulateNMatches(matches, games, probA, probB):

    """
    Algorithm
        loop matches times
            simulate one match
            update match counts
    :param matches: int -> number of matches to simulate
    :param games: int -> max games per match
    :param probA: float -> probability for A wins serve
    :param probB: float -> probability for B wins serve
    :return: int -> matchesA; int -> matchesB ... matches won by ech player
    """

    matchesA = 0; matchesB = 0
    for match_count in range(matches):
        gamesA, gamesB = simulateOneMatch(games, probA, probB)
        if gamesA > gamesB:
            matchesA += 1
        else:
            matchesB += 1
    return matchesA, matchesB


def simulateOneMatch(games, probA, probB):

    """
    Algorithm
        while match not over
            simulate one match
            update player game count
            flip server
    :param games: int -> max games per match
    :param probA: float -> probability for A wins serve
    :param probB: float -> probability for B wins serve
    :return: int -> gamesA; int -> gamesB
    """

    gamesA = 0; gamesB = 0
    server = 'A'
    while not matchOver(gamesA, gamesB, games):
        scoreA, scoreB = simulateOneGame(probA, probB, server)
        if scoreA > scoreB:
            gamesA += 1
        else:
            gamesB += 1
        server = 'A' if server == 'B' else 'B'
    return gamesA, gamesB


def simulateOneGame(probA, probB, server):

    """
    Algorithm
        while games not over
            alternate service (A serves odd games; B even)
            use probabilities to determine outcome of serve
            update scores
    :param probA: float -> probability for A wins serve
    :param probB: float -> probability for B wins serve
    :param server: str -> either 'A' or 'B' for server A or server B
    :return: int -> scoreA; int -> scoreB
    """

    scoreA = 0; scoreB = 0
    while not gameOver(scoreA, scoreB):
        if server == 'A':
            if random() < probA:
                scoreA += 1
            else:
                server = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                server = 'A'
    return scoreA, scoreB


def gameOver(A, B):
    return A == 15 or B == 15


def matchOver(A, B, G):
    # g / 2 plus something (or rounded up)
    return A == ceil(G / 2) or B == ceil(G / 2)


def summary(matchesA, matchesB, numMatches, matchGames, probA, probB):
    print('\nRacketball Simulation\n-------------------------------')
    print('\nMatches played: {}'.format(matchGames, numMatches))
    print('\nProbaility player A wins serve: {}'.format(probA))
    print('\nProbaility player B wins serve: {}'.format(probB))
    print('\nMatches won by player A: {}'.format(matchesA))
    print('\nMatches won by player B: {}'.format(matchesB))
    print('\n')


if __name__ == '__main__':
    main()
    # a, b, = simulateOneGame(.9, .3, 'B')
    # print(a, b)
    # a, b, = simulateOneMatch(5, .55, .5)
    # print(a, b)
    # a, b, = simulateNMatches(10, 5, .55, .5)
    # print(a, b)

