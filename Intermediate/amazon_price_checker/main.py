import requests
import smtplib
from bs4 import BeautifulSoup


from dotenv import load_dotenv
import os

load_dotenv()

my_email =os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
smtp_address = os.getenv("SMTP_ADDRESS")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

amazon_live_link = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

amazon_st_link = "https://appbrewery.github.io/instant_pot/"


response = requests.get(url= amazon_live_link, headers=headers)
data = response.text



soup = BeautifulSoup(data, "html.parser")
# print(soup.prettify())


text = soup.find("span",class_ ="aok-offscreen").get_text()
actual_price = float(text.split()[0].split("$")[1])

if actual_price < float(100.00):
    with smtplib.SMTP(smtp_address,port =587) as connection:
        connection.starttls()
        connection.login(user = my_email, password =my_password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs="kingdavidxr@gmail.com",
            msg=f"Subject: New Price Alert\n\n Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, ${actual_price}"
        )
