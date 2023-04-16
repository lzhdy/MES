from constant.mes_codes import operations
from db.mysql_conn_session import session
from reptile.search import get_301, get_302, get_303, get_304, get_305, get_306, get_307, get_308, get_309, \
    get_310, get_311, get_312, get_313, get_314, get_315
from reptile.url_request import get_mes_barcode
from tables.models import D301, C301, D302, C302, D303, C303, D304, C304, D305, C305, D306, C306, \
    D307, C307, D308, C308, D309, C309, D310, C310, D311, C311, D312, C312, D313, C313, D314, C314, D315, C315


async def save_p75_data(start_time, end_time):
    for i in operations:
        barcodes = get_mes_barcode("W401", i, start_time, end_time)
        if len(barcodes) != 0:
            await save_many(barcodes, i)


async def save_p64_data(start_time, end_time):
    for i in operations:
        barcodes = get_mes_barcode("W402", i, start_time, end_time)
        if len(barcodes) != 0:
            await save_many(barcodes, i)


async def save_many(barcodes, operation):
    """
    批量存储各工序电芯数据
    :param barcodes: 一段时间某个工序的条码
    :param operation: 工序号
    :return:
    """
    result = None
    if operation == operations[0]:
        result = await save_301(barcodes)
    elif operation == operations[1]:
        result = await save_302(barcodes)
    elif operation == operations[2]:
        result = await save_303(barcodes)
    elif operation == operations[3]:
        result = await save_304(barcodes)
    elif operation == operations[4]:
        result = await save_305(barcodes)
    elif operation == operations[5]:
        result = await save_306(barcodes)
    elif operation == operations[6]:
        result = await save_307(barcodes)
    elif operation == operations[7]:
        result = await save_308(barcodes)
    elif operation == operations[8]:
        result = await save_309(barcodes)
    elif operation == operations[9]:
        result = await save_310(barcodes)
    elif operation == operations[10]:
        result = await save_311(barcodes)
    elif operation == operations[11]:
        result = await save_312(barcodes)
    elif operation == operations[12]:
        result = await save_313(barcodes)
    elif operation == operations[13]:
        result = await save_314(barcodes)
    elif operation == operations[14]:
        result = await save_315(barcodes)

    try:
        session.add_all(result)
        session.commit()
        session.close()
    except Exception as e:
        session.rollback()
        raise e


async def save_301(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_301(barcode, D301())
            result.append(bar)
        elif model == "75":
            bar = await get_301(barcode, C301())
            result.append(bar)
        else:
            print("Invalid barcode: " + barcode)
    return result


async def save_302(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            lists: list[D302] = [D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302(),
                                 D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302(), D302()]
            list_302 = await get_302(barcode, lists)
            result = result + list_302

        elif model == "75":
            lists: list[C302] = [C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302(),
                                 C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302(), C302()]
            list_302 = await get_302(barcode, lists)
            result = result + list_302
        else:
            print("Invalid barcode: " + barcode)

    return result


async def save_303(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_303(barcode, D303())
            result.append(bar)

        elif model == "75":
            bar = await get_303(barcode, C303())
            result.append(bar)
        else:
            print("Invalid barcode: " + barcode)

    return result


async def save_304(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_304(barcode, D304())
            result.append(bar)
        elif model == "75":
            bar = await get_304(barcode, C304())
            result.append(bar)
        else:
            print("Invalid barcode: " + barcode)
    return result


async def save_305(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_305(barcode, D305())
            result.append(bar)
        elif model == "75":
            bar = await get_305(barcode, C305())
            result.append(bar)
        else:
            print("Invalid barcode: " + barcode)

    return result


async def save_306(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_306(barcode, D306())
            result.append(bar)
        elif model == "75":
            bar = await get_306(barcode, C306())
            result.append(bar)
        else:
            print("Invalid barcode: " + barcode)
    return result


async def save_307(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            lists: list[D307] = [D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307(),
                                 D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307(), D307()]

            list_307 = await get_307(barcode, lists)
            result = result + list_307
        elif model == "75":
            lists: list[C307] = [C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307(),
                                 C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307(), C307()]
            list_307 = await get_307(barcode, lists)
            result = result + list_307

        else:
            print("Invalid barcode: " + barcode)

    return result


async def save_308(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_308(barcode, D308())
            result.append(bar)
        elif model == "75":
            bar = await get_308(barcode, C308())
            result.append(bar)
        else:
            print("Invalid barcode: " + barcode)
    return result


async def save_309(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_309(barcode, D309())
            result.append(bar)

        elif model == "75":
            bar = await get_309(barcode, C309())
            result.append(bar)

        else:
            print("Invalid barcode: " + barcode)
    return result


async def save_310(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_310(barcode, D310())
            result.append(bar)
        elif model == "75":
            bar = await get_310(barcode, C310())
            result.append(bar)
        else:
            print("Invalid barcode: " + barcode)
    return result


async def save_311(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_311(barcode, D311())
            result.append(bar)

        elif model == "75":
            bar = await get_311(barcode, C311())
            result.append(bar)

        else:
            print("Invalid barcode: " + barcode)
    return result


async def save_312(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_312(barcode, D312())
            result.append(bar)
        elif model == "75":
            bar = await get_312(barcode, C312())
            result.append(bar)
        else:
            print("Invalid barcode: " + barcode)
    return result


async def save_313(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_313(barcode, D313())
            result.append(bar)
        elif model == "75":
            bar = await get_313(barcode, C313())
            result.append(bar)

        else:
            print("Invalid barcode: " + barcode)

    return result


async def save_314(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_314(barcode, D314())
            result.append(bar)

        elif model == "75":
            bar = await get_314(barcode, C314())
            result.append(bar)
        else:
            print("Invalid barcode: " + barcode)
    return result


async def save_315(barcodes):
    result = []
    for barcode in barcodes:
        print("正在查询条码：" + barcode + "的数据")
        model = barcode[10:12]
        if model == "64":
            bar = await get_315(barcode, D315())
            result.append(bar)

        elif model == "75":
            bar = await get_315(barcode, C315())
            result.append(bar)

        else:
            print("Invalid barcode: " + barcode)

    return result
