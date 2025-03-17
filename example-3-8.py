"""
使用cookie文件中保存的信息，请求一个登录后页面的url，可以返回该页面内容。
"""

import urllib.request
import http.cookiejar

# 定义要访问的URL
url = 'https://example.uk/wp-admin'

# 定义cookie文件的路径
cookie_file = 'cookie.txt'

# 创建一个LWPCookieJar对象来存储cookie
cookie = http.cookiejar.LWPCookieJar(cookie_file)

# 从文件中加载cookie，如果文件不存在则忽略
cookie.load(cookie_file, ignore_expires=True, ignore_discard=True)

# 创建一个HTTPCookieProcessor对象，用于处理cookie
handler = urllib.request.HTTPCookieProcessor(cookie)

# 创建一个opener对象，用于发送HTTP请求
opener = urllib.request.build_opener(handler)

# 使用opener对象打开URL，并获取响应
response = opener.open(url)

# 读取响应内容并解码为UTF-8字符串，然后打印出来
print(response.read().decode('utf-8'))
