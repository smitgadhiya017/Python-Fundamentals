# Display Art
import random
from art import logo,vs
from game_data import data

def format_data(account):
    """Take the account data and return the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo[0])
score = 0
game_should_continue = True
account_b = random.choice(data)

# Fetch Random data
while game_should_continue:
    # Making account  at position B become the next account at Position A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs[0])
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more Followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo[0])

    # If user guess right then +1 point continue else game over
    # - Get follower count of each account
    a_follower_count = account_a["followers"]
    b_follower_count = account_b["followers"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess.
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False

# Make the game repeatable.