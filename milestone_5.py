import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user to guess a letter.
    '''    
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
        print(f'The mystery word has {self.num_letters} unique characters.')
        print(f'\n{self.word_guessed}')
        
    def check_guess(self, guess):
        '''
        Checks if the guessed letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked

        '''         
        guess.lower()

        if guess in self.word:
            print(f'\nGood guess! {guess} is in the word.') 
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = letter 
            self.num_letters -= 1  
            print(self.word_guessed) 
        else:
            self.num_lives -= 1 
            print(f'\nSorry, {guess} is not in the word. Try again.')
            print(f'\nYou have {self.num_lives} lives left.')

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        '''        
        while True:
            guess = input('Guess a letter. \n')
            if not (len(guess) == 1 and guess.isalpha()):
                print('\nInvalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('\nYou already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)    
                break
                
def play_game(word_list):
    '''
    Creates a hangman game object, passing in the word list to choose a random word from.
    It then loops through the hangman game functions until the player either succeeds in guessing
    the word or runs out of lives before guessing the word.
    
    Parameters:
    ----------
    word_list: str
        The list of words from which a random word is chosen as the mystery word.
    
    '''      
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f'\nYou lost! The word was {game.word}.')
            break
        elif game.num_letters > 0:    
            game.ask_for_input()
        else:
            print('\nCongratulations. You won the game!')
            break
                
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)           
 