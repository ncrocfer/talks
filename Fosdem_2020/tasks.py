import random
from celery import Celery


app = Celery("tasks", broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/1")


@app.task
def get_rand():
    return random.randint(1, 10)


@app.task
def get_sum(numbers):
    return sum(numbers)

