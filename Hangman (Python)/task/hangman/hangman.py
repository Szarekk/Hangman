import random
import sys
from string import ascii_lowercase


def valid_input(letter, guessed_letters):
    if len(letter) != 1:
        print('Please, input a single letter.')
    elif letter not in ascii_lowercase:
        print('Please, enter a lowercase letter from the English alphabet.')
    elif letter in guessed_letters:
        print('You\'ve already guessed this letter.')
    else:
        return True
    return False


def display_game(word, letters):
    print()
    print(''.join(letter if letter in letters else '-' for letter in word))
    return input('Input a letter: ')


def display_menu(wins, losses):
    answer = ''
    while answer not in ('play', 'results', 'exit'):
        answer = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if answer == 'play':
        return None
    if answer == 'results':
        print(f'You won: {wins} times.\nYou lost: {losses} times.')
        display_menu(wins, losses)
    if answer == 'exit':
        sys.exit()


def play_game(words, wins, losses):
    word = random.choice(words)
    attempts = 8
    guessed_letters = set()
    while attempts > 0:
        letter = display_game(word, guessed_letters)
        if valid_input(letter, guessed_letters):
            guessed_letters.add(letter)
            if letter not in word:
                print('That letter doesn\'t appear in the word.')
                attempts -= 1
        if all(letter in guessed_letters for letter in word):
            print(f'You guessed the word {word}!\nYou survived!')
            wins += 1
            return wins, losses
    print('\nYou lost!')
    losses += 1
    return wins, losses


words = ('python', 'java', 'swift', 'javascript')
wins, losses = 0, 0
print('H A N G M A N')

while True:
    display_menu(wins, losses)
    wins, losses = play_game(words, wins, losses)
