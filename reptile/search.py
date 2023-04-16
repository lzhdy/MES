from constant.mes_codes import copy_code
from reptile.url_request import get_mes_data


async def get_301(barcode, c):
    respond = await get_mes_data(barcode, "C170")
    c.bar_code = barcode
    c.P007 = barcode[14:17]
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


async def get_302(barcode, lists):
    respond = await get_mes_data(barcode, "C180")
    batch = barcode[14:17]
    p001 = None
    p002 = None
    p003 = None
    if respond:
        for i in respond:
            id = i["parameterId"]
            for (k, v) in copy_code["302"].items():
                if id == k:
                    if v == "P001":
                        p001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        p002 = i["parameterValue"]
                        continue
                    if v == "P003":
                        p003 = i["parameterValue"]
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
    result = []
    for i in lists:
        if i.P004:
            i.bar_code = barcode
            i.P001 = p001
            i.P002 = p002
            i.P003 = p003
            i.P015 = batch
            result.append(i)
    return result


async def get_303(barcode, c):
    respond = await get_mes_data(barcode, "C190")
    c.bar_code = barcode
    c.P006 = barcode[14:17]
    start_date = None
    end_time = None
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
                        start_date = i["parameterValue"]
                    if v == "P005" and k == "P007":
                        end_time = i["parameterValue"]
        if start_date is not None and end_time is not None:
            c.P005 = start_date + " " + end_time

    return c


async def get_304(barcode, c):
    respond = await get_mes_data(barcode, "C200")
    c.bar_code = barcode
    c.P007 = barcode[14:17]
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


async def get_305(barcode, c):
    respond = await get_mes_data(barcode, "C210")
    c.bar_code = barcode
    c.P007 = barcode[14:17]
    start_date = None
    end_time = None
    if respond:
        for i in respond:
            for (k, v) in copy_code["305"].items():
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
                        start_date = i["parameterValue"]
                    if v == "P005" and k == "P007":
                        end_time = i["parameterValue"]
                    if v == "P006":
                        c.P006 = i["parameterValue"]
        if start_date is not None and end_time is not None:
            c.P005 = start_date + " " + end_time

    return c


async def get_306(barcode, c):
    respond = await get_mes_data(barcode, "C220")
    c.bar_code = barcode
    c.P037 = barcode[14:17]
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


async def get_307(barcode, lists):
    respond = await get_mes_data(barcode, "C230")
    batch = barcode[14:17]
    p001 = None
    p002 = None
    p013 = None
    p014 = None
    p015 = None
    p016 = None
    if respond:
        for i in respond:
            id = i["parameterId"]
            for (k, v) in copy_code["307"].items():
                if id == k:
                    if v == "P001":
                        p001 = i["parameterValue"]
                        continue
                    if v == "P002":
                        p002 = i["parameterValue"]
                        continue
                    if v == "P013":
                        p013 = i["parameterValue"]
                        continue
                    if v == "P014":
                        p014 = i["parameterValue"]
                        continue
                    if v == "P015":
                        p015 = i["parameterValue"]
                        continue
                    if v == "P016":
                        p016 = i["parameterValue"]
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
    result = []
    for i in lists:
        if i.P003:
            i.bar_code = barcode
            i.P001 = p001
            i.P002 = p002
            i.P013 = p013
            i.P014 = p014
            i.P015 = p015
            i.P016 = p016
            i.P017 = batch
            result.append(i)
    return result


async def get_308(barcode, c):
    respond = await get_mes_data(barcode, "C235")
    c.bar_code = barcode
    c.P008 = barcode[14:17]
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


async def get_309(barcode, c):
    respond = await get_mes_data(barcode, "C240")
    c.bar_code = barcode
    c.P007 = barcode[14:17]
    start_date = None
    end_time = None
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
                        start_date = i["parameterValue"]
                        continue
                    if v == "P005" and k == "P007":
                        end_time = i["parameterValue"]
        if start_date is not None and end_time is not None:
            c.P005 = start_date + " " + end_time

    return c


async def get_310(barcode, c):
    respond = await get_mes_data(barcode, "C245")
    c.bar_code = barcode
    c.P008 = barcode[14:17]
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


async def get_311(barcode, c):
    respond = await get_mes_data(barcode, "C250")
    c.bar_code = barcode
    c.P008 = barcode[14:17]
    start_date = None
    end_time = None
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
                        start_date = i["parameterValue"]
                        continue
                    if v == "P005" and k == "P007":
                        end_time = i["parameterValue"]
        if start_date is not None and end_time is not None:
            c.P005 = start_date + " " + end_time

    return c


async def get_312(barcode, c):
    respond = await get_mes_data(barcode, "C255")
    c.bar_code = barcode
    c.P008 = barcode[14:17]
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


async def get_313(barcode, c):
    respond = await get_mes_data(barcode, "C260")
    c.bar_code = barcode
    c.P009 = barcode[14:17]
    start_date = None
    end_time = None
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
                        start_date = i["parameterValue"]
                        continue
                    if v == "P005" and k == "P007":
                        end_time = i["parameterValue"]
        if start_date is not None and end_time is not None:
            c.P005 = start_date + " " + end_time

    return c


async def get_314(barcode, c):
    respond =await get_mes_data(barcode, "C270")
    c.bar_code = barcode
    c.P011 = barcode[14:17]
    start_date = None
    end_time = None
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
                        start_date = i["parameterValue"]
                        continue
                    if v == "P004" and k == "P005":
                        end_time = i["parameterValue"]
        if start_date is not None and end_time is not None:
            c.P004 = start_date + " " + end_time

    return c


async def get_315(barcode, c):
    respond = await get_mes_data(barcode, "C280")
    c.bar_code = barcode
    c.P015 = barcode[14:17]
    start_date = None
    end_time = None
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
                        start_date = i["parameterValue"]
                        continue
                    if v == "P013" and k == "P011":
                        end_time = i["parameterValue"]
        if start_date is not None and end_time is not None:
            c.P013 = start_date + " " + end_time

    return c
