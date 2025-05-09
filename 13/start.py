import requests

cookies = {
    'Hm_lvt_c99546cf032aaa5a679230de9a95c7db': '1746771782',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'sessionid': 's7l5a71usa4px4kmxr62t3dgzsno9d1g',
    'tk': '4135379688337894796',
    'Hm_lvt_9bcbda9cbf86757998a2339a0437208e': '1746771782',
    'Hm_lpvt_9bcbda9cbf86757998a2339a0437208e': '1746802592',
    'HMACCOUNT': '8EF8021399BDBCDC',
    'yuanrenxue_cookie': '1746803182|lPhY51kSeIhxPgcoMKf54MVPx3OMBvPmrdravndOmrCjtZwEmdYHQUZBORCCJ6N4tIGNMP6H60YV0Xkuoyn36SKJ6h2Mt9OK3giZQarz4ZN4CrWAXDIuVKqywXGNbpPvPmLK35',
    'Hm_lpvt_c99546cf032aaa5a679230de9a95c7db': '1746803184',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://match.yuanrenxue.cn/match/13',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response1 = requests.get('https://match.yuanrenxue.cn/match/13', cookies=cookies, headers=headers)
data = response1.text.split('<script>')[1].split('</script>')[0]

# 简化合并后的代码
import re
result = ''.join(re.findall(r'\((.*?)\)', data)).replace(" ", "").replace("'", "")
# 删除前缀 'yuanrenxue_cookie='
result = result.replace('yuanrenxue_cookie=', '')
print(result)
cookies['yuanrenxue_cookie']= result
sum = 0
for page in range(1, 6):
    if page == 1:
        url = 'https://match.yuanrenxue.cn/api/match/13'
    else:
        url = f'https://match.yuanrenxue.cn/api/match/13?page={page}'

    response2 = requests.get(url, cookies=cookies, headers=headers)
    print(response2.status_code)
    print(response2.json())
    data_list = response2.json()['data']
    for data in data_list:
        sum+=data['value']
print(sum)