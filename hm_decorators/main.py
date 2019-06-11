import random
from datetime import datetime
from pprint import pprint


def log(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('data/log.txt', 'a', encoding='utf8')as f:
            time_start = datetime.isoformat(datetime.now(), sep=' ')
            f.write(
                f"{time_start} function name: {old_function.__name__} attributes: {args}{kwargs} result: {result}\n")
        return result
    return new_function


@log
def random_list(size):
    random_list = [random.random() for _ in range(size)]
    return random_list


if __name__ == '__main__':
    random_list(100)


