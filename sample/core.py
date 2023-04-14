from constant.mes_codes import operations
from reptile.search import save_many
from reptile.url_request import get_mes_barcode


def save_p75_data(start_time, end_time):
    for i in operations:
        barcodes = get_mes_barcode("W401", i, start_time, end_time)
        save_many(barcodes, i)


def save_p64_data(start_time, end_time):
    for i in operations:
        barcodes = get_mes_barcode("W402", i, start_time, end_time)
        save_many(barcodes, i)
