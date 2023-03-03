import time
# from random import randrange
import random


def calculate_valid_timestamp(timestamp, i_count):
    try:
        return timestamp + (i_count - timestamp % i_count)
    except ZeroDivisionError:
        return timestamp


def generate_timestamp(sentences):
    now = int(time.time() * 1000)
    # return now
    i_count = 1
    for sentence in [item['text'] for item in sentences]:
        i_count += sentence.count("i")

    return calculate_valid_timestamp(now, i_count)


def generate_id():
    return int(1e4) * round(1e4 * random.random())
    # return randrange(1_000_000, 100_000_000)
