# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"
NUMBER_OF_GUESSES = 8

# Helper Code
# Load the list of words into the variable wordList
# so that it can be accessed from anywhere in the program


def load_words():
    """
    :returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")

    with open(WORDLIST_FILENAME) as file:
        line = file.read()

    wordList = line.split()
    print("  ", len(wordList), "words loaded.")

    return wordList


def choose_word(wordList):
    """
    :param wordList: list of words (strings)

    :returns: a word from wordlist at random
    """
    return random.choice(wordList)

# end of Helper Code
# -----------------------------------


def is_word_guessed(secretWord, lettersGuessed):
    """
    :param secretWord: string, the word the user is guessing
    :param lettersGuessed: list, what letters have been guessed so far
    :returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True


def get_guessed_word(secretWord, lettersGuessed):
    """
    :param secretWord: string, the word the user is guessing
    :param lettersGuessed: list, what letters have been guessed so far
    :returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    guessed_word = ""

    for letter in secretWord:
        guessed_word += (letter + " ") if letter in lettersGuessed else "_ "

    return guessed_word


def get_available_letters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    available_letters = ""

    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            available_letters += letter

    return available_letters


def print_hangman_game_header(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")


def print_game_result(was_word_guessed, secretWord):
    if was_word_guessed:
        print("Congratulations, you won!")
        return
    print("Sorry, you ran out of guesses. The word was " + secretWord + ".")


def print_line_of_dashes():
    print("-------------")


def hangman(secretWord):
    """
    :param secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    mistakes_made = 0
    lettersGuessed = []

    print_hangman_game_header(secretWord)

    while NUMBER_OF_GUESSES - mistakes_made > 0 and not is_word_guessed(secretWord, lettersGuessed):
        print_line_of_dashes()
        print("You have " + str(NUMBER_OF_GUESSES - mistakes_made) + " guesses left.")
        print("Available letters: " + get_available_letters(lettersGuessed))
        letter_guessed = input("Please guess a letter: ").lower()

        if letter_guessed in lettersGuessed:
            print("Oops! You've already guessed that letter: " + get_guessed_word(secretWord, lettersGuessed))
            continue

        lettersGuessed.append(letter_guessed)

        if letter_guessed in secretWord:
            print("Good guess:", end=" ")
        else:
            print("Oops! That letter is not in my word:", end=" ")
            mistakes_made += 1

        print(get_guessed_word(secretWord, lettersGuessed))

    print_line_of_dashes()
    print_game_result(is_word_guessed(secretWord, lettersGuessed), secretWord)


def main():
    wordList = load_words()
    secretWord = choose_word(wordList).lower()
    hangman(secretWord)


if __name__ == "__main__":
    main()