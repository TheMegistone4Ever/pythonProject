from threading import Thread
from time import time
import numpy as np
from multiprocessing import Pool
from multiprocessing import freeze_support
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def sqr_mx(size: int) -> np.ndarray:
    return np.random.rand(size, size)


def sqr_mxs(mx: np.ndarray) -> type(None):
    [[sum(a * b for a, b in zip(row_a, row_b)) for row_b in zip(*mx)] for row_a in mx]


def mul_n_times_threading(n: int) -> type(None):
    start_time = time()
    threads = []
    [threads.append(Thread(target=sqr_mxs, args=(sqr_mx(99), ))) for _ in range(n)]
    [t.start() for t in threads]    # запускаємо усі потоки
    [t.join() for t in threads]     # чекаємо на завершення усіх потоків
    print("mul_n_times_threading time: %.4f seconds..." % (time() - start_time))


def mul_n_times_multiprocessing(n: int) -> type(None):
    start_time = time()
    with Pool(processes=n) as pool:
        pool.map(sqr_mxs, [sqr_mx(99) for _ in range(n)])
    print("mul_n_times_multiprocessing time: %.4f seconds..." % (time() - start_time))


def mul_n_times_thread_pool_executor(n: int) -> type(None):
    start_time = time()
    with ThreadPoolExecutor(max_workers=n) as tpe:
        [tpe.submit(sqr_mxs, sqr_mx(99)) for _ in range(n)]
    print("mul_n_times_thread_pool_executor time: %.4f seconds..." % (time() - start_time))


def mul_n_times_process_pool_executor(n: int) -> type(None):
    start_time = time()
    with ProcessPoolExecutor(max_workers=n) as ppe:
        [ppe.submit(sqr_mxs, sqr_mx(99)) for _ in range(n)]
    print("mul_n_times_process_pool_executor time: %.4f seconds..." % (time() - start_time))


if __name__ == '__main__':
    mul_n_times_threading(4)
    mul_n_times_thread_pool_executor(4)
    freeze_support()
    mul_n_times_multiprocessing(4)
    mul_n_times_process_pool_executor(4)
