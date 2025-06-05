import random

should_start_game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_choices = []
computer_choices = []

def blackjack():

    for _ in range(2):
        user_choices.append(random.choice(cards))
        computer_choices.append(random.choice(cards))
        
    user_total_values = sum(user_choices)
    computer_total_values = sum(computer_choices)
        

    print(f"your cards: {user_choices}, current score: {user_total_values}")
    print(f"computer's first cards: {computer_choices}, current score: {computer_total_values}")
    

    for element in user_choices:
        print(element)
        if element == 11 and element == 10 and len(user_choices) == 2:
            print("User has BlackJack!!! User Wins")
        elif element != 11 and element != 10:

            if user_total_values > 21:
                if 11 in user_choices:
                    if user_total_values - 10 > 21:
                        print("Game Over, You Lose!")
                    else:
                        start_another_round = True
                else:
                    print("Game Over, You Lose!")
            elif user_total_values < 21:
                print(print)
                start_another_round = True
 
    # computer choices

    for element in computer_choices:
        if element == 11 and element == 10 and len(computer_choices) == 2:
            print("Computer has BlackJack!!! Computer Wins")
            start_another_round = True
            
            
    # else:
    #     # start_another_round = True

    # THIS LOOP IS TO START THE SECOND ROUND OF PICKING A CARD
    start_another_round = True

    while start_another_round:
        pick_another_card = input("Type 'y' to get another card, Type 'n' to skip: ").lower()


        if pick_another_card == 'y':
                for _ in range(1):
                    user_choices.append(random.choice(cards))
                    user_total_values = sum(user_choices)
                    computer_total_values = sum(computer_choices)
                    print(f"your cards: {user_choices}, current score: {user_total_values}")
                    print(f"computer's first cards: {computer_choices}, current score: {computer_total_values}")
                   

        elif pick_another_card == 'n':
            if computer_total_values < 17:
                
                for _ in range(1):
                    computer_choices.append(random.choice(cards))
                    computer_total_values = sum(computer_choices)
                    print(f"your final hand: {user_choices}, current score: {user_total_values}")
                    print(f"computer's final hand: {computer_choices}, current score: {computer_total_values}")
            if computer_total_values > 21:
                print("Game Over, Computer Lost!")
                should_start_game = True  
            else:
                if user_total_values > computer_total_values:
                    print("Game Over, User Wins!!!")
                    # should_start_game = False  
                    
                elif computer_total_values > user_total_values:
                    
                    print("Game Over, Computer Wins!")
                    should_start_game = True  
                else:
                    print("It's a Draw")
 



# this loop is to start and end the game
while should_start_game:
    game_start = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()

    if game_start == 'yes':
        blackjack()
    else:
        should_start_game = False
        print("You have chosen to exit the game. Goodbye!")