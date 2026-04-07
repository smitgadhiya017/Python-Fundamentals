import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
print(logo[0])

choose_word = random.choice(word_list)
print(choose_word)

placeholder =""
for position in choose_word:
    placeholder += "_"

print(placeholder)

correct_letters = []
game_over = False
while not game_over:
    guess = input("Guess a Letter : ")

    display = ""
    for letter in choose_word:
        if letter == guess:
            display += guess
            correct_letters += guess
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in correct_letters:
        lives -= 1

        if lives == 0:
            game_over = True
            print("You Lose.")

    if "_" not in display:
        game_over = True
        print("You Win!")

    print(stages[lives])

