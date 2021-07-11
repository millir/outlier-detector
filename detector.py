import logging
from data_stream import DataStream
from util import read_csv, write_csv

log = logging.getLogger(__name__)

if __name__ == '__main__':
    data_points = read_csv('data/full_data.csv')
    write_csv('data/clean_data.csv', 'Date', 'Price')
    write_csv('data/outlier_data.csv', 'Date', 'Price')

    stream = DataStream(window_size=25)

    for data in data_points:
        date=data['Date']
        price=data['Price']

        stream.add_point(date, price)
        stream.update_calculations()
        outlier = stream.check_if_outlier(z_scores=3)
        
        if outlier:
            log.info(outlier)
            write_csv('data/outlier_data.csv', date, price)

        else:
            write_csv('data/clean_data.csv', date, price)
