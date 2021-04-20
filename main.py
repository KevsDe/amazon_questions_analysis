from services.questions_scraper import AmzQuestionsScraper
from time import sleep
import pandas as pd
asins = ['B06XR32F98', 'B00XQ2XGAA', 'B07KX2GSL5', 'B083KNQJW8', 'B079C336Y3', 'B0847C7P5P', 'B07NQKTVH5', 'B07XY4V526',
         'B07YLKCQZT', 'B07Q6YSGF9']
questions_list = []

for asin in asins:
    questions_1 = AmzQuestionsScraper(asin)
    for x in range(1, questions_1.total_pages + 1):
        sleep(3)
        for y in questions_1.get_questions(x):
            questions_list.append(y.text)
    questions_1.quit_driver()


d = {'question': questions_list}
df = pd.DataFrame(data=d)

df.to_csv('output/amz_questions.csv')
