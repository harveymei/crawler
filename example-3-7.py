import urllib.request
import urllib.parse
import http.cookiejar
# import json
# 返回不是json格式数据，所以此处引入的模块未使用

url = 'https://lewo.uk/wp-login.php'
data = bytes(urllib.parse.urlencode({'log':'harvey', 'pwd':'123465'}), encoding='utf-8')
cookie_file = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(cookie_file)
# 创建一个cookiejar对象，用于保存cookie

cookie_processor = urllib.request.HTTPCookieProcessor(cookie)
# 创建一个cookie处理器，用于处理cookie
opener = urllib.request.build_opener(cookie_processor)
# 创建一个opener，并添加cookie处理器

response = opener.open(url, data=data)
# 发送请求，并保存cookie

cookie.save(ignore_expires=True, ignore_discard=True)
# 保存cookie
for i in cookie:
    print(i.name, i.value)


"""
/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-7.py 
wordpress_test_cookie WP%20Cookie%20check

Process finished with exit code 0
"""
