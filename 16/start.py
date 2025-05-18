import requests
import execjs


cookies = {
    "sessionid": "s7l5a71usa4px4kmxr62t3dgzsno9d1g",
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1746771782,1747038360",
    "no-alert3": "true",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1746771782,1747038360",
    "m": "f35237bbfe7dd24042bcf774482eef56",
    "RM4hZBv0dDon443M": "DrB0shWdXOtEyqpR9JUW3Ki2P/gwfhnbRtU5gSh3+zbf/DTlW1TC7WBhQISPCJsxD3/SQtQ7VgI3b/G6P/UmNJ0EPGUGrLR9Vpiq8+2GOeP90RgebkjzW1urlVi2XAQyZ8oqsqZ4yaES0VG+wB6nr7V4LL/MXjWh/4axPxnGNf2ZHoutIlR5wLG3YoQy/+b+Cmx8DiuSspe5EyOl3YFf0uoQpoAlyeJldk9cBPkFitY=",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1747203485",
    "HMACCOUNT": "F699FB7A9C9BEE8B",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1747205706",
}

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/16",
    "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    # 'cookie': 'sessionid=s7l5a71usa4px4kmxr62t3dgzsno9d1g; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1746771782,1747038360; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1746771782,1747038360; m=f35237bbfe7dd24042bcf774482eef56; RM4hZBv0dDon443M=DrB0shWdXOtEyqpR9JUW3Ki2P/gwfhnbRtU5gSh3+zbf/DTlW1TC7WBhQISPCJsxD3/SQtQ7VgI3b/G6P/UmNJ0EPGUGrLR9Vpiq8+2GOeP90RgebkjzW1urlVi2XAQyZ8oqsqZ4yaES0VG+wB6nr7V4LL/MXjWh/4axPxnGNf2ZHoutIlR5wLG3YoQy/+b+Cmx8DiuSspe5EyOl3YFf0uoQpoAlyeJldk9cBPkFitY=; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1747203485; HMACCOUNT=F699FB7A9C9BEE8B; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1747205706',
}
file_data = open(r"16\m_value.js", "r", encoding="utf-8").read()
file_exe = execjs.compile(file_data)
result = 0
for page in range(1, 6):
    key_data = file_exe.call("get_params")
    params = {
        "page": str(page),
        "m": key_data["m"],
        "t": key_data["t"],
    }
    response = requests.get(
        "https://match.yuanrenxue.cn/api/match/16",
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response.json())
    jason_data = response.json()
    for i in jason_data["data"]:
        result += i["value"]
print(result)
