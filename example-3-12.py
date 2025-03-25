"""
双重异常捕获
适用于URLError和HTTPError父子类的双重异常捕获，避免但一异常类捕获不到异常的情况
"""
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('https://www.python.org/', timeout=0.1)
    # 限制超时，模拟网络异常

except urllib.error.HTTPError as error:
    # 捕获HTTPError异常，以及打印状态码和异常信息
    print('状态码为：', error.code)
    print('HTTPError异常信息为：', error.reason)
    print('请求头信息如下： \n', error.headers)

except urllib.error.URLError as error:
    # 进一步捕获URLError异常，打印异常信息
    print('URLError异常信息为：', error.reason)


'''
/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-12.py 
URLError异常信息为： [Errno 101] Network is unreachable

Process finished with exit code 0

'''

