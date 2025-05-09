import requests
import base64 
cookies = {
    'sessionid': 'lxtlh0f7mxs0eiuyir9znqyimuznsj9g',
    'Hm_lvt_9bcbda9cbf86757998a2339a0437208e': '1746771782',
    'HMACCOUNT': 'FF67817707386E22',
    'Hm_lvt_c99546cf032aaa5a679230de9a95c7db': '1746771782',
    'tk': '4135379688337894796',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'Hm_lpvt_9bcbda9cbf86757998a2339a0437208e': '1746783987',
    'Hm_lpvt_c99546cf032aaa5a679230de9a95c7db': '1746783998',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/12',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=lxtlh0f7mxs0eiuyir9znqyimuznsj9g; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1746771782; HMACCOUNT=FF67817707386E22; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1746771782; tk=4135379688337894796; qpfccr=true; no-alert3=true; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1746783987; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1746783998',
}

sum=0
for page in range(1,6):
    original_string = f'yuanrenxue{page}'
    encoded_bytes = base64.b64encode(original_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')

    params = {
        'page': str(page),
        'm': encoded_string,
    }

    response = requests.get('https://match.yuanrenxue.cn/api/match/12', params=params, cookies=cookies, headers=headers)
    print(response.status_code)
    print(response.json())
    data_list = response.json()['data']
    for data in data_list:
        sum+=data['value']
print(sum)