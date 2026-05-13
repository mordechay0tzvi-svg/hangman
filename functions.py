from words import *
import random

def pick_randon_word():
    return words[random.randint(0,len(words)-1)]

def is_letter(char):
    return len(char) == 1 and char.isalpha()

def was_guessed(letter,guessed):
    return letter in guessed

def check(letter,word_to_guess):
    return letter in word_to_guess

def fill_word(word_guessed, word, letter):
    for place in range(len(word)):
        if word[place] == letter:
            word_guessed[place] = letter
    return word_guessed
