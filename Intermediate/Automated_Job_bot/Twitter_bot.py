from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
class InternetSpeedTwitterBot():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.options)
        self.down = 0
        self.up = 0

    

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/result/18003965361")


    def tweet_at_provider(self):
        pass



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

time.sleep(5)
bot.driver.quit()
