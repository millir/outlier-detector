import math
from util import get_datetime

class DataStream:
    def __init__(self) -> None:        
        self.n = 0
        self.mean = 0.0
        self.variance = 0.0
        self.M2 = 0.0

    def add_point(self, date, price):
        self.date = get_datetime(date)
        self.timestamp = self.date.timestamp()
        self.price = float(price)

    def update_calculations(self):
        self.n += 1
        delta1 = self.price - self.mean
        self.mean += delta1 / self.n
        delta2 = self.price - self.mean
        self.M2 += delta1 * delta2
        if self.n < 2:
            self.variance = float('nan')
        else:
            self.variance = self.M2 / (self.n - 1)  # sample variance

    def check_if_outlier(self, z_scores=3):
        if not - z_scores <= (self.price - self.mean) / math.sqrt(self.variance) <= z_scores:
            outlier = (self.date, self.price)
            return outlier
