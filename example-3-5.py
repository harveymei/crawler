"""
模拟登录，示例站点无法访问，使用wordpress站点进行测试
需要替换域名及用户名密码信息
"""
import urllib.request
import urllib.parse
import http.cookiejar
# import json
# 没有示例站点的json返回提示及判断逻辑，所以此处引入的模块未使用

url = 'https://example.com/wp-login.php'

data = bytes(urllib.parse.urlencode({'log':'harvey', 'pwd':'123465'}), encoding='utf-8')
r = urllib.request.Request(url=url, data=data, method='POST')
response = urllib.request.urlopen(r)
# print(response.read().decode('utf-8'))

# 实例化对象
cookie = http.cookiejar.CookieJar()
# 在 Python 的 urllib.request 模块中，HTTPCookieProcessor 是一个用于处理 HTTP Cookie 的处理器，
# 常与 build_opener() 一起使用来管理 Cookie。
# 生成cookie处理器
# HTTPCookieProcessor 的核心作用是简化 Cookie 的管理和使用，帮助开发者轻松实现会话保持或用户认证等功能。
# 创建一个HTTPCookieProcessor对象，用于管理cookie
cookie_processor = urllib.request.HTTPCookieProcessor(cookie)

# 构建一个自定义的opener，它能够处理包含cookie的请求
opener = urllib.request.build_opener(cookie_processor)

# 使用自定义的opener发送请求，这里包含cookie信息，以便服务器进行会话跟踪或用户认证
response2 = opener.open(url, data=data)


# 遍历cookie信息
for i in cookie:
    print(i.name, i.value)

"""
控制台输出的cookie信息

/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-5.py 
wordpress_test_cookie WP%20Cookie%20check
_lscache_vary 5c5fbf6d32ea4fbd9432799dc0f478d7
wordpress_logged_in_e6668002bb96a970eebe69a13348df8d harvey%7C1742138921%7CBxoQdy9c1VyUchhYiiBzCML7KRXA9l0f8znnF81qDG5%7C61077036fa936a447387b16fd7df83913544e8af30c77111d41566b3206586af
wp_lang en_US
wordpress_sec_e6668002bb96a970eebe69a13348df8d harvey%7C1742138921%7CBxoQdy9c1VyUchhYiiBzCML7KRXA9l0f8znnF81qDG5%7Ce04ba62e78c8dc60252237e30a609f202d7bced146d458294c2c1a082958a7f6
wordpress_sec_e6668002bb96a970eebe69a13348df8d harvey%7C1742138921%7CBxoQdy9c1VyUchhYiiBzCML7KRXA9l0f8znnF81qDG5%7Ce04ba62e78c8dc60252237e30a609f202d7bced146d458294c2c1a082958a7f6

Process finished with exit code 0

"""