import requests


def get_jssm():
    session1 = requests.session()
    session1.headers = {
        "Host": "match.yuanrenxue.cn",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua-platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://match.yuanrenxue.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://match.yuanrenxue.cn/match/3",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }
    cookies = {
        "sessionid": "s7l5a71usa4px4kmxr62t3dgzsno9d1g",
        "qpfccr": "true",
        "no-alert3": "true",
    }
    url = "https://match.yuanrenxue.cn/jssm"
    response = session1.post(url, cookies=cookies)
    print(response.text)
    print(response)


def get_data(page):
    session2 = requests.session()
    session2.headers = {
        "Host": "match.yuanrenxue.cn",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua-platform": '"Windows"',
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://match.yuanrenxue.cn/match/3",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }
    cookies = {
        "sessionid": "s7l5a71usa4px4kmxr62t3dgzsno9d1g",
        "qpfccr": "true",
        "no-alert3": "true",
    }
    url = "https://match.yuanrenxue.cn/api/match/3"
    params = {"page": str(page)}
    response = session2.get(url, cookies=cookies, params=params)
    print(response)
    print(response.json())
    data_list = response.json()["data"]
    for data in data_list:
        result_list.append(data["value"])


if __name__ == "__main__":
    result_list = []
    for page in range(1, 6):
        get_jssm()
        get_data(page)
    print(max(result_list, key=result_list.count))
