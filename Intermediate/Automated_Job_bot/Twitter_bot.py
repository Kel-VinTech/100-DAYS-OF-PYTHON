from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
class InternetSpeedTwitterBot():
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.down = 0
        self.up = 0

    

    def get_internet_speed(self):
        pass


    def tweet_at_provider(self):
        pass



bot = InternetSpeedTwitterBot
bot.get_internet_speed()
bot.tweet_at_provider()
