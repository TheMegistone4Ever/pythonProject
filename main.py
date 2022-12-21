from threading import Thread
from time import time
import numpy as np
from multiprocessing import Pool
from multiprocessing import freeze_support
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def gen_sqr_mx(size: int) -> np.ndarray:    # створення матриці size x size та заповнення випадковими значеннями
    return np.random.rand(size, size)


def sqr_mx(mx: np.ndarray) -> type(None):   # множення матриць лінійним способом
    [[sum(a * b for a, b in zip(row_a, row_b)) for row_b in zip(*mx)] for row_a in mx]


def mul_n_times_threading(n: int) -> type(None):
    start_time = time()
    threads = []
    [threads.append(Thread(target=sqr_mx, args=(gen_sqr_mx(99),))) for _ in range(n)]
    [t.start() for t in threads]    # запускаємо усі потоки
    [t.join() for t in threads]     # чекаємо на завершення усіх потоків
    print("mul_n_times_threading time: %.4f seconds..." % (time() - start_time))


def mul_n_times_thread_pool_executor(n: int) -> type(None):
    start_time = time()
    with ThreadPoolExecutor(max_workers=n) as tpe:  # запускаємо усі потоки та чекаємо на завершення усіх потоків
        [tpe.submit(sqr_mx, gen_sqr_mx(99)) for _ in range(n)]
    print("mul_n_times_thread_pool_executor time: %.4f seconds..." % (time() - start_time))


def mul_n_times_multiprocessing(n: int) -> type(None):
    start_time = time()
    with Pool(processes=n) as pool:     # створення пула з n процесами та чекаємо на завершення усіх
        pool.map(sqr_mx, [gen_sqr_mx(99) for _ in range(n)])
    print("mul_n_times_multiprocessing time: %.4f seconds..." % (time() - start_time))


def mul_n_times_process_pool_executor(n: int) -> type(None):
    start_time = time()
    with ProcessPoolExecutor(max_workers=n) as ppe:     # створення пула з n процесами та чекаємо на завершення усіх
        [ppe.submit(sqr_mx, gen_sqr_mx(99)) for _ in range(n)]
    print("mul_n_times_process_pool_executor time: %.4f seconds..." % (time() - start_time))


def main() -> int:
    mul_n_times_threading(n=4)
    mul_n_times_thread_pool_executor(n=4)
    freeze_support()
    mul_n_times_multiprocessing(n=4)
    mul_n_times_process_pool_executor(n=4)
    return 0


if __name__ == '__main__':
    main()
