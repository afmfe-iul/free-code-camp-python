from multiprocessing import Process, Value, Array, Lock, Queue
import time


def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


def add_100_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()
    shared_number = Value("i", 0)
    shared_array = Array("d", [0.0, 100.0, 200.0])

    print(f"Number at the beginning is {shared_number.value}")
    print(f"Array at the beginning is {shared_array[:]}")

    p1 = Process(target=add_100, args=(shared_number, lock1))
    p2 = Process(target=add_100, args=(shared_number, lock1))
    p3 = Process(target=add_100_array, args=(shared_array, lock2))
    p4 = Process(target=add_100_array, args=(shared_array, lock2))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print(f"Number at end is {shared_number.value}")
    print(f"Array at end is {shared_array[:]}")


def square(numbers, queue):
    for i in numbers:
        queue.put(i * i)


def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1 * i)


if __name__ == "__main__":
    q = Queue()
    numbers = range(1, 6)

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())
