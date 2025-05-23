import requests
import time

t = int(time.time()) * 1000
sum = 0
for page in range(1, 6):
    arg1 = f"{page}|{t}"
    params1 = {"arg1": arg1}
    url1 = "http://127.0.0.1:5612/business/invoke?group=match20&action=get_sign"
    response1 = requests.get(url=url1, params=params1)
    json1 = response1.json()
    sign = json1["data"]

    session = requests.session()
    session.headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://match.yuanrenxue.cn/match/20",
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
    }
    url = "https://match.yuanrenxue.cn/api/match/20"

    params = {"page": str(page), "sign": sign, "t": str(t)}
    response = requests.get(url, cookies=cookies, params=params)

    print(response)
    print(response.text)
    data_list = response.json()["data"]
    for data in data_list:
        sum += data["value"]
print(sum)
