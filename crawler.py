from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class product_crawler(object):
    def __init__(self,query):
        self.query=query
        self.url=f"https://www.thegioididong.com/dtdd"
        self.webdriver=webdriver.Chrome("E:\WorkSpace\capstone\crawler\chrome-driver\chromedriver.exe")
        self.delay=5
        
    def load_page(self):
        driver = self.driver
        driver.get(self.url)
        all_data= driver.find_elements_by_class_name("item")
        for data in all_data:
            print(data.text) # print infor of product
    
    

query = "tu-13-20-trieu"
crawler = product_crawler(query)
crawler.load_page()

