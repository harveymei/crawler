import urllib.request
import urllib.parse
url = 'https://www.httpbin.org/post'
# 创建请求体数据，使用urlencode()方法进行编码,将字典类型转为字节类型
data = bytes(urllib.parse.urlencode({'hello': 'python'}), encoding='utf-8')
# 使用urlopen()方法发送请求，在使用data参数传递请求体数据，使用POST请求
response = urllib.request.urlopen(url=url, data=data)
# 获取响应体数据并使用utf-8解码
print(response.read().decode('utf-8'))

"""
Pycharm返回结果

/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-2.py 
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "hello": "python"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "12", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "www.httpbin.org", 
    "User-Agent": "Python-urllib/3.12", 
    "X-Amzn-Trace-Id": "Root=1-67d2f325-4ef2672715ed820e3edc8d12"
  }, 
  "json": null, 
  "origin": "31.94.36.29", 
  "url": "https://www.httpbin.org/post"
}


Process finished with exit code 0
"""