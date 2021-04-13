import threading
from threading import Thread
import time
import datetime
from multiprocessing import Pool, Process
from concurrent.futures import ProcessPoolExecutor
import os

# 1. Write the method that return the number of threads currently in execution.
# Also prepare the method that will be executed with threads and run during the first method counting.


def foo():
    for x in range(10):
        print(f"The first is running...{x}")
        time.sleep(0.2)


def foo2():
    for x in range(10):
        print(f"The second is running...{x}")
        time.sleep(0.5)


def thread_count():
    print(f"Count of threads: {threading.activeCount()}")


threading1 = Thread(target=foo)
threading2 = Thread(target=foo2)

threading1.start()
threading2.start()
while threading.activeCount() > 1:
    thread_count()
    time.sleep(0.7)
threading1.join()
threading2.join()

# 2. Print current date by using 2 threads.
# 1. Define a subclass using Thread class.
# 2. Instantiate the subclass and trigger the thread.


class CurrentDate(Thread):

    def run(self) -> None:
        print(f"Today is {datetime.date.today()}")
        time.sleep(1)


thread1 = CurrentDate()
thread2 = CurrentDate()
thread1.start()
thread2.start()
thread1.join()
thread2.join()


# 3. Use Pool.apply() to get the row wise common items in list_a and list_b.
list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]


def func():
    return [set(a).intersection(b) for a, b in zip(list_a, list_b)]


with Pool() as pool:
    print(f"{pool.apply(func)}")


# 4. Divide the work between 2 methods: print_cube that returns the cube of number and print_square
# that returns the square of number. These two methods should be executed by using 2 different processes.

def print_cube(num):
    name = os.getpid()
    print(f"Current process: {name}")
    print(f"{num} in cube is {num ** 3}")
    return num ** 3


def print_square(numb):
    name = os.getpid()
    print(f"Current process: {name}")
    print(f"{numb} in square is {numb ** 2}")
    return numb ** 2


with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(print_cube)
    pool.submit(print_square)

    process1 = Process(name="Process1", target=print_cube, args=(5,))
    process2 = Process(name="Process2", target=print_square, args=(5,))
    process1.start()
    process2.start()
