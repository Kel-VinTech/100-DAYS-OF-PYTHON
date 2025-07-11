import requests
from bs4 import BeautifulSoup

header = {
    "USER-AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

user_input = (input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "))
# print(user_input)

response = requests.get(url =f"https://www.billboard.com/charts/hot-100/{user_input}")
data = response.text
# print(data)

song_list = []

soup = BeautifulSoup(data, "html.parser")
song_title = [item.get_text().strip() for item in soup.select("li.o-chart-results-list__item h3.c-title")]
song_list.append(song_title)
print(song_list)

