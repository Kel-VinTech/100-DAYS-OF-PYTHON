
# #Caeser cipher
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# def caesar(original_text, shift_amount, encode_or_decode):

#     output_text=""

#     if encode_or_decode == "decode":
#         shift_amount *= - 1

#     for letter in original_text:

#         if letter not in alphabet:
#             output_text += letter
#         else:
            
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet)
#             output_text += alphabet[shifted_position]
#     print(f"The {encode_or_decode}d text is {output_text}")

# should_continue = True

# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text =  input("Type your message:\n").lower()
#     shift= int(input("Type your shift number:\n"))

#     caesar(original_text = text, shift_amount = shift,encode_or_decode = direction)

#     retry = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

#     if retry == "no":
#         should_continue = False
#         print("Game Over, Goodbye!!")





# Python Dictionary

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
# }

# # programming_dictionary = {}

# programming_dictionary["Blue"] = "Color"

# for key in programming_dictionary:
#     print(programming_dictionary[key])


# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grade = {}

# for student in student_scores:
#     score = student_scores[student]

#     if score >= 91:
#         student_grade[student] = "Outstanding"
#     elif score >= 81:
#         student_grade[student] = "Exceeds Expectations"
#     elif score >= 71 :
#         student_grade[student] = "Acceptable"
#     else:
#         student_grade[student] = "Fail"

# print(student_scores[student])


travel_log = {
    "France" : ["Paris", "Lille", "Dijon"]
}

# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

# travel_log = {
#     "France" :{
#         "cities_visited" :  ["Paris", "Lille", "Dijon"],
#         "total_visits": 8     
#     },
#     "Germany" : {
#         "cities_visited" :  ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5  
#     }
# }


# print(travel_log["Germany"]["cities_visited"][2])

# create a dic when=re name is key and bid is the value.loop through the dic and see who gas made the higgest bid and decalre them the winner
# should_continue = True

# while should_continue:

#     if should_continue == "no":
#         print("Game Over, Goodbye!!")

# print("hello")
# print("\n" * 100)
# input("Press Enter to continue...")

def find_highest_bid(auction_bid):
    highest_bid = 0
    winner = ""

    for bidder in auction_bid:
        bid_amount = auction_bid[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The Winner is {winner} with a bid of {highest_bid}")



bid_dict = {}

should_continue = True

while should_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bid_dict[name] = bid

    more_bids = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    
    
    if more_bids == "no":
        should_continue = False
        find_highest_bid(bid_dict)
    
    elif more_bids == "yes":
       print("\n" * 100)


