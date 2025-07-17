from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://www.linkedin.com/jobs/search/?currentJobId=4268101048&f_AL=true&f_E=1%2C2&f_WT=2&geoId=103644278&keywords=social%20media%20manager&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD"
driver.get(url=url)


time.sleep(3)
driver.quit()
 
