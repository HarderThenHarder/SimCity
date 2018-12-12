"""
@author: P_k_y
"""
import time
import threading


class Timer:
    def __init__(self):
        self._second = 0
        self._minute = 0
        self._hour = 0

    def start(self):
        while True:
            time.sleep(1)
            self._second += 1
            if self._second == 60:
                self._minute += 1
                self._second = 0
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
            if self._hour == 60:
                self._hour = 0

    def get_second(self):
        return self._second

    def get_minute(self):
        return self._minute

    def get_hour(self):
        return self._hour


def print_time(timer):
    while True:
        print(timer.get_second())
        time.sleep(1)


def main():
    timer = Timer()
    t1 = threading.Thread(target=timer.start)
    t1.start()

    t2 = threading.Thread(target=print_time, args=(timer, ))
    t2.start()


if __name__ == '__main__':
    main()



