import time


def send():
    for i in range(10000):
        pass


start = time.time()
send()
end = time.time()

duration = end - start
print(duration)
