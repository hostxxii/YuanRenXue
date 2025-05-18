# 使用pywasm 0.4.8的API
import pywasm
import time
import random
import os
import requests

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/15",
    "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}
cookies = {
    "sessionid": "s7l5a71usa4px4kmxr62t3dgzsno9d1g",
    "no-alert3": "true",
    "m": "571222ff8df31f0c979872e581657677|1747488389000",
}
url = "https://match.yuanrenxue.cn/api/match/15"

sum = 0
for page in range(1, 6):
    random_number = random.randint(1, 50)
    t1 = int(time.time()) // 2
    t2 = t1 - random_number
    module = pywasm.load(os.path.join("15", "main.wasm"))
    key = module.exec("encode", [t1, t2])
    result = str(key) + "|" + str(t1) + "|" + str(t2)
    # print(type(result))
    # print(result)

    params = {"m": result, "page": str(page)}
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    print(response.text)
    print(response)
    json_data = response.json()
    for i in json_data["data"]:
        sum += i["value"]
print(sum)
