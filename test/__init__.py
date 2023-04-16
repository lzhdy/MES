import asyncio
import datetime

from reptile.url_request import get_mes_barcode
from sample.core import save_many, save_p75_data


def hour_range(bgn, end):
    fmt = '%Y-%m-%d %H:%M:%S'
    begin = datetime.datetime.strptime(bgn, fmt)
    end = datetime.datetime.strptime(end, fmt)
    delta = datetime.timedelta(hours=1)

    interval = int((end - begin).days * 24 + (end - begin).seconds / 60 / 60) + 1

    return [begin + delta * i for i in range(0, interval, 1)]


if __name__ == '__main__':
    # barcodes = get_mes_barcode("W401", "C280", "2023-03-01 12:00:00", "2023-03-01 13:00:00")
    #
    # if len(barcodes) != 0:
    #     asyncio.run(save_many(barcodes, "C280"))

    times = hour_range("2023-03-01 13:00:00", "2023-03-02 08:00:00")
    for i in range(19):
        print(i)
        print(times[i].strftime('%Y-%m-%d %H:%M:%S'), times[i+1].strftime('%Y-%m-%d %H:%M:%S'))
        asyncio.run(save_p75_data(times[i].strftime('%Y-%m-%d %H:%M:%S'), times[i+1].strftime('%Y-%m-%d %H:%M:%S')))


