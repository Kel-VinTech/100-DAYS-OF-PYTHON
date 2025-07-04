import requests
api_key = "ac772c593742edde8cc6ea973f24fc30"


"""Learning about Apis authentication"""

weather_param = {
    "lat": 9.5,
    "lon": 2.25,
    "appid": api_key,
    "cnt": 4,
}



API_LOCATION = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(API_LOCATION,params = weather_param)
print(response.raise_for_status())
print(response)
data = response.json()
weather_id = data["list"][0]["weather"][0]["id"]
weather_desc = data["list"][0]["weather"][0]["description"]
print(weather_id)
print(weather_desc)

for forcast in data["list"]:
    if weather_id < 700:
        print("bring an umbrella")

