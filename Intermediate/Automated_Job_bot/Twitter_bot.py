from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
class InternetSpeedTwitterBot():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.options)
        self.down = 0
        self.up = 0

    

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        self.driver.find_element(By.CLASS_NAME, "start-button").click()
        self.speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        print(f"Download Speed: {self.speed.text} Mbps")

    def tweet_at_provider(self):
        pass



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

time.sleep(20)
bot.driver.quit()
