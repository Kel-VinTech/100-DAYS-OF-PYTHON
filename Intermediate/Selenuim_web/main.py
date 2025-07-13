# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://www.python.org/"
driver.get(url=url)

# wait = WebDriverWait(driver,10)
# price_container =wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price")))

# price_dollar = price_container.find_element(By.CLASS_NAME, value = "a-price-whole")
# price_cent = price_container.find_element(By.CLASS_NAME, value = "a-price-fraction")

# print(f"The price is {price_dollar.text}.{price_cent.text}")


event_time = {item.text for item in driver.find_elements(By.CSS_SELECTOR, ".event-widget time")}
event_text = {item.text for item in driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")}
events = {}

for n in range(len(event_time)):
    events[n] = {
        "time": event_time  ,
        "name" : event_text 
    }
    
print(events)

driver.quit()
