"""
测试使用请求头和不使用请求头时，返回的差异
"""
import urllib.request
import urllib.parse

url = 'https://www.baidu.com/'

response = urllib.request.urlopen(url=url)
print(response.read().decode('utf-8'))

"""
实际未测试到效果
"""