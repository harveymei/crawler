import urllib.request
url = 'https://www.python.org'
# 设置网络超时为0.1秒，将返回错误
response = urllib.request.urlopen(url=url, timeout=0.1)
print(response.read().decode('utf-8'))
