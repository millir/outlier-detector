import csv
from datetime import datetime
import numpy as np
import os.path


def read_csv(file):
    with open(file, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data_points = list(csv_reader)
        return data_points

def get_datetime(date_string):
    return datetime.strptime(date_string, '%d/%m/%Y')

def write_csv(file, date, price):
    with open(file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((date,price))
