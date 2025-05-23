import requests
import execjs

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/6",
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
    "sessionid": "im21angoa28woyzyogx8l99rkooh22us",
    "qpfccr": "true",
    "no-alert3": "true",
    "tk": "-2982228765806358039",
}
url = "https://match.yuanrenxue.cn/api/match/6"
file = open(r"6/m_value.js", "r", encoding="utf-8").read()
ctx = execjs.compile(file)
sum = 0
q = ""
for page in range(1, 6):
    key = ctx.call("get_m", page)
    q += f"1-{key[1]}|"

    params = {"page": str(page), "m": key[0], "q": f"{page}-{key[1]}|"}

    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response)
    print(response.json())
    data_list = response.json()["data"]
    for i in data_list:
        sum += i["value"] + i["value"] * 8 + i["value"] * 15
print(sum)
