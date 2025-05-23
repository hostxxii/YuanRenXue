import subprocess
import json
import requests

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
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "sessionid": "im21angoa28woyzyogx8l99rkooh22us",
    "qpfccr": "true",
    "no-alert3": "true",
    "tk": "-2982228765806358039"
}
url = "https://match.yuanrenxue.cn/api/match/6"

# 调用 node 执行 js 文件，并获取 console.log 输出
result = subprocess.run([
    'node', '6/m_value.js'
], capture_output=True, text=True)

# 解析 console.log 输出的内容
output = result.stdout.strip()
try:
    # 假设输出为类似 ["加密串", 时间戳]
    key = json.loads(output.replace("'", '"'))
except Exception as e:
    print('解析输出失败:', e)
    key = None



# 构造请求参数
if key:
    params = {
        "page": "1",
        "m": key[0],
        "q": f'1-{key[1]}|'
    }
    
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print('response:', response)
    try:
        print('response.json:', response.json())
    except Exception as e:
        print('解析返回JSON失败:', e)
else:
    print('未获取到有效参数')   