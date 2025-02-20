def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

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
    '''
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {len(secretWord)} letters long.")
    print("-------------")

    lettersGuessed = []
    guessesLeft = 8

    while guessesLeft > 0:
        print(f"You have {guessesLeft} guesses left.")
        print(f"Available letters: {getAvailableLetters(lettersGuessed)}")
        guess = input("Please guess a letter: ").lower()

        if guess in lettersGuessed:
            print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}")
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print(f"Good guess: {getGuessedWord(secretWord, lettersGuessed)}")
        else:
            lettersGuessed.append(guess)
            guessesLeft -= 1
            print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}")

        print("------------")

        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            return

    print(f"Sorry, you ran out of guesses. The word was {secretWord}.")