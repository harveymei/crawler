import urllib.request
import urllib.parse
# 用于解析url的模块

url = 'https://www.httpbin.org/post'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# 构建请求头信息，字典类型
data = bytes(urllib.parse.urlencode({'hello': 'python'}), encoding='utf-8')
# 对文本内容进行编码并构建bytes类型的请求体
r = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# 构建请求对象，使用Request()方法
response =urllib.request.urlopen(r)
# 发送网络请求
print(response.read().decode('utf-8'))
# 打印解码

"""
/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-4.py 
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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", 
    "X-Amzn-Trace-Id": "Root=1-67d43e19-6fccce43293e0e765e174519"
  }, 
  "json": null, 
  "origin": "31.94.24.48", 
  "url": "https://www.httpbin.org/post"
}


Process finished with exit code 0
"""