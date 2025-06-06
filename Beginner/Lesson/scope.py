import random       

 ### comment this out or remove this if you don't want to output the answer to the users


# the code below is a function to do the calculations of the game.
def guess_calc(attempts, answer):
    
    ### this while loop keeps running provided the number of attempts is greater than zero.
    while attempts > 0:

        print(f"you have {(attempts)} attempts remaining to guess the number ")
        guess = int(input("Make a guess: "))

        if guess ==  answer:
            print("You got it right! The answer was {answer}")
            return
        attempts -= 1

        if attempts == 0 :
            print("You've run out of guesses.")
        else:
            if guess > answer:
                print("Too High")
            else:
                print("Too Low")

    #this code breaks out of the while loop to allow users restart the game           
    restart_game = input("do you want to restart the game? Type 'Y' or 'N': ").lower()
    if restart_game == 'y':
        start_game()
    else:
        return    


# the code below is a function to get the game started
def start_game():

    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")


    answer = random.randint(1,100)
    print(answer)

    game_level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if game_level == "easy":
        attempts = 10
        guess_calc(attempts,answer)

    elif game_level == "hard":
        attempts = 5
        guess_calc(attempts,answer)
    else:
        print("Invalid difficulty level. Please restart the game.")
    
start_game()
    



