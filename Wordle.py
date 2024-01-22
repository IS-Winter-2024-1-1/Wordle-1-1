# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        if s.upper() == random_word:
            row = gw.get_current_row()
            for x in range(5):
                gw.set_square_color(row, x, "#66BB66")
            gw.show_message('You guessed it!')


        elif s.lower() in FIVE_LETTER_WORDS:
            row = gw.get_current_row()

            # These variables are here so we can edit them for processing without changing the original words.
            guessedWord = []
            tempRandom = []
            for x in range(5):
                guessedWord.append(s[x])
                tempRandom.append(random_word[x])


            for x in range(5):
                if guessedWord[x] == random_word[x]:
                    gw.set_square_color(row, x, "#66BB66")

                    # Replacing the correct letter in each temp string with symbols so it will be excluded from future
                    # processing.
                    guessedWord[x] = '_'
                    tempRandom[x] = '*'


            for x in range(5):
                if (guessedWord[x] in tempRandom):
                    gw.set_square_color(row, x, "#CCBB66")

                    # Replacing the found letter in the random word so it will be excluded from future processing
                    tempRandom[tempRandom.index(guessedWord[x])] = '*'

                elif gw.get_square_color(row, x) == "#FFFFFF":
                    print(gw.get_square_color(row, x))
                    gw.set_square_color(row, x, "#999999")




            if row + 1 < N_ROWS:
                gw.show_message('') # Blank out message

                gw.set_current_row(gw.get_current_row() + 1)
            else:
                gw.show_message('Game Over')

        else:
            gw.show_message("Not in word list")




    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    random_word = random.choice(FIVE_LETTER_WORDS).upper()

    print(random_word)


    # For milestone 1. Commented out for future purposes.
    '''

    # print(f"Random Word: {random_word}")
    for column, letter in enumerate(random_word):
        # print(f"Setting letter '{letter}' in row 0, column {column}")
        if column < N_COLS:
            gw.set_square_letter(0, column, letter)
    '''

# Startup code

if __name__ == "__main__":
    wordle()
