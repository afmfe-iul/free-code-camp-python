from threading import Thread, Lock, current_thread
import time

database_value = 0

############### Multi-threading with locks ##############
#########################################################

"""
def increase(lock: Lock):
    global database_value

    # Passing the lock prevents race conditions
    with lock:  # this context manager acquires and releases the lock for us
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":
    print("starting value", database_value)

    lock = Lock()

    t1 = Thread(target=increase, args=(lock,))
    t2 = Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("ending value", database_value)

    print("End main")
"""

############### Multi-threading with queue ##############
#########################################################

from queue import Queue


def worker(q: Queue, lock):
    while True:
        value = q.get()  # Thread safe, will block until there's something in the queue
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()  # Thread safe


if __name__ == "__main__":
    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        # Daemon thread = background thread that will die when the main thread dies
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)  # Thread safe

    # When this stops blocking the main thread dies and all the daemon threads die too
    q.join()

    print("End main")
