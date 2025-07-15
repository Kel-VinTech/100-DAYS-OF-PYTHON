from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select




# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Ensure desktop view
# options.add_argument("--headless")  # Uncomment if you want headless
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


# Open the page
# driver.get("https://secure-retreat-92358.herokuapp.com/")

# # Wait for search box to be present first
# # wait = WebDriverWait(driver, 10)
# # fname = wait.until(EC.presence_of_element_located((By.NAME, "fName")))
# # lName = wait.until(EC.presence_of_all_elements_located((By.NAME, "lName")))
# # wait.until(EC.element_to_be_clickable((By.NAME, "search")))

# fname = driver.find_element(By.NAME, "fName")
# lname = driver.find_element(By.NAME, "lName")
# email = driver.find_element(By.NAME, "email")
# button = driver.find_element(By.CLASS_NAME, "btn")

# # Type "python" and press Enter
# fname.send_keys("Kelvin")
# lname.send_keys("Leven")
# email.send_keys("kingdavidxr@gmail.com")
# button.click()

# # Quit the driver
# import time
# time.sleep(3)
# driver.quit()

url = "https://ozh.github.io/cookieclicker/"
driver.get(url)
select = Select(driver.find_element(By.ID, "langSelect"))
select.select_by_value("EN")



driver.quit()

