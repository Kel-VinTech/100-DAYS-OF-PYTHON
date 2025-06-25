"""List comprehension"""

# numbers = [1,2,3]

# new_list = [n+1 for n in numbers]

# nums = range(1,5)
# num_range = [x * 2 for x in nums].upper


# condtional list comprehension

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(chars) for chars in list_of_strings]
# result = [num for num in numbers if (num % 2) == 0 ]
# print(result)
# # print(numbers)

# with open("Intermediate/Lesson/Naton_Alphabet/file1.txt") as file:
#         num_1 = [line.strip() for line in file.readlines() if line.strip()]


# with open("Intermediate/Lesson/Naton_Alphabet/file2.txt") as file:
#     num_2 = [line.strip() for line in file.readlines() if line.strip()]

# result = [int(num) for num in num_1 if num in num_2]
# print(result)

""""List comprehension with Dictionaries"""

# import random

# names= {"Alex", "Beth", "Caroline", "David", "Eleanor", "Fredie"}

# student_scores = {student:random.randint(1,100) for student in names}
# passed_score = {student:score for (student,score) in student_scores.items() if score >= 60}
# print(student_scores)
# print(passed_score)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)



# import pandas



# students_data = {
#     "student_name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Jade"],
#     "score": [85, 92, 78, 90, 88, 95, 70, 83, 76, 89]
# }

# student_db = pandas.DataFrame(students_data)

# print(student_db)

# # looping through pandas dataframe

# for (index,row) in student_db.iterrows():
#     print(row.student_name)
#     # print(row.score)




# """"NATO Alphabet   """
import pandas
nato_data = pandas.read_csv("Intermediate/Lesson/Naton_Alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index,row) in nato_data.iterrows()}

def generate_phonetics():
    user_input = str(input("Enter a word: ")).upper()
    try:
        result = [nato_dict[char] for char in user_input ]
    except KeyError:
        print("only letters in alphabet please")
        generate_phonetics()

    else:
        print(result)
        


generate_phonetics()