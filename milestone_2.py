import random

word_list = ['orange', 'mango', 'guava', 'watermelon', 'peach']
#print(word_list)

word = random.choice(word_list)
#print(word)

guess = input('Enter a single letter.')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That input is not valid.')