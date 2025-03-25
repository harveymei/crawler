"""
使用HTTPError类捕获异常
HTTPError类是URLError类的子类，用于处理HTTP请求所出现的异常

"""
import urllib.request  # 导入urllib.request模块，用于发送HTTP请求
import urllib.error    # 导入urllib.error模块，用于处理HTTP请求中的异常

try:
    # 使用urlopen方法发送HTTP GET请求到指定的URL
    response = urllib.request.urlopen('http://mirrors.163.com/a.html')
    # 打印HTTP响应的状态码
    print(response.status)

except urllib.error.HTTPError as error:
    # 捕获HTTPError异常，并打印状态码
    print('状态码为：', error.code)
    # 打印异常的原因
    print('异常信息为：', error.reason)
    # 打印HTTP响应头信息
    print('请求头信息如下： \n', error.headers)


"""
/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-11.py 
状态码为： 404
异常信息为： Not Found
请求头信息如下： 
 Server: nginx
Date: Tue, 25 Mar 2025 14:13:51 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 146
Connection: close



Process finished with exit code 0

"""