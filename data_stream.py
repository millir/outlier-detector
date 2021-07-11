import math
from statistics import variance
from util import get_datetime

class DataStream:
    def __init__(self, window_size=25) -> None:     
        self.mean = 0.0
        self.variance = 0.0

        assert window_size != 0, "Window size must not be zero!"
        self.size = window_size
        self.window = []
        self.sum = 0

    def add_point(self, date, price):
        self.date = get_datetime(date)
        self.timestamp = self.date.timestamp()
        self.price = float(price)

    def update_calculations(self):
        self.sum += self.price
        self.window.append(self.price)
        if len(self.window) > self.size:
            self.sum -= self.window.pop(0)
        
        self.mean = self.sum / len(self.window)
        if len(self.window) > 1:
            self.variance = variance(self.window)

    def check_if_outlier(self, z_scores=3):
        assert 0 < z_scores < 5, "Z score must be between 1-4!"  # 68–95–99.7 rule
        outlier = (self.date, self.price)

        if self.variance == 0:
            return None
        if not - z_scores <= (self.price - self.mean) / math.sqrt(self.variance) <= z_scores:
            return outlier
