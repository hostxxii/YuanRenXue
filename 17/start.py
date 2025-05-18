import httpx
import time


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/17",
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
    "no-alert3": "true"
}
url = "https://match.yuanrenxue.cn/api/match/17"

with httpx.Client(http2=True, headers=headers, cookies=cookies) as client:
    sum=0
    for page_num in range(1, 6):
        params = {
            "page": str(page_num)
        }
        print(f"Requesting page: {page_num}")
        response = client.get(url, params=params)
        print(f"Status Code for page {page_num}: {response.status_code}")
        print(f"Response for page {page_num}:")
        print(response.text)
        json_data = response.json()
        for value in json_data['data']:
            sum+=value['value']
    print(sum)
        

