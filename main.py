from threading import Thread
from time import time
import numpy as np


def sqr_mx(size: int) -> np.ndarray:
    return np.random.rand(size, size)


def multiply_matrices(first: np.ndarray, second: np.ndarray) -> type(None):
    [[sum(a * b for a, b in zip(row_a, row_b)) for row_b in zip(*second)] for row_a in first]


def mul_n_times_threading(n: int) -> type(None):
    start_time = time()
    threads = []
    [threads.append(Thread(target=multiply_matrices, args=(sqr_mx(99), sqr_mx(99),))) for _ in range(n)]
    [t.start() for t in threads]    # запускаємо усі потоки
    [t.join() for t in threads]     # чекаємо на завершення усіх потоків
    print("mul_n_times_threading time: %.4f seconds" % (time() - start_time))


mul_n_times_threading(4)
