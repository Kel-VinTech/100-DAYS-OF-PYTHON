from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://en.wikipedia.org/wiki/Main_Page"


driver.get(url = url)

data = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(data.text)

driver.quit()
