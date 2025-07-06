import requests
from datetime import datetime

""" Advance HTTP request
- GET - get data from an external service
- POST - give an external service a data without worrying aout the response
- PUT - update an external data
- DELETE - delete a piece of data from the external service
"""

#HTTP REQUEST 

USERNAME = "david404"
TOKEN = "twoef12573rwef"
GRAPH_ID = "kaddy2"

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}



# response = requests.post(url = pixela_endpoint, json = user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_param = {
    "id": GRAPH_ID,
    "name": "cycling graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url = graph_endpoint, json = graph_param, headers= headers)
# print(response.text)


pixe_cration_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year = 2025, month = 7, day = 7)
today_now = today.strftime("%Y%m%d")

pixel_data = {
    "date": today_now,  # Use 4-digit year
    "quantity": "49",
}


px_response = requests.post(url = pixe_cration_endpoint, json = pixel_data, headers=headers)
# print(px_response.text )


pixel_up_data = {
    "quantity": "60",

}
pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_now}"

up_response = requests.put(url = pixel_update, json = pixel_up_data, headers = headers)
# print(up_response.text)

pixel_dt =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_now}"

dt_response = requests.delete(url = pixel_dt, headers = headers)
print(dt_response.text)

