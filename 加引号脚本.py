# 读取文本内容并转换为字典
import json

# 读取原始文本文件
with open(r'笔记.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 创建字典
result = {}
for line in lines:
    if ':' in line:
        key, value = map(str.strip, line.split(':', 1))
        result[key] = value

# 写入JSON格式
with open('加引号脚本处理结果.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print("转换完成！结果已保存到处理结果.json")