import os
import datetime

now = datetime.datetime.now()
log_name = "report.txt"
log_path = os.path.abspath(log_name)


def get_log(primary_function):
    def new_function(a, b, user_path_log=log_path):
        with open(user_path_log, 'a', encoding='utf-8') as f:
            path_log = os.path.abspath(log_name)
            f.write(f'\n{"_" * len(os.path.abspath(log_name))}\n')
            f.write(f'Дата и время вызова функции: {now.strftime("%d.%m.%Y %H:%M")}\n')
            f.write(f'Вызвана функция {primary_function.__name__} с аргументами {a} и {b}\n')
            result = primary_function(a, b)
            f.write(f'Результат: {str(result)}\n')
            f.write(f'{path_log}\n')
            f.write(f'{"_" * len(os.path.abspath(log_name))}\n')
            return result
    return new_function


def get_log_questions(questions_function):
    def new_function(user_path_log=log_path):
        with open(user_path_log, 'a', encoding='utf-8') as f:
            path_log = os.path.abspath(log_name)
            f.write(f'\n{"_" * len(os.path.abspath(log_name))}\n')
            f.write(f'Дата и время вызова функции: {now.strftime("%d.%m.%Y %H:%M")}\n')
            f.write(f'Вызвана функция {questions_function.__name__}\n')
            result = questions_function()
            f.write(f'Все вопросы за последние два дня и содержит тэг "Python" с сайта stackoverflow:\n')
            for res in result:
                f.write(f'---> {res}\n')
            f.write(f'{path_log}\n')
            f.write(f'{"_" * len(os.path.abspath(log_name))}\n')
            return result
    return new_function
