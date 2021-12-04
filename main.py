import requests
from get_log_file import get_log, input_path_to_log, get_log_questions


@get_log
def multipliers(a, b, c):
    return a * b * c


@input_path_to_log()
def summator(a, b):
    return a + b


@get_log_questions
def get_questions():
    url = "https://api.stackexchange.com/2.3/questions"
    params = {"fromdate": 1630454400, "todate": 1632096000, "order": "desc", "sort": "activity", "tagged": "Python",
              "site": "stackoverflow"}
    response = requests.get(url, headers={'User-agent': 'netology'}, params=params)
    questions = response.json()
    questions_list = []
    title_list = []
    for quest in questions['items']:
        questions_list.append(quest)
    for title in questions_list:
        title_list.append(title['title'])
    return title_list


multipliers(5, 15, 25)
summator(4, 8)
get_questions()
