import random       


print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")


answer = random.randint(1,100)
print(answer)

def guess_calc(attempts):
    
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
        


game_level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if game_level == "easy":
    attempts = 10
    guess_calc(attempts)

elif game_level == "hard":
    attempts = 5
    guess_calc(attempts)
else:
    print("Invalid difficulty level. Please restart the game.")
    


# """ TODO:1 write the code functionality for thr hard guess game:
# the user guess should match the random number generated else reduce the number of times to guess
# print the lower or high if the guess is higher or lower than the random number
#  """


