# Problem Set 2, hangman.py
# Name: Lydia Yu
# Collaborators: Aditya Mehrotra, Wilson Banks Spearman
# Time spent: 2 hrs

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def check_game_won(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    numMatches = 0
    for letter in secret_word:   #goes through all the letters in secret_word
        for char in letters_guessed:    #goes through each letter in letters_guessed
            if letter == char:  #sees if the letter in letters_guessed matches a letter in secret_word
                numMatches += 1     #adds 1 to the number of matching letters
    if numMatches == len(secret_word):
        return True     #if the number of matches is the same as the number of letters in secret word, then the word was successfully guessed
    else:
        return False

def get_word_progress(secret_word, letters_guessed):
    ''' 
    secret_word: string, the word the user is guessing; assumes the letters in
      secret_word are all lowercase.
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters and carets (^) that represents
      which letters in secret_word have not been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ''
    for letter in secret_word:   #goes through all the letters in secret_word
        if letter in letters_guessed:   
            result += letter    #checks if the letter was one of the letters guessed and adds it to result if it is
        else:
            result += '^'   #puts a caret in result if the letter has not been guessed yet
    return result

def get_remaining_possible_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which 
      letters have not yet been guessed. The letters should be returned in
      alphabetical order.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ''
    for letter in string.ascii_lowercase:   
        if letter not in letters_guessed:   #if the letter of the alphabet is not in letters_guessed then it is added to result
            result += letter
            
    return result


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guesses = 0
    guesses = []    #create an empty list of guesses
    
    print("Welcome to Hangman!\nI am thinking of a word that is", len(secret_word), "letters long.")
    
    while not check_game_won(secret_word, guesses):
        if num_guesses >= 10:        #player has used up all of their guesses
            print("-----------------------------------")
            print("Sorry, you ran out of guesses")
            print("The word was", secret_word)
            break
        print("-----------------------------------")
        print("You have", 10 - num_guesses, "guesses left.")   #start with 10 guesses, decrease by 1 after each guess
        print("Available letters:", get_remaining_possible_letters(guesses))    
        letter_guessed = str.lower(input("Please guess a letter: "))    #makes letter guessed lowercase
        
        if str.isalpha(letter_guessed):     #checks to see if the guess is a letter
            if letter_guessed in guesses:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word, guesses))
            else:
                guesses.append(letter_guessed)  #adds letter_guessed to list of guessed letters
                if letter_guessed in secret_word:
                    print("Good guess:", get_word_progress(secret_word, guesses))     
                else:   #letter is not part of the word
                    print("Oops! That letter is not in my word:", get_word_progress(secret_word, guesses))
                    num_guesses += 1    #increases 1 to the guesses
        else:
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, guesses))
            
    
    if check_game_won(secret_word, guesses):        #player has won game
        print("-----------------------------------")
        print("Congratulations, you won!")
        total_score = (2*(10-num_guesses)) + (3*len(set(secret_word))*len(secret_word))
        print("Your total score for this game is", total_score)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def hangman_with_help(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make sure that
      the user puts in a letter.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol ?, you should reveal to the user one of the 
      letters missing from the word at the cost of 2 guesses. If the user does 
      not have 2 guesses remaining, print a warning message. Otherwise, add 
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guesses = 0
    guesses = []    #create an empty list of guesses
    
    print("Welcome to Hangman!\nI am thinking of a word that is", len(secret_word), "letters long.")
    
    while not check_game_won(secret_word, guesses):
        if num_guesses >= 10:        #player has used up all of their guesses
            print("-----------------------------------")
            print("Sorry, you ran out of guesses")
            print("The word was", secret_word)
            break
        print("-----------------------------------")
        print("You have", 10 - num_guesses, "guesses left.")   #start with 10 guesses, decrease by 1 after each guess
        print("Available letters:", get_remaining_possible_letters(guesses))    
        letter_guessed = str.lower(input("Please guess a letter: "))    #makes all guessed letters lowercase
        
        if letter_guessed == '?':
            if num_guesses <= 8:    #adds two to the number of guesses as long as the player hasn't guessed more than 8 already
                num_guesses += 2
                for letter in secret_word:      #finds a letter in the secret word that hasn't already been guessed correctly
                    if letter not in guesses:
                        guesses.append(letter)      #adds that letter to guesses
                        print("letter revealed:", letter, get_word_progress(secret_word, guesses))
                        break
            else:
                print("Warning: not enough guesses left")
            
        elif str.isalpha(letter_guessed):     #checks to see if the guess is a letter
            if letter_guessed in guesses:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word, guesses))
            else:
                guesses.append(letter_guessed)  #adds letter_guessed to list of guessed letters
                if letter_guessed in secret_word:
                    print("Good guess:", get_word_progress(secret_word, guesses))     
                else:   #letter is not part of the word
                    print("Oops! That letter is not in my word:", get_word_progress(secret_word, guesses))
                    num_guesses += 1    #decreases 1 from the guesses
        else:
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, guesses))
            
    
    if check_game_won(secret_word, guesses):        #player has won game
        print("-----------------------------------")
        print("Congratulations, you won!")
        total_score = (2*(10-num_guesses)) + (3*len(set(secret_word))*len(secret_word))
        print("Your total score for this game is", total_score)


# When you've completed your hangman_with_help function, comment the two similar
# lines below that were used to run the hangman function, and then uncomment
# those two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    # hangman_with_help(secret_word)
