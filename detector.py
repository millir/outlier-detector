from util import read_csv, write_csv
from data_stream import DataStream
import logging

log = logging.getLogger(__name__)

if __name__ == '__main__':
    data_points = read_csv('data/Outliers.csv')
    write_csv('data/clean_data.csv', 'Date', 'Price')
    
    stream = DataStream()

    for data in data_points:
        date=data['Date']
        price=data['Price']

        stream.add_point(date, price)
        stream.update_calculations()
        outlier = stream.check_if_outlier(number_of_standard_deviations=3)
        if outlier:
            log.info(outlier)
        else:
            write_csv('data/clean_data.csv', date, price)
