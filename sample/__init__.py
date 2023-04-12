from reptile.search import save_many
from reptile.url_request import get_mes_barcode

if __name__ == '__main__':
    barcodes = get_mes_barcode("W401", "C170", "2023-04-01 08:00:00", "2023-04-01 08:59:59")
    save_many(barcodes, "C170")
