from constant.mes_codes import copy_code, operations
from db.mysql_conn_session import session
from tables.models import C301, BatteryMark, C302, C303, C304, C305, C306, C307, C308, C309, C310, C311, C312, \
    C313, C314, C315, D301, D302, D303, D304, D305, D306, D307, D308, D309, D310, D311, D312, D313, D314, D315
from reptile.url_request import get_mes_data


def save_many(barcodes, operation):
    """
    批量存储各工序电芯数据
    :param barcodes: 一段时间某个工序的条码
    :param operation: 工序号
    :return:
    """
    lists = []
    if operation == operations[0]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_301(barcode, D301()))
            elif model == "75":
                lists.append(get_301(barcode, C301()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[1]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists: list[D302] = [D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302(),
                                     D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302()]
                for i in get_302(barcode, lists):
                    lists.append(i)
            elif model == "75":
                lists: list[C302] = [C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302(),
                                     C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302()]
                for i in get_302(barcode, lists):
                    lists.append(i)
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[2]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_303(barcode, D303()))
            elif model == "75":
                lists.append(get_303(barcode, C303()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[3]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_304(barcode, D304()))
            elif model == "75":
                lists.append(get_304(barcode, C304()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[4]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_305(barcode, D305()))
            elif model == "75":
                lists.append(get_305(barcode, C305()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[5]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_306(barcode, D306()))
            elif model == "75":
                lists.append(get_306(barcode, C306()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[6]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists: list[D307] = [D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307(),
                                     D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307()]
                for i in get_307(barcode, lists):
                    lists.append(i)
            elif model == "75":
                lists: list[C307] = [C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307(),
                                     C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307()]
                for i in get_307(barcode, lists):
                    lists.append(i)
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[7]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_308(barcode, D308()))
            elif model == "75":
                lists.append(get_308(barcode, C308()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[8]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_309(barcode, D309()))
            elif model == "75":
                lists.append(get_309(barcode, C309()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[9]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_310(barcode, D310()))
            elif model == "75":
                lists.append(get_310(barcode, C310()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[10]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_311(barcode, D311()))
            elif model == "75":
                lists.append(get_311(barcode, C311()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[11]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_312(barcode, D312()))
            elif model == "75":
                lists.append(get_312(barcode, C312()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[12]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_313(barcode, D313()))
            elif model == "75":
                lists.append(get_313(barcode, C313()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[13]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_314(barcode, D314()))
            elif model == "75":
                lists.append(get_314(barcode, C314()))
            else:
                print("Invalid barcode: " + barcode)
    if operation == operations[14]:
        for barcode in barcodes:
            model = barcode[10:12]
            if model == "64":
                lists.append(get_315(barcode, D315()))
            elif model == "75":
                lists.append(get_315(barcode, C315()))
            else:
                print("Invalid barcode: " + barcode)

    session.add_all(lists)
    session.commit()
    session.close()


def get_301(barcode, c):
    respond = get_mes_data(barcode, "C170")
    c.bar_code = barcode
    c.P007 = barcode[14:17]
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["301"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P005":
                        c.P005 = i["parameterValue"]

    return c


def get_302(barcode, lists):
    respond = get_mes_data(barcode, "C180")
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    batch = barcode[14:17]
    p001 = ""
    p002 = ""
    p003 = ""
    if respond:
        for i in respond:
            id = i["parameterId"]
            for (k, v) in copy_code["302"].items():
                if id == k:
                    if v == "P001":
                        p001 = p001 + i["parameterValue"]
                        continue
                    if v == "P002":
                        p002 = p002 + i["parameterValue"]
                        continue
                    if v == "P003":
                        p003 = p003 + i["parameterValue"]
                        continue
                if len(id) > 4:
                    ids = id.split("_")
                    if ids[0] == k:
                        if v == "P004":
                            lists[int(ids[1])].P004 = i["parameterValue"]
                            continue
                        if v == "P005":
                            lists[int(ids[1])].P005 = i["parameterValue"]
                            continue
                        if v == "P006":
                            lists[int(ids[1])].P006 = i["parameterValue"]
                            continue
                        if v == "P007":
                            lists[int(ids[1])].P007 = i["parameterValue"]
                            continue
                        if v == "P008":
                            lists[int(ids[1])].P008 = i["parameterValue"]
                            continue
                        if v == "P009":
                            lists[int(ids[1])].P009 = i["parameterValue"]
                            continue
                        if v == "P010":
                            lists[int(ids[1])].P010 = i["parameterValue"]
                            continue
                        if v == "P011":
                            lists[int(ids[1])].P011 = i["parameterValue"]
                            continue
                        if v == "P012":
                            lists[int(ids[1])].P012 = i["parameterValue"]
                            continue
                        if v == "P013":
                            lists[int(ids[1])].P013 = i["parameterValue"]
                            continue
                        if v == "P014":
                            lists[int(ids[1])].P014 = i["parameterValue"]
    for i in lists:
        if i.P004:
            i.bar_code = barcode
            i.P001 = p001
            i.P002 = p002
            i.P003 = p003
            i.P015 = batch
            if battery_mark:
                i.mark = battery_mark
        else:
            lists.remove(i)
    return lists


def get_303(barcode, c):
    respond = get_mes_data(barcode, "C190")
    c.bar_code = barcode
    c.P006 = barcode[14:17]
    start_date = ""
    end_time = ""
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["303"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P005" and k == "P006":
                        start_date = start_date + i["parameterValue"]
                    if v == "P005" and k == "P007":
                        end_time = end_time + i["parameterValue"]

        c.P005 = start_date + " " + end_time

    return c


def get_304(barcode, c):
    respond = get_mes_data(barcode, "C200")
    c.bar_code = barcode
    c.P007 = barcode[14:17]
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["304"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P005":
                        c.P005 = i["parameterValue"]

    return c


def get_305(barcode, c):
    respond = get_mes_data(barcode, "C210")
    c.bar_code = barcode
    c.P007 = barcode[14:17]
    start_date = ""
    end_time = ""
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["305"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P005" and k == "P006":
                        start_date = start_date + i["parameterValue"]
                    if v == "P005" and k == "P007":
                        end_time = end_time + i["parameterValue"]
                    if v == "P006":
                        c.P006 = i["parameterValue"]

        c.P005 = start_date + " " + end_time

    return c


def get_306(barcode, c):
    respond = get_mes_data(barcode, "C220")
    c.bar_code = barcode
    c.P037 = barcode[14:17]
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["306"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P005":
                        c.P005 = i["parameterValue"]
                        continue
                    if v == "P006":
                        c.P006 = i["parameterValue"]
                        continue
                    if v == "P007":
                        c.P007 = i["parameterValue"]
                        continue
                    if v == "P008":
                        c.P008 = i["parameterValue"]
                        continue
                    if v == "P009":
                        c.P009 = i["parameterValue"]
                        continue
                    if v == "P010":
                        c.P010 = i["parameterValue"]
                        continue
                    if v == "P011":
                        c.P011 = i["parameterValue"]
                        continue
                    if v == "P012":
                        c.P012 = i["parameterValue"]
                        continue
                    if v == "P013":
                        c.P013 = i["parameterValue"]
                        continue
                    if v == "P014":
                        c.P014 = i["parameterValue"]
                        continue
                    if v == "P015":
                        c.P015 = i["parameterValue"]
                        continue
                    if v == "P016":
                        c.P016 = i["parameterValue"]
                        continue
                    if v == "P017":
                        c.P017 = i["parameterValue"]
                        continue
                    if v == "P018":
                        c.P018 = i["parameterValue"]
                        continue
                    if v == "P019":
                        c.P019 = i["parameterValue"]
                        continue
                    if v == "P020":
                        c.P020 = i["parameterValue"]
                        continue
                    if v == "P021":
                        c.P021 = i["parameterValue"]
                        continue
                    if v == "P022":
                        c.P022 = i["parameterValue"]
                        continue
                    if v == "P023":
                        c.P023 = i["parameterValue"]
                        continue
                    if v == "P024":
                        c.P024 = i["parameterValue"]
                        continue
                    if v == "P025":
                        c.P025 = i["parameterValue"]
                        continue
                    if v == "P026":
                        c.P026 = i["parameterValue"]
                        continue
                    if v == "P027":
                        c.P027 = i["parameterValue"]
                        continue
                    if v == "P028":
                        c.P028 = i["parameterValue"]
                        continue
                    if v == "P029":
                        c.P029 = i["parameterValue"]
                        continue
                    if v == "P030":
                        c.P030 = i["parameterValue"]
                        continue
                    if v == "P031":
                        c.P031 = i["parameterValue"]
                        continue
                    if v == "P032":
                        c.P032 = i["parameterValue"]
                        continue
                    if v == "P033":
                        c.P033 = i["parameterValue"]
                        continue
                    if v == "P034":
                        c.P034 = i["parameterValue"]
                        continue
                    if v == "P035":
                        c.P035 = i["parameterValue"]
                        continue
                    if v == "P036":
                        c.P036 = i["parameterValue"]

    return c


def get_307(barcode, lists):
    respond = get_mes_data(barcode, "C230")
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    batch = barcode[14:17]
    p001 = ""
    p002 = ""
    p013 = ""
    p014 = ""
    p015 = ""
    p016 = ""
    if respond:
        for i in respond:
            id = i["parameterId"]
            for (k, v) in copy_code["307"].items():
                if id == k:
                    if v == "P001":
                        p001 = p001 + i["parameterValue"]
                        continue
                    if v == "P002":
                        p002 = p002 + i["parameterValue"]
                        continue
                    if v == "P013":
                        p013 = p013 + i["parameterValue"]
                        continue
                    if v == "P014":
                        p014 = p014 + i["parameterValue"]
                        continue
                    if v == "P015":
                        p015 = p015 + i["parameterValue"]
                        continue
                    if v == "P016":
                        p016 = p016 + i["parameterValue"]
                        continue
                if len(id) > 4:
                    ids = id.split("_")
                    if ids[0] == k:
                        if v == "P003":
                            lists[int(ids[1])].P003 = i["parameterValue"]
                            continue
                        if v == "P004":
                            lists[int(ids[1])].P004 = i["parameterValue"]
                            continue
                        if v == "P005":
                            lists[int(ids[1])].P005 = i["parameterValue"]
                            continue
                        if v == "P006":
                            lists[int(ids[1])].P006 = i["parameterValue"]
                            continue
                        if v == "P007":
                            lists[int(ids[1])].P007 = i["parameterValue"]
                            continue
                        if v == "P008":
                            lists[int(ids[1])].P008 = i["parameterValue"]
                            continue
                        if v == "P009":
                            lists[int(ids[1])].P009 = i["parameterValue"]
                            continue
                        if v == "P010":
                            lists[int(ids[1])].P010 = i["parameterValue"]
                            continue
                        if v == "P011":
                            lists[int(ids[1])].P011 = i["parameterValue"]
                            continue
                        if v == "P012":
                            lists[int(ids[1])].P012 = i["parameterValue"]

    for i in lists:
        if i.P003:
            i.bar_code = barcode
            i.P001 = p001
            i.P002 = p002
            i.P017 = batch
            if battery_mark:
                i.mark = battery_mark
        else:
            lists.remove(i)
    return lists


def get_308(barcode, c):
    respond = get_mes_data(barcode, "C235")
    c.bar_code = barcode
    c.P008 = barcode[14:17]
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["308"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P005":
                        c.P005 = i["parameterValue"]
                        continue
                    if v == "P006":
                        c.P006 = i["parameterValue"]
    return c


def get_309(barcode, c):
    respond = get_mes_data(barcode, "C240")
    c.bar_code = barcode
    c.P006 = barcode[14:17]
    start_date = ""
    end_time = ""
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["309"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P005" and k == "P006":
                        start_date = start_date + i["parameterValue"]
                        continue
                    if v == "P005" and k == "P007":
                        end_time = end_time + i["parameterValue"]

        c.P005 = start_date + " " + end_time

    return c


def get_310(barcode, c):
    respond = get_mes_data(barcode, "C245")
    c.bar_code = barcode
    c.P008 = barcode[14:17]
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["310"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P005":
                        c.P005 = i["parameterValue"]
                        continue
                    if v == "P006":
                        c.P006 = i["parameterValue"]
    return c


def get_311(barcode, c):
    respond = get_mes_data(barcode, "C250")
    c.bar_code = barcode
    c.P008 = barcode[14:17]
    start_date = ""
    end_time = ""
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["311"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P007":
                        c.P007 = i["parameterValue"]
                        continue
                    if v == "P005" and k == "P006":
                        start_date = start_date + i["parameterValue"]
                        continue
                    if v == "P005" and k == "P007":
                        end_time = end_time + i["parameterValue"]

        c.P005 = start_date + " " + end_time

    return c


def get_312(barcode, c):
    respond = get_mes_data(barcode, "C255")
    c.bar_code = barcode
    c.P008 = barcode[14:17]
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["312"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P005":
                        c.P005 = i["parameterValue"]
                        continue
                    if v == "P006":
                        c.P006 = i["parameterValue"]
    return c


def get_313(barcode, c):
    respond = get_mes_data(barcode, "C260")
    c.bar_code = barcode
    c.P009 = barcode[14:17]
    start_date = ""
    end_time = ""
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["313"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P007":
                        c.P007 = i["parameterValue"]
                        continue
                    if v == "P008":
                        c.P008 = i["parameterValue"]
                        continue
                    if v == "P005" and k == "P006":
                        start_date = start_date + i["parameterValue"]
                        continue
                    if v == "P005" and k == "P007":
                        end_time = end_time + i["parameterValue"]

        c.P005 = start_date + " " + end_time

    return c


def get_314(barcode, c):
    respond = get_mes_data(barcode, "C270")
    c.bar_code = barcode
    c.P011 = barcode[14:17]
    start_date = ""
    end_time = ""
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["314"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        c.P002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P005":
                        c.P005 = i["parameterValue"]
                        continue
                    if v == "P006":
                        c.P006 = i["parameterValue"]
                        continue
                    if v == "P007":
                        c.P007 = i["parameterValue"]
                        continue
                    if v == "P008":
                        c.P008 = i["parameterValue"]
                        continue
                    if v == "P009":
                        c.P009 = i["parameterValue"]
                        continue
                    if v == "P010":
                        c.P010 = i["parameterValue"]
                        continue
                    if v == "P004" and k == "P004":
                        start_date = start_date + i["parameterValue"]
                        continue
                    if v == "P004" and k == "P005":
                        end_time = end_time + i["parameterValue"]

        c.P004 = start_date + " " + end_time

    return c


def get_315(barcode, c):
    respond = get_mes_data(barcode, "C280")
    c.bar_code = barcode
    c.P015 = barcode[14:17]
    start_date = ""
    end_time = ""
    battery_mark = session.query(BatteryMark).filter(BatteryMark.bar_code == barcode).first()
    if battery_mark:
        c.mark = battery_mark.mark
    if respond:
        for i in respond:
            for (k, v) in copy_code["315"].items():
                if i["parameterId"] == k:
                    if v == "P001":
                        c.P001 = i["parameterValue"]
                        continue
                    if v == "P003":
                        c.P003 = i["parameterValue"]
                        continue
                    if v == "P004":
                        c.P004 = i["parameterValue"]
                        continue
                    if v == "P005":
                        c.P005 = i["parameterValue"]
                        continue
                    if v == "P006":
                        c.P006 = i["parameterValue"]
                        continue
                    if v == "P007":
                        c.P007 = i["parameterValue"]
                        continue
                    if v == "P008":
                        c.P008 = i["parameterValue"]
                        continue
                    if v == "P009":
                        c.P009 = i["parameterValue"]
                        continue
                    if v == "P010":
                        c.P010 = i["parameterValue"]
                        continue
                    if v == "P011":
                        c.P011 = i["parameterValue"]
                        continue
                    if v == "P012":
                        c.P012 = i["parameterValue"]
                        continue
                    if v == "P014":
                        c.P014 = i["parameterValue"]
                        continue
                    if v == "P013" and k == "P010":
                        start_date = start_date + i["parameterValue"]
                        continue
                    if v == "P013" and k == "P011":
                        end_time = end_time + i["parameterValue"]

        c.P013 = start_date + " " + end_time

    return c
