# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    '''
  for every letter in secret_word
    if letter is NOT in letters_guessed
      stop looking and return False

  success, all letters guessed correctly
  return True
  '''

    for letters in secret_word:
      if letters not in letters_guessed:
        return False
    return True



### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    
    '''
    output_string = ''
    for every letter in secret_word
      if the letter is in letters_guessed
        concatenate that letter on to output_string
      otherwise
        concatenate underscore space on to output_string

      return output_string
    '''
    
    output_string = ''

    for letters in secret_word:
      if letters in letters_guessed:
        output_string += letters
      else:
        output_string += '_ '
    return output_string
    
    
    
      
#Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))
# print(get_guessed_word ('grapefruit', ['k', 'm', 'b', 'j', 'e', 'w', 's', 'z', 'u', 'x']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    '''
    convert lowercase alphabet from string to list
      for every letter in letters_guessed
        .remove the letters from the lowercase alphabet
      return lowercase letters
    '''

    import string
    lowercase = string.ascii_lowercase

    for letters in letters_guessed:
      if letters in lowercase:
        lowercase = lowercase.replace(letters, '')
    return lowercase



#Testcases 
# print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))
# print(get_available_letters(['p', 'r', 'f', 'd', 'k', 'h', 'c', 'a', 'i', 'y', 'w', 'b']))
  
def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    guesses_remaining = 8
    letters_guessed = []

    print ('Let the game begin!')
    print('I am thinking of a word with', secretWordLength(secret_word), 'letters.')

    while is_word_guessed(secret_word, letters_guessed) == False:
      print('You have ', guesses_remaining, 'guesses remaining.')
      print('Letters available to you: ', get_available_letters(letters_guessed))
      guessed_input = input('Guess a Letter: ')

      if guessed_input in get_available_letters(letters_guessed):
        letters_guessed.append(guessed_input)
        if(guessed_input in secret_word):
          print('Correct: ', get_guessed_word(secret_word, letters_guessed))
        else:
          print('Incorrect, this letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
          guesses_remaining -= 1
      else:
        print('You fool! You tried this letter already: ', get_guessed_word(secret_word, letters_guessed))

      if guesses_remaining == 0:
        break

    if is_word_guessed(secret_word, letters_guessed) == True:
      print('You Win!')
    else:
      print('Game Over! The word was ', secret_word)

def secretWordLength(secret_word):
    result = 0
    for letters in secret_word:
      result += 1
    return result

def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

    

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()
    

    
