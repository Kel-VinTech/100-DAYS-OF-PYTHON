from bs4 import BeautifulSoup
import requests
import pandas

# import lxml

# with open ("Intermediate/web_scrapping/website.html", "r") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")


# # print(soup.title.string)
# # print(soup.prettify())

# all_paragraphs = soup.find_all('p')
# # print(all_paragraphs)

# for tags in all_paragraphs:
#     print(tags.get_text())
    




# response = requests.get(url = "https://appbrewery.github.io/news.ycombinator.com/")
# hack_web = response.text


# soup  = BeautifulSoup(hack_web, "html.parser")

# articles = soup.find_all("a", class_ = "storylink")
# article_text = []
# article_link = []

# for article in articles:
#     text = article.getText()
#     article_text.append(text)
#     link = article.get("href")
#     article_link.append(link)

# article_upvote = [int(score.getText().split()[0])for score in soup.find_all("span", class_ = "score")]
# largest_number = max(article_upvote)
# position = article_upvote.index(largest_number)
# print(article_link[position])
# print(article_text[position])
# # print(article_link)
# # print(article_text)
# # print(article_upvote)



""" scraping a movie website and turning the ouput into a text file"""

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movie_web = response.text

soup = BeautifulSoup(movie_web, "html.parser")

# print(soup.prettify())

movies = [title.getText() for title in soup.find_all("h3", class_  ="title")]

#to reverse the list
movies = movies[::-1]

#use pandas 
# df = pandas.DataFrame(movies)
# df.to_csv("Movies.txt",index=False, header =False)

#use a for loop

with open("Movies.txt", mode = "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")





