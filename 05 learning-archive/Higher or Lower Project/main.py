from hmac import compare_digest
from operator import truediv
from threading import active_count
from wsgiref.util import request_uri

from art import logo
from art import vs
from game_data import data
import random

# Function to formate the data
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_followers = account["follower_count"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_description} from {account_country}"


# Funciton to Compare the data
def comparing_data(guess, A_followers, B_followers,):
    """Compares the followers and gives true or False."""
    # compairng a and b, and relating it with guess

    if guess == max(A_followers, B_followers): # [?]IF right, add the score, and continue the game
        return True
    else:
        return False



# The global constants ??


# Game function
def higher_lower():

    # infinte loop to play again n again
    playing_game = True
    while playing_game:
        # Score outside to record next loop
        score = 0
        # looping the game until wrong answer
        continuing = True
        # Choosing accounts
        account_a = random.choice(data)
        while continuing:
            ## [?] How to set the account a = guess if guess correct
            # account_a = account_b
            # account_b = random.choice(data)
            # if account_a == account_b:
            #     account_b = random.choice(data)
            account_b = random.choice(data)

            # the followers of accounts
            a_followers = account_a["follower_count"]
            b_followers = account_b["follower_count"]

            # the Game View
            print(f"A: {format_data(account_a)}     {a_followers}")
            print(vs)
            print(f"B: {format_data(account_b)}     {b_followers}")


            # letting user guess
            guess = input("Who has more followers ")
            if guess == "a":
                guess = a_followers
            else:
                guess = b_followers

            # Checking the answer
            is_correct = comparing_data(guess, a_followers, b_followers)

            next_account = ""
            if a_followers > b_followers:
                next_account = account_a
            else:
                next_account = account_b


            # Keeping score
            if is_correct:
                score += 1
                print(f"Your Score: {score}")
                account_a = next_account
            else:
                continuing = False
                print("you lost" )
                print("\n"*100)

higher_lower()