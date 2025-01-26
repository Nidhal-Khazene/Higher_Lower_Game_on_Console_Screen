from art import logo,vs
from game_data import data
from random import choice

def check_answer(u_guess, a_followers,b_followers):
    """check the user guess is correct or not."""
    if a_followers > b_followers:
        return u_guess == 'A'
    else:
        return u_guess == 'B'


def present_competitor(account):
    """format the account data into printable format"""
    return f"{account['name']}, a {account['description']}, from {account['country']}."

def game():
    print(logo)
    score = 0
    account_b = choice(data)
    should_continue = True
    while should_continue:
        account_a = account_b
        account_b = choice(data)

        if account_a == account_b:
            account_b = choice(data)

        print(f"Compare A: {present_competitor(account_a)}")
        print(vs)
        print(f"Against B: {present_competitor(account_b)}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        print("\n" * 25)
        print(logo)
        a_followers_count = account_a['follower_count']
        b_followers_count = account_b['follower_count']
        is_correct = check_answer(user_guess, a_followers_count, b_followers_count)

        if is_correct:
            score += 1
            print(f"You're right!, Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            should_continue = False

game()