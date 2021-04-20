from services.questions_scraper import AmzQuestionsScraper
from time import sleep
asins = ['B07NQKTVH5', 'B08DG68P6B']
questions_list = []

for asin in asins:
    questions_1 = AmzQuestionsScraper(asin)
    for x in range(1, questions_1.total_pages + 1):
        sleep(5)
        for y in questions_1.get_questions(x):
            questions_list.append(y.text)
    questions_1.quit_driver()

print(questions_list)