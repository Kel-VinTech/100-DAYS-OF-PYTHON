# import random

# Defining a Function

# def print_name():
#     for steps in range(6):
#         print("Kelvin")

# print_name()


# fruits = ["apples", "pawpaw", "mango", "corn"]

# for fruit in fruits:
#     print(f'{fruit} pie')



# number_of_steps = 6

# while number_of_steps >0:
#     print("Kelvin")
#     number_of_steps -= 1
#     print(number_of_steps)

# word_list = ["baboon", "camel", "donkey", "elephant", "flamingo", "giraffe", "hippo", "vulture", "walrus", "yak", "zebra"]

# game_over = False

# while not game_over:
#     chosen_word = random.choice(word_list)
#     print(chosen_word)

#     guess = str(input("Guess a word: ")).lower()

#     placeholder = "_ " * len(chosen_word)

#     display = ""
#     correct_words = []

#     no_of_trials = len(chosen_word)

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_words.append(guess)

#         elif  letter in correct_words:
#             display += letter
#         else:
#             display += " "

#     print(display)

#     if guess not in chosen_word:
#         no_of_trials -= 1
#         print(f"you got {no_of_trials} trials left")
#         print("letter not in the chosen word")
#         if no_of_trials == 0:
#             game_over = True
#             print("Game Over, You Lose!!")
            
#     if "_" not in display:
#         game_over= True
#         print("You Win!!")


#     if guess in correct_words:
#         print("you have guessed this letter")





""" debugging"""
