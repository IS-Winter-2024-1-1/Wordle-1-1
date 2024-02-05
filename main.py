import tkinter as tk
from tkinter import Checkbutton, IntVar
import random
from WordleDictionary import FIVE_LETTER_WORDS
from swahiliDictionary import SWAHILI_FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS



def colorblindY():
    global colorblind, wordBank
    colorblind = True
    root.destroy()
    
    wordle(wordBank)

def colorblindN():
    global colorblind, wordBank
    colorblind = False
    root.destroy()

    wordle(wordBank)

def english():
    global wordBank
    wordBank = FIVE_LETTER_WORDS
    p = tk.Toplevel(root)


    # Ask for colorblindness
    label = tk.Label(p, text='\tEnable ColorBlind Mode?   \t\n')

    bYes = tk.Button(p, text="Yes", command=colorblindY)
    bNo = tk.Button(p, text="No", command=colorblindN)
    
    for el in [label, bYes, bNo]:
        el.pack()


def swahili():
    global wordBank
    wordBank = SWAHILI_FIVE_LETTER_WORDS
    root.destroy()
    # Ask for colorblindness


def modal(question):
    if question in questionsAsked:
        return False
    questionsAsked.append(question)

    label = tk.Label(root, text=question)

    bEnglish = tk.Button(root, text="English", command=english)
    bSwahili = tk.Button(root, text="Swahili", command=swahili)
    
    for el in [label, bEnglish, bSwahili]:
        el.pack()

def wordle(wordBank):
    def enter_action(s):
        # Colors
        global colorblind
        if not colorblind:
            correct = "#66BB66"
            close = "#CCBB66"
            wrong = "#999999"

        else:
            correct = "#0C7BDC"
            close = "#FFC20A"
            wrong = "#999999"


         # Check if word was guessed correctly.
        if s.upper() == random_word:
            row = gw.get_current_row()
            for x in range(5):
                gw.set_square_color(row, x, correct)
            gw.show_message('You guessed it!')

        # Check if guessed word is in dictionary.
        elif s.lower() in wordBank:
            row = gw.get_current_row()

            # These variables are here so we can edit them for processing without changing the original words.
            guessedWord = []
            tempRandom = []
            for x in range(5):
                guessedWord.append(s[x])
                tempRandom.append(random_word[x])

            # Check for correct positions.
            for x in range(5):
                if guessedWord[x] == random_word[x]:
                    gw.set_square_color(row, x, correct)

                    # Replace the correct letter in each temp string with symbols so it will be excluded from future
                    # processing.
                    guessedWord[x] = '_'
                    tempRandom[x] = '*'

            # Check for correct letter wrong position.
            for x in range(5):
                if (guessedWord[x] in tempRandom):
                    gw.set_square_color(row, x, close)

                    # Replace the found letter in the random word so it will be excluded from future processing.
                    tempRandom[tempRandom.index(guessedWord[x])] = '*'

                # Color everything else gray.
                elif gw.get_square_color(row, x) == "#FFFFFF":
                    gw.set_square_color(row, x, wrong)



            # Check if it's game over. If not, ove to the next row.
            if row + 1 < N_ROWS:
                gw.show_message('') # Blank out message
                gw.set_current_row(gw.get_current_row() + 1)

            else:
                gw.show_message('Game Over')

        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    random_word = random.choice(wordBank).upper()
    print(random_word)

if __name__ == "__main__":
    root = tk.Tk()
    questionsAsked = []
    modal("What language would you like to play in?\n")
    root.mainloop()
