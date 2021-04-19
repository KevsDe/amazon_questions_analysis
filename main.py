from services.questions_scraper import AmzQuestionsScraper

questions_1 = AmzQuestionsScraper('B07NQKTVH5')
questions_1.get_questions()
print(questions_1.questions_list)