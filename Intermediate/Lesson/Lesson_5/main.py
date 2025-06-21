# with open("Intermediate/Lesson/Lesson_5/weather_data.csv") as csv_data:
#     data = csv_data.readlines()
#     print(data)

temperatures = []
dir = "Intermediate/Lesson/Lesson_5/weather_data.csv"

import csv

# with open(dir) as data_files:
#     data = csv.reader(data_files)

#     for row in data:
        
#         if row[1] != "temp":
#             x = int(row[1])
#             temperatures.append(x)
#     print(temperatures)

# import pandas

# dir = "Intermediate/Lesson/Lesson_5/weather_data.csv"

# data = pandas.read_csv(dir)

# # print(data.to_dict())


# temp_list = data["temp"].to_list()
# print(temp_list)


# print(data["temp"].mean())
# print(data["temp"].max())

# print(data.condition)

# get data in rows
# data_max = data[data.temp == data.temp.max()]
# print(data_max)

# print(data[data.temp == data.temp.min()])

# monday = data[data.day == "Monday"]

# print(monday.temp[0] * 1.8 +32)

#create dataframe from scratch

# student_data = {
#     "students": ["Alice", "Bob", "Charlie", "Diana"],
#     "scores": [85, 92, 78, 90]
# }

# student_data_frame = pandas.DataFrame(student_data) 
# print(student_data_frame)
# data.to_csv("student_file.csv")

"""using the 2018 central park squirrel census data, create a dataframe that contains the fur color of the squirrels and the number of squirrels with that fur color"""

import pandas
dir = "Intermediate/Lesson/Lesson_5/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
park_data = pandas.read_csv(dir)

gray_fur_color =len(park_data[park_data["Primary Fur Color"] == "Gray"])
red_fur_color = len(park_data[park_data["Primary Fur Color"] == "Cinnamon"])
black_fur_color = len(park_data[park_data["Primary Fur Color"] == "Black"])

squirrel_summary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_fur_color,red_fur_color,black_fur_color]
}
squirrel_data_frame = pandas.DataFrame(squirrel_summary)
squirrel_data_frame.to_csv("squirrel_count.csv")

