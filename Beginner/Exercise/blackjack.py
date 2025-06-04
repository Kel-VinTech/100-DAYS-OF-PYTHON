import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    
    user_first_choice = random.choices(cards,k=2)
    computer_first_choice = random.choices(cards,k=2)

    user_total_values = sum(user_first_choice)
    computer_total_values = sum(computer_first_choice)

    print(user_first_choice)
    print(computer_first_choice)

    print(f"your cards: {user_first_choice}, current score: {user_total_values}")
    print(f"computer's first cards: {computer_first_choice}, current score: {computer_total_values}")


should_start_game = True
while should_start_game:
    game_start = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()

    if game_start == 'yes':
        blackjack()
    else:
        should_start_game = False
        print("You have chosen to exit the game. Goodbye!")