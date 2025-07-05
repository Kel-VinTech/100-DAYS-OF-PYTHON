import requests

""" Advance HTTP request
- GET - get data from an external service
- POST - give an external service a data without worrying aout the response
- PUT - update an external data
- DELETE - delete a piece of data from the external service
"""

#HTTP REQUEST 

USERNAME = "david404"
TOKEN = "twoef12573rwef"

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
    "id": "kaddy2",
    "name": "cycling graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url = graph_endpoint, json = graph_param, headers= headers)
print(response.text)

