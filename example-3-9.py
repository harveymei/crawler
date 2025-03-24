import urllib.request
# 导入urllib.request模块

url = 'https://www.httpbin.org/get'
# 定义url

# 创建ProxyHandler对象，并传入代理服务器的IP地址和端口号
proxy_handler = urllib.request.ProxyHandler(
    {'https':'43.153.4.37:13001'}
)

# 创建Opener对象，并传入ProxyHandler对象
opener = urllib.request.build_opener(proxy_handler)
# 发送请求，并获取响应
response = opener.open(url, timeout=2)
# 打印返回内容
print(response.read().decode('utf-8'))

"""
/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-9.py 
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Host": "www.httpbin.org", 
    "User-Agent": "Python-urllib/3.12", 
    "X-Amzn-Trace-Id": "Root=1-67e17677-324a18837321a030214a58f4"
  }, 
  "origin": "43.153.4.37", 
  "url": "https://www.httpbin.org/get"
}


Process finished with exit code 0

"""