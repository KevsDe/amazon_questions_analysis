from selenium import webdriver
import re
from math import ceil

chrome_driver = '/home/kevin/development/chromedriver'

class AmzQuestionsScraper:
    def __init__(self, asin: str):
        self.asin = asin
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.get(f'https://www.amazon.co.uk/ask/questions/asin/{asin}/')
        self.cookies = self.driver.find_element_by_css_selector('#sp-cc-accept')
        self.cookies.click()
        self.total_pages = self.get_total_pages()

    def get_total_pages(self):
        number = self.driver.find_element_by_xpath('//*[@id="a-page"]/div[1]/div[5]/table/tbody/tr/td[1]/div/span').text
        total_questions = int(re.findall(r' \d* ', number)[0].strip())
        total_pages = ceil(total_questions / 10)
        return total_pages

    def get_questions(self, idx):
        self.driver.implicitly_wait(5)
        self.driver.get(f'https://www.amazon.co.uk/ask/questions/asin/{self.asin}/{idx}/')
        return self.driver.find_elements_by_css_selector('.a-declarative')

    def quit_driver(self):
        self.driver.quit()
