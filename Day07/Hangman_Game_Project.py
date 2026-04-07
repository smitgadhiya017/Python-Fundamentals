import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
print(logo[0])

random_word = random.choice(word_list)

placeholder =""
for position in random_word:
    placeholder += '_'

print("Word :",placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************{lives}/6 LIVES LEFT***************")
    guess = input("Guess a letter : ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in random_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display +='_'

    print(display)

    if guess not in random_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"***************IT WAS {random_word}! YOU LOSE.***************")


    if '_' not in display:
        game_over = True
        print("***************YOU WIN!***************")

    print(stages[lives])