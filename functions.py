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

def win_announcement(tries, word_shown):
    print(f"Congrats! You guessed it in {10 - tries} guesses.\n")
    print('===========================')
    print("The word was:", "".join(word_shown))
    print('===========================')

def round_start(word_shown, guessed_wrong, tries):
    print("Word:", " ".join(word_shown))
    print('===========================')
    print("Wrong guesses:", " ".join(guessed_wrong))
    print(f"Tries left: {tries}")

def main():
    print("🎮 Welcome to Hangman!")
    print("Guess the hidden word.\n")
    tries = 10
    word = pick_randon_word()
    word_shown = ["_" for _ in range(len(word))]
    guessed_wrong = []
    while tries > 0:
        guessed = guessed_wrong + word_shown
        round_start(word_shown, guessed_wrong, tries)
        print('\n')
        current = input("Guess a letter: ").lower()
        if not is_letter(current):
            print("Sorry, that is not a letter\n")
            continue
        if was_guessed(current,guessed):
            print("You've already guessed it.\n")
            continue
        if check(current,word):
            print(f"✅ '{current}' is in the word!\n")
            word_shown = fill_word(word_shown, word, current)
            if "_" not in word_shown:
                win_announcement(tries, word_shown)
                break
        else:
            print(f"❌ '{current}' is not in the word.\n")
            tries -= 1
            if tries == 0:
                print(f"No more guesses left, the word was: {word}")
                break
            guessed_wrong.append(current)





