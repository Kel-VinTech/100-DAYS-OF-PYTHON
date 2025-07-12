import requests
from bs4 import BeautifulSoup


response = requests.get(url= "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
data = response.text
soup = BeautifulSoup(data, "html.parser")
text = soup.find(class_ ="a-price")
acutal_price = text
print(acutal_price)
