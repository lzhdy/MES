import json

import requests
from requests import ReadTimeout


def get_mes_barcode(area, operation, start_time, end_time) -> set:
    """
    从mes上获取一段时间内的所有条码
    :param area: 生产线号：W401/W402
    :param operation: 工序号
    :param start_time: 开始时间
    :param end_time: 结束时间
    :return: 返回记录，条码：lotName，工序号：processOperationName
    """
    url = 'http://10.231.31.40:8081/api/mes-twork-boot/productionReportForHour/queryDetail'
    headers = {
        "user-agent": "Mozilla/5. (Windows NT 10.; Win64; x64) AppleWebKit"
                      "/537.36 (KHTML, like Gecko) Chrome/86..424.198 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        'Host': '10.231.31.40:8081',
    }
    payload = {
        "pageNo": 1,
        "pageSize": 10,
        "limit": 10,
        "areaName": area,
        "processOperationName": operation,
        "operateValue": "HourComplete",
        "startTime": start_time,
        "endTime": end_time
    }
    re = requests.post(url=url, data=json.dumps(payload), headers=headers)
    if re.status_code != 200:
        print("条码获取失败！")
        return None
    payload["limit"] = json.loads(re.text)["data"]["total"]
    re = requests.post(url=url, data=json.dumps(payload), headers=headers)
    if re.status_code != 200:
        print("条码获取失败！")
        return None
    bar = json.loads(re.text)["data"]["records"]
    barcode = set()
    for i in bar:
        bar = i["lotName"]
        if len(bar) == 24:
            barcode.add(bar)
    return barcode


def get_mes_data(barcode, operation):
    """
    从mes获取工艺参数
    :param barcode: 电芯条码
    :param operation: 工序号
    :return: 工艺参数记录，参数id：parameterId，参数值：parameterValue，参数描述：parameterDesc，
    """
    url = 'http://10.231.31.40:8081/api/mes-twork-boot/processParam/product/queryPageList'
    headers = {
        "user-agent": "Mozilla/5. (Windows NT 10.; Win64; x64) AppleWebKit"
                      "/537.36 (KHTML, like Gecko) Chrome/86..424.198 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        'Host': '10.231.31.40:8081',
    }
    payload = {
        "pageNo": 1,
        "limit": 300,
        "lot24Name": barcode,
        "lotName": "00D134067110",
        "workShopSection": "C3",
        "processOperationName": operation
    }
    try:
        re = requests.post(url=url, data=json.dumps(payload), headers=headers, timeout=30)
        if re.status_code != 200:
            print("数据获取失败！")
            return None
        return json.loads(re.text)["data"]["records"]
    except ReadTimeout:
        return None

