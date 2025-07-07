import requests
from datetime import datetime
from habit_private_key import API_ID,API_KEY, HEADER

GENDER = "male"
WEIGHT_KG = 45
HEIGHT_CM = 145
AGE =   20


headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

nutrient_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text= input("tell me what exercise you did: ")

parameter = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age" : AGE
}


response = requests.post(url = nutrient_endpoint, json=parameter, headers = headers)
results = response.json()

# Sheety API endpoint
SHEETY_ENDPOINT = "https://api.sheety.co/f79aadcd14f247f871465aa52a3eae2f/workout/workouts"

headers = HEADER

today_date = datetime.now().strftime("%d%m%y")
now_time =datetime.now().strftime("%X")


for exercise in results["exercises"]:
    sheet_name = {
        "workout": {
            "date" : today_date,
            "time" : now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(
    SHEETY_ENDPOINT,
    json = sheet_name,
    # headers=headers
    )
print(sheet_response.text)

# dt_response = requests.delete(url = "https://api.sheety.co/f79aadcd14f247f871465aa52a3eae2f/workout/workouts/2")
# print(dt_response.text)

