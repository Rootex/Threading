import threading
from queue import Queue
import time

lock = threading.Lock()

total = 0

def sq(number):
    return number**2


def summation(num):
    time.sleep(0.1)
    global total
    with lock:
        total += sq(num)
    print(threading.current_thread().name, total)


def threader():
    while True:
        x = q.get()
        summation(x)
        q.task_done()

q = Queue()

for i in range(20):
    q.put(i)

start = time.time()
for i in range(20):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

q.join()

print("Our job took: ", time.time() - start)
star = time.time()

print(sum([i**2 for i in range(20)]))

print("Non parallel took: ", time.time() - star)