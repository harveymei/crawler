import urllib.request

url = 'https://www.python.org/'
response = urllib.request.urlopen(url=url)
print('响应代码为：', response.status)
print('响应头所有信息为：', response.getheaders())
print('响应头指定信息为：', response.getheader('Accept-Ranges'))

# 读取html代码并进行utf-8解码
print('Python官网html代码如下：\n', response.read().decode('utf-8'))
response.close()
