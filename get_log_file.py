import os
import datetime

now = datetime.datetime.now()
log_name = "report.txt"
log_path = os.path.abspath(log_name)


# задание 1
def get_log(primary_function):
    def new_function(*args, **kwargs):
        with open(log_name, 'a', encoding='utf-8') as f:
            path_log = os.path.abspath(log_name)
            f.write(f'\n{"_" * len(path_log)}\n')
            f.write(f'Дата и время вызова функции: {now.strftime("%d.%m.%Y %H:%M")}\n')
            f.write(f'Вызвана функция {primary_function.__name__} с аргументами {args}\n')
            result = primary_function(*args, **kwargs)
            f.write(f'Результат: {str(result)}\n')
            f.write(f'{"_" * len(path_log)}\n')
            return result

    return new_function


# задание 2
def input_path_to_log(path_to_log=log_path):
    def get_log_path(primary_function):
        def new_function(*args, **kwargs):
            with open(path_to_log, 'a', encoding='utf-8') as f:
                f.write(f'\n{"_" * len(path_to_log)}\n')
                f.write(f'Дата и время вызова функции: {now.strftime("%d.%m.%Y %H:%M")}\n')
                f.write(f'Вызвана функция {primary_function.__name__} с аргументами {args}\n')
                result = primary_function(*args, **kwargs)
                f.write(f'Результат: {str(result)}\n')
                f.write(f'{path_to_log}\n')
                f.write(f'{"_" * len(path_to_log)}\n')
            return result

        return new_function

    return get_log_path


# задание 3
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



