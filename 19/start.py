import requests


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
    "no-alert3": "true",
    "RM4hZBv0dDon443M": "XpRz9t6Vu2rd3d58MkrnQd4+/YuJXdO6PS2IIZFDPMXIp+XFbrI19lSLWU9P+dGHFEozBEEsltXKaym59PpyqK0Bwiq9fk0abSSZh077O/japLweBH+KdkEHhsrh4+EsLcWx9gGD0Kjy66QLDtLY2sq2SBdw976bdUTqCZBU5DLrEfDBa89nfrwFPdZCkrGHt09T0XM1Rj0jNiHMAIci1LvjAbWgVjj5e67w+PFqIDM=",
    "mz": "TW96aWxsYSxOZXRzY2FwZSw1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNi4wLjAuMCBTYWZhcmkvNTM3LjM2LFtvYmplY3QgTmV0d29ya0luZm9ybWF0aW9uXSx0cnVlLCxbb2JqZWN0IEdlb2xvY2F0aW9uXSwxNix6aC1DTix6aC1DTixlbiwwLFtvYmplY3QgTWVkaWFDYXBhYmlsaXRpZXNdLFtvYmplY3QgTWVkaWFTZXNzaW9uXSxbb2JqZWN0IE1pbWVUeXBlQXJyYXldLHRydWUsW29iamVjdCBQZXJtaXNzaW9uc10sV2luMzIsW29iamVjdCBQbHVnaW5BcnJheV0sR2Vja28sMjAwMzAxMDcsW29iamVjdCBVc2VyQWN0aXZhdGlvbl0sTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNi4wLjAuMCBTYWZhcmkvNTM3LjM2LEdvb2dsZSBJbmMuLCxbb2JqZWN0IERlcHJlY2F0ZWRTdG9yYWdlUXVvdGFdLFtvYmplY3QgRGVwcmVjYXRlZFN0b3JhZ2VRdW90YV0sNzYwLDAsMCwxNDIzLDI0LDgwMCxbb2JqZWN0IFNjcmVlbk9yaWVudGF0aW9uXSwyNCwxNDIzLFtvYmplY3QgRE9NU3RyaW5nTGlzdF0sZnVuY3Rpb24gYXNzaWduKCkgeyBbbmF0aXZlIGNvZGVdIH0sLG1hdGNoLnl1YW5yZW54dWUuY24sbWF0Y2gueXVhbnJlbnh1ZS5jbixodHRwczovL21hdGNoLnl1YW5yZW54dWUuY24vbWF0Y2gvMTQsaHR0cHM6Ly9tYXRjaC55dWFucmVueHVlLmNuLC9tYXRjaC8xNCwsaHR0cHM6LGZ1bmN0aW9uIHJlbG9hZCgpIHsgW25hdGl2ZSBjb2RlXSB9LGZ1bmN0aW9uIHJlcGxhY2UoKSB7IFtuYXRpdmUgY29kZV0gfSwsZnVuY3Rpb24gdG9TdHJpbmcoKSB7IFtuYXRpdmUgY29kZV0gfSxmdW5jdGlvbiB2YWx1ZU9mKCkgeyBbbmF0aXZlIGNvZGVdIH0=",
    "m": "c3bd0f9a555ab9f112995c38d9daf24c|1747671301000"
}
url = "https://match.yuanrenxue.cn/api/match/19"
params = {
    "page": "3"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)