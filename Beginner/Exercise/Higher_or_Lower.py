import random

from game_data import data

#TODO1 : get the formatted string of the data
def get_formatted_data(account):
    """Format the account data for display and returns as output."""

    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"       


#Todo2: get the random choice from thr data list

    
def check_user_guess (user_guess, a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == "b"

    
score = 0

start_game = True
account_b = random.choice(data)

while start_game:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data) 
    
    print(f"Compare A: {get_formatted_data(account_a)}")
    print("\n"* 1)
    print(f"Compare B: {get_formatted_data(account_b)}") 

    user_guess = input("who has more followers? Type 'A' or 'B': ").lower()


    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_user_guess(user_guess,a_followers,b_followers)
    

    if is_correct:
        score +=1
        print(f"You are right! Current score is: {score}")
    else:
        print(f"You guessed wrong, final score is {score}")
        start_game = False

