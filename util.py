import csv
import numpy as np

def read_csv(file):
    with open(file, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        outliers = list(csv_reader)
        return outliers