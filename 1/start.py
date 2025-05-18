import requests
import execjs
cookies = {
    'sessionid': '4yi61gunppho4axuu0hmehb1rzwxpnp9',
    'Hm_lvt_c99546cf032aaa5a679230de9a95c7db': '1746892969',
    'HMACCOUNT': '379EFDE2923B06DE',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'tk': '4135379688337894796',
    'Hm_lvt_9bcbda9cbf86757998a2339a0437208e': '1746892982',
    'Hm_lpvt_9bcbda9cbf86757998a2339a0437208e': '1746892982',
    'Hm_lpvt_c99546cf032aaa5a679230de9a95c7db': '1746895393',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/1',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=4yi61gunppho4axuu0hmehb1rzwxpnp9; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1746892969; HMACCOUNT=379EFDE2923B06DE; qpfccr=true; no-alert3=true; tk=4135379688337894796; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1746892982; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1746892982; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1746895393',
}

sum=0
for page in range(1,6):
    m=execjs.compile(open(r'1\m_value.js', 'r', encoding='utf-8').read()).call('get_m')
    params = {
        'page': str(page),
        'm': m,
    }
    response = requests.get('https://match.yuanrenxue.cn/api/match/1', params=params, cookies=cookies, headers=headers)
    print(response.status_code)
    print(response.json())
    data_list = response.json()['data']
    for data in data_list:
        sum+=data['value']
print(sum)