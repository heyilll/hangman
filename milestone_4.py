import random

class Hangman:
    def __init__(self,word_list,num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_', '_', '_', '_', '_']
        self.num_letters = 0
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    def check_guess(self,guess): 
        guess.lower()

        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i in range(self.word):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
            self.num_letters -= 1   
        else:
            self.num_lives -= 1 
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter.')
            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)        

h1 = Hangman(['orange', 'mango', 'guava', 'watermelon', 'peach'],5)
h1.ask_for_input()  