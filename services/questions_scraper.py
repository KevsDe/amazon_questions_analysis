from selenium import webdriver
import re
from math import ceil
from time import sleep
import pandas as pd

chrome_driver = '/home/kevin/development/chromedriver'


class AmzQuestionsScraper:
    def __init__(self, asin: str):
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.get(f'https://www.amazon.co.uk/ask/questions/asin/{asin}/')
        self.cookies = self.driver.find_element_by_css_selector('#sp-cc-accept')
        self.cookies.click()
        self.questions_list = []

    def get_questions(self):
        number = self.driver.find_element_by_xpath('//*[@id="a-page"]/div[1]/div[5]/table/tbody/tr/td[1]/div/span').text
        total_questions = int(re.findall(r' \d* ', number)[0].strip())
        total_pages = ceil(total_questions / 10)
        for x in range(total_pages):
            sleep(2)
            questions = self.driver.find_elements_by_css_selector('.a-declarative')
            self.questions_list.append(questions)
            next_page = self.driver.find_element_by_css_selector('.a-last')
            next_page.click()

