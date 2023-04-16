import json
import asyncio
import aiohttp

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, text
from sqlalchemy.dialects.mysql import CHAR, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


async def get_mes_data(barcode, operation):
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
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, data=json.dumps(payload), headers=headers, timeout=30) as re:
                if re.status != 200:
                    print("数据获取失败！")
                    return None
                return json.loads(await re.text())["data"]["records"]
    except aiohttp.ClientError:
        return None


async def get_301(barcode, c):
    copy_code = {
        "301": {
            "P001": "P001",
            "P002": "P002",
            "P003": "P003",
            "P004": "P004",
            "P005": "P005",
        }
    }
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


Base = declarative_base()
metadata = Base.metadata


class C301(Base):
    __tablename__ = 'c301'
    __table_args__ = {'comment': '电芯活化工序表'}

    id = Column(BigInteger, primary_key=True)
    bar_code = Column(VARCHAR(24), nullable=False, index=True, comment='电芯条码')
    P001 = Column(DateTime, index=True, comment='活化开始时间')
    P002 = Column(DateTime, comment='活化结束时间')
    P003 = Column(VARCHAR(24), comment='活化时间/min\\r\\n')
    P004 = Column(VARCHAR(24), comment='托盘号')
    P005 = Column(VARCHAR(24), comment='库位号')
    P006 = Column(Integer, comment='位置号')
    P007 = Column(VARCHAR(24), comment='批次号')

