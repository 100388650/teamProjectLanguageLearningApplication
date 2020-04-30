import datetime
import math
import random
import itertools
import threading

time_fmt = "%Y-%m-%d"


# card part
class card:
    def __init__(self, last, first, time, repetition=0, interval=1, easiness=2.5):
        self.last = last
        self.first = first

    self.easiness = easiness
    self.time = time.replace(second=0, microsecond=0)
    self.interval = interval
    self.repetition = repetition


def new(self):
    return self.repetition == 0

    def repeat(self, quality, time):
        assert quality >= 0 and quality <= 5

    self.easiness = max(1.3, self.easiness + 0.1 - (5.0 - quality) * (0.08 + (5.0 - quality) * 0.02))
    if quality < 3:
        self.repetition = 0
    else:
        self.repetition += 1
    if self.repetition == 1:
        self.interval = 1
    elif self.repetition == 2:
        self.interval = 6
    else:
        self.interval *= self.easiness
    self.time = time


# repeat part
from threading import Timer
from datetime import datetime


class Timer(object):
    def __init__(self, time_interval, start_time):
        self.timer = None
        self.time_interval = time_interval
        self.start_time = start_time

    def start(self):
        time_interval = self.time_interval - (datetime.now().timestamp() - self.__start_time.timestamp())

    print(time_interval)
    self.timer.start()

    def cancel(self):


self.timer.cancel()
self.timer = None


class AA:
    def card


# card dealing part that im not sure how to do

if __name__ == "__main__":
    aa = AA()
    start = datetime.now().replace(minute=3, second=0, microsecond=0)
    tmr = Timer(start, 60 * 60, aa.card)
    tmr.start()
    tmr.cancel()
