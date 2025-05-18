import requests
import execjs

# 将文件读取和编译操作移到循环外部
file_data = open(r'5\RM4hZBv0dDon443M_value.js', 'r', encoding='utf-8').read()
ctx = execjs.compile(file_data)  # 编译一次

for page in range(1, 6):
    # 调用已编译的上下文中的函数
    all_params = ctx.call('generateAllParams')
    key = all_params['rm_cookie_val']
    m_cookie = all_params['m_cookie_val']
    m_param = all_params['m_param_val']
    f_param = all_params['f_param_val']

    # print("RM4hZBv0dDon443M (key):", key)
    # print("m (cookie):", m_cookie)
    # print("m (param):", m_param)
    # print("f (param):", f_param)

    cookies = {
        'sessionid': 's7l5a71usa4px4kmxr62t3dgzsno9d1g',  # 你的 sessionid
        'm': m_cookie,
        'RM4hZBv0dDon443M': key,
        # ... 其他 cookies
    }
    headers = {
        # ... headers
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://match.yuanrenxue.cn/match/5',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    params_data = {
        'page': str(page),
        'm': m_param,
        'f': f_param,
    }
    response = requests.get('https://match.yuanrenxue.cn/api/match/5', params=params_data, cookies=cookies, headers=headers)
    print(f"Page: {page}, Status: {response.status_code}")
    print(response.text)
