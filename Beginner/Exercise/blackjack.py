import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_choices = []
computer_choices = []

def blackjack():

    for i in range(2):
        user_choices.append(random.choice(cards))
        computer_choices.append(random.choice(cards))

    user_total_values = sum(user_choices)
    computer_total_values = sum(computer_choices)

    print(f"your cards: {user_choices}, current score: {user_total_values}")
    print(f"computer's first cards: {computer_choices}, current score: {computer_total_values}")


    start_another_round = True

    while start_another_round:
        pick_another_card = input("Type 'y' to get another card, Type 'n' to skip").lower()

        if pick_another_card == 'y':
            # user_other_choice = random.choices(cards,k=1)
            # computer_other_choice = random.choices(cards,k=1)

            # user_total_values = sum(user_other_choice)
            # computer_total_values = sum(computer_other_choice) 
            for _ in range(1):
                user_choices.append(random.choice(cards))
            else:
                computer_choices.append(random.choice(cards))
















should_start_game = True
while should_start_game:
    game_start = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()

    if game_start == 'yes':
        blackjack()
    else:
        should_start_game = False
        print("You have chosen to exit the game. Goodbye!")