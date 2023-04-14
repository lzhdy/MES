from datetime import datetime

if __name__ == '__main__':
    value = '2017-10-7 22:03:02'
    datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    print(datetime.strptime(value, '%Y-%m-%d %H:%M:%S'))
    bar = "0K3CE002YN64DGD3E1102135"
    print(len(bar))
    print(bar[10:12])