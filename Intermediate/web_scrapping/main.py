from bs4 import BeautifulSoup
import requests

response = requests.get(url = "https://appbrewery.github.io/news.ycombinator.com/")
hack_web = response.text


soup  = BeautifulSoup(hack_web, "html.parser")

a_tag = soup.find("a", class_ = "storylink")
article_text = a_tag.get_text()
article_link = a_tag.find("a")
print(article_link)
print(article_text)









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
    