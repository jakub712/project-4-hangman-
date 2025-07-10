from words import easy_with_hints, medium_with_hints, hard_with_hints
import random
from colorama import Fore, Style, init
init(autoreset=True)
alphabet = list("abcdefghijklmnopqrstuvwxyz")
guesses = 0
guessed_letters = ("")

while True:
    difficulty = input("Pick easy, medium or hard. ")
    if difficulty not in ["easy", "medium", "hard"]:
        print("please write easy, medium or hard.")
    else:
        break

if difficulty == "easy":
    word = (random.choice(list(easy_with_hints.keys())))
    clue = easy_with_hints[word]
elif difficulty == "medium":
    word = (random.choice(list(medium_with_hints.keys())))
    clue = medium_with_hints[word]
else:
    word = (random.choice(list(hard_with_hints.keys()))) 
    clue = hard_with_hints[word]

for i in str(len(word)):
    x = list("_" * len(word))


lives = 6



while True:

    if guesses == 0:
        print(word)##### DELETE THIS LATER!
        print(x)
    
    word_list = list(word)
    guess = input(f"pick a letter a-z, you have {lives} lives. The hint is think of a {clue}. ")

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter (a-z only).")
        continue



    if guess in guessed_letters:
        print("you already guessed this letter")    
        continue

    if guess in word:
        # Update all positions where the letter appears
        for idx, letter in enumerate(word):
            if letter == guess:
                x[idx] = guess
        print(f"{guess} was in the word")
        if guesses > 0:
            print(x)
    
    if guess not in word:
        guesses +=1
        lives -= 1
        print(f"{guess} was not in word.")

    guessed_letters += guess

    if lives > 0 and "_" not in x:
        print("You Win!")
        print(f"The word was {word}")

    if lives == 0:
        print(f"You Lose! The word was {word}")

