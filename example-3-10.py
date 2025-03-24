"""
异常处理之处理URLError 异常
"""
import urllib.request
import urllib.error

# 捕获异常
try:
    # 请求一个不存在的网址
    response = urllib.request.urlopen('http://site2.rjkflm.com:666/123index.html')
except urllib.error.URLError as error:
    # 获取异常原因
    print(error.reason)


"""
/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-10.py 
[Errno -5] No address associated with hostname

Process finished with exit code 0

"""