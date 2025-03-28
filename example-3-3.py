import urllib.request
# 导入异常处理模块，在发生异常时捕获异常进行进一步处理
import urllib.error
import socket

url = 'https://www.python.org/'

# 捕获异常，将可能引发异常的代码放在try块中
try:
    response = urllib.request.urlopen(url=url, timeout=0.1)
    print(response.read().decode('utf-8'))

# 捕获异常，如果发生异常，则跳转到except块
except urllib.error.URLError as error:
    # 判断异常原因，如果是超时，则执行超时处理逻辑
    if isinstance(error.reason, socket.timeout):
        print('当前任务已超时，即将执行下一个任务')
    # 按照示例代码，异常处理逻辑不完整，因此添加了以下代码
    else:
        print(f'发生其他错误： {error.reason}')


"""
/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-3.py 
发生其他错误： [Errno 101] Network is unreachable

Process finished with exit code 0
"""

"""
模拟网络延迟（适用于 Linux 系统）
   sudo tc qdisc add dev eth0 root netem delay 1000ms
清除网络延迟：
   sudo tc qdisc del dev eth0 root netem
"""