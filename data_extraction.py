from services.questions_scraper import AmzQuestionsScraper
from time import sleep
import pandas as pd

#Data extraction
asins = ['B06XR32F98', 'B00XQ2XGAA', 'B07KX2GSL5', 'B083KNQJW8', 'B079C336Y3', 'B0847C7P5P', 'B07NQKTVH5', 'B07XY4V526',
         'B07YLKCQZT', 'B07Q6YSGF9', 'B08WJ2QHFY', 'B01947XDNK', 'B077NDS9V3', 'B07G5H6FC2', 'B083WM96KQ', 'B08K3M7JD1']

asins = list(set(asins))

questions_list = []

for asin in asins:
    questions_1 = AmzQuestionsScraper(asin)
    for x in range(1, questions_1.total_pages + 1):
        sleep(3)
        for question in questions_1.get_questions(x):
            questions_list.append(question.text)
    questions_1.quit_driver()

scraped_data = {'question': questions_list}
df = pd.DataFrame(data=scraped_data)
df.to_csv('output/amz_questions.csv')
