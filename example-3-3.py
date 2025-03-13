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
    else:
        print(f'发生其他错误： {error.reason}')
