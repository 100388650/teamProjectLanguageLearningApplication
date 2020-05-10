# Functions for the spaced repetition algorithm
from datetime import date
import time

firstDayUseProgram = date.today() # Defines the date of first use for the program
start_minutes = time.perf_counter()
studiedCards = [] # An array of cards already studied

def gen_fib(): # A function for generating the fibonnaci sequence numbers for the daily cards
    a,b = 1,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b


def calculate_next_date(userAnswer, cardCat):
    # Gets the information of the card currently being studied
    # Input card information into the exercise below
    if userAnswer:
        newCardCat = (cardCat + 1)
        return newCardCat
    else:
        newCardCat = (cardCat - 1)
        return newCardCat


def calculate_next_cat(userAnswer, cardCat):
    # Calculates the new category for new cards (Category A, B and C)
    # And starts a timer for the card to be checked again
    # ADD TIMER
    if userAnswer:
        if cardCat == 0.1:
            newCardCat = 0.2
        elif cardCat == 0.2:
            newCardCat = 0.3
        else:
            newCardCat = 1
    else:
        if cardCat == 0.1:
            newCardCat = 0.1
        elif cardCat == 0.2:
            newCardCat = 0.1
        elif cardCat == 0.3:
            newCardCat = 0.2
    return newCardCat


def start_of_study_check(firstDayUsed):
    # Checks the intervals at the start of the study session using the days elapsed
    currentDay = date.today()
    daysElapsed = firstDayUsed - currentDay
    daysElapsedProgram = currentDay - firstDayUseProgram
    g = gen_fib()
    fibs = [next(g) for _ in range(daysElapsed)]
    # Get the number of fibonacci places equal to the days the program has been used for
    if daysElapsedProgram in fibs:
        return True
    else:
        return False


def during_study_check():
    # Checks the intervals during the study session using the minutes elapsed
    minute_check = time.perf_counter()
    minutes_elapsed = start_minutes - minute_check
    return minutes_elapsed