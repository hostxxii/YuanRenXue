import urllib3
import ssl
import requests

# 设置为与 Chrome 浏览器类似的加密套件
chrome_ciphers = (
    'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:'
    'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:'
    'ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:'
    'ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:'
    'AES256-GCM-SHA384:AES128-SHA:AES256-SHA'
)

# 替换默认加密套件
urllib3.util.ssl_.DEFAULT_CIPHERS = chrome_ciphers

# 禁用警告信息
urllib3.disable_warnings()

# 确保使用最新的 TLS 协议版本
context = ssl.create_default_context()
context.set_ciphers(chrome_ciphers)
context.minimum_version = ssl.TLSVersion.TLSv1_2  # 设置最低使用TLS 1.2版本

# 在 requests 中使用这个上下文
session = requests.Session()
adapter = requests.adapters.HTTPAdapter()
session.mount('https://', adapter)

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/19",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "sessionid": "s7l5a71usa4px4kmxr62t3dgzsno9d1g",
}
url = "https://match.yuanrenxue.cn/api/match/19"
params = {
    "page": '1'
}

try:
    response = session.get(url, headers=headers, cookies=cookies, params=params, verify=False)
    print(response.text)
    print(response.status_code)
except Exception as e:
    print(f"发生错误: {e}")
