""" when handling an exception in python you need:
#try = something that might cause an exception
#except - do this if there was an exception
#else - do tis if there was no exception
#finally - do this no matter what happens"""


# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("This is the content inside")
# except KeyError as error_message:
#     print(f"Key error: {error_message}")
# else:
#     content=file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")

# # raise can be used to raise an exception
# # raise ValueError("This is an error message")



# height = float(input("height: "))
# weight = int(input("weight: "))

# if height > 3:
#     raise ValueError("Height should not be above 3 meters")

# bmi = weight/ height **2
# print(bmi)


# fruits = ["Apple", "Pear", "Orange"]

# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):

#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
        

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]


# def count_likes(posts):

#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
#         except KeyError:
#             print("This post has no likes")
            
    
#     return total_likes


# count_likes(facebook_posts)

"""this is how to read, update json data"""

# with open("data.json", "r") as data_file:
#     # json.dump(new_data,data_file,indent=4)
#     data = json.load(data_file) # how to read data from json file
#     #then update the old data with new data
#     data.update(new_data)

#     #how to update data fromjson file
#     #first read, then update the old data with new data, then save updated data
#     with open("data.json", "w") as data_file:
#         json.dump(data, data_file, indent =4)

#     entry_website.delete(0, END)  # Clear the website entry field
#     entry_password.delete(0, END)  # Clear the password entry field