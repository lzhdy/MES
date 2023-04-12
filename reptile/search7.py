import asyncio
import json
import pandas as pd
import aiohttp
import sys
import concurrent.futures
import retrying

@retrying.retry(wait_fixed=5000, stop_max_attempt_number=3)
async def get_mes_data(session, semaphore, barcode, op_name, param_id):
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
        "lotName": "00CAB3231373",
        "workShopSection": "C3",
        "virtualId": barcode,
        "processOperationName": op_name
    }
    async with semaphore:
        try:
            async with session.post(url, data=json.dumps(payload), timeout=30) as resp:
                if resp.status != 200:
                    raise IOError("HTTP Error " + str(resp.status) + ":" + barcode)
                return await resp.text(), barcode, op_name, param_id
        except (aiohttp.ClientError, asyncio.TimeoutError, Exception) as e:
            print("查询失败！条码：{} 参数：{} 原因：{}".format(barcode, param_id, str(e)))
            return None, barcode, op_name, param_id



def extract_data(jsons, barcode, op_name, param_id):
    if jsons is None:
        return {
            barcode: "无数据"
        }
    data = json.loads(jsons)["data"]
    records = data["records"]
    for item in records:
        if item["parameterId"] == param_id:
            if item["parameterValue"]:
                return {
                    op_name + "/" + param_id: {
                        barcode: item["parameterValue"]
                    } 
                }
            else:
                continue
    return {
        op_name + "/" + param_id: {
            barcode: "无数据"
        }
    }
    

def dict_update(raw, new):
    dict_update_iter(raw, new)
    dict_add(raw, new)


def dict_update_iter(raw, new):
    for key in raw:
        if key not in new.keys():
            continue
        if isinstance(raw[key], dict) and isinstance(new[key], dict):
            dict_update(raw[key], new[key])
        else:
            raw[key] = new[key]


def dict_add(raw, new):
    update_dict = {}
    for key in new:
        if key not in raw.keys():
            update_dict[key] = new[key]

    raw.update(update_dict)


async def main():
    path_file = input("请输入文件：")
    file_data = pd.read_excel(path_file, sheet_name=0, header=0)

    # 获取需要查那些数据
    excel_header = file_data.columns.tolist()
    # 获取需要查询数据的电芯条码
    excel_barcode = file_data[excel_header[0]].values.tolist()
    excel_header.pop(0)

    # construct query list
    search_list = []
    for eh in excel_header:
        params = eh.split('/')
        if len(params) != 2 or params[0][0] != "C" or params[1][0] != "P":
            print("表头：" + eh + "格式错误！")
            break
        for eb in excel_barcode:
            search_list.append((eb, *params))
    
    headers = {
        "user-agent": "Mozilla/5. (Windows NT 10.; Win64; x64) AppleWebKit"
                      "/537.36 (KHTML, like Gecko) Chrome/86..424.198 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        'Host': '10.231.31.40:8081',
    }
            
# create session pool
    async with aiohttp.ClientSession(headers=headers) as session:
        # execute query
        search_result = {}
        semaphore = asyncio.Semaphore(3000)
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            tasks = [get_mes_data(session, semaphore, *sl) for sl in search_list]
            responses = await asyncio.gather(*tasks)
            for resp, barcode, op_name, param_id in responses:
                result_dict = extract_data(resp, barcode, op_name, param_id)
                print(result_dict)
                dict_update(search_result, result_dict)

    # save result to Excel file
    result_data = {"电芯条码": excel_barcode}
    for eh in excel_header:
        line_data = []
        for eb in excel_barcode:
            line_data.append(search_result[eh][eb])
        result_data.update({
            eh: line_data
        })

    df = pd.DataFrame(result_data)
    path = path_file.split("\\")
    path.pop()
    file_name = "\\".join(path) + "\\result_data.xlsx"
    df.to_excel(file_name, index=False)

    print("已完成数据查询！")
    input("Press Enter to exit...")
    sys.exit()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
