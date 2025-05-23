import os
import requests
import KNN
import base64
import numpy as np

# 获取当前脚本所在的绝对路径，用于拼接依赖文件的绝对路径，防止路径错误
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 读取召唤师名称
names_path = os.path.join(BASE_DIR, '../summoner_names.txt')
with open(names_path, 'r', encoding='utf-8') as f:
    names = [line.strip() for line in f.readlines() if line.strip()]

numbers = []
# 循环爬取第1页到第5页的数据
for page in range(1, 6):
    cookies = {'sessionid': 's7l5a71usa4px4kmxr62t3dgzsno9d1g'}
    headers = {'User-Agent': 'yuanrenxue.project'}
    # 字体编码与数字的映射字典（训练数据）
    data_dict = {
        '.notdef': '.',   # 字体文件中的特殊符号
        'unif619': '5',
        'unif129': '9',
        'unib649': '4',
        'unia375': '0',
        'unia185': '8',
        'unic142': '6',
        'unie314': '2',
        'unie184': '3',
        'unif974': '7',
        'unic148': '1',
    }
    # 创建一个requests会话对象
    session = requests.Session()
    # 构建请求URL
    url = f'http://match.yuanrenxue.com/api/match/7?page={page}'
    # 发送GET请求
    response = session.get(url, cookies=cookies, headers=headers)
    # 解析返回的JSON数据
    result_json = response.json()
    # 从响应中提取字体文件（Base64编码），并保存到本地
    font = result_json['woff']
    font2_path = os.path.join(BASE_DIR, 'font2.woff')   # 目标字体文件路径
    train_path = os.path.join(BASE_DIR, 'train.woff')   # 训练字体文件路径
    with open(font2_path, 'wb') as f:
        f.write(base64.b64decode(font))
    # 使用KNN算法对比训练字体和目标字体，获取真实映射表
    really_table = KNN.knn(train_path, data_dict, font2_path)
    # 遍历返回的数据，解析出真实数字
    for i in result_json['data']:
        number = ''
        # 每个数字是由多个字体编码拼接而成
        for j in i['value'].split(' '):
            if j:
                # 将形如'&#x9ea3'的编码转换为'uni9ea3'格式，然后查找真实数字
                number += really_table[j.replace('&#x', 'uni')]
        numbers.append(int(number))

# 映射名称和数字
name_number_pairs = list(zip(names, numbers))
# 找出数字最大的名称
max_name, max_number = max(name_number_pairs, key=lambda x: x[1])

print("所有名称与数字的对应关系：")
for name, num in name_number_pairs:
    print(f"{name}: {num}")
print(f"\n数字最大的名称是：{max_name}，分数为：{max_number}")
