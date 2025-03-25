"""
使用parse子模块进行URL语法分析
拆分URL
"""
import urllib.parse

parse_result = urllib.parse.urlparse('https://docs.python.org/3/library/urllib.parse.html')
# 使用urlparse()方法，返回一个ParseResult对象

print(type(parse_result))
# 查看对象的类型
print(parse_result)

# 除了直接返回ParseResult对象外，还可以直接获取对象中的6个属性值
print('scheme值为：', parse_result.scheme)
print('netloc值为：', parse_result.netloc)
print('path值为：', parse_result.path)
print('params值为：', parse_result.params)
print('query值为：', parse_result.query)
print('fragment值为：', parse_result.fragment)


"""
/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-13.py 
<class 'urllib.parse.ParseResult'>
ParseResult(scheme='https', netloc='docs.python.org', path='/3/library/urllib.parse.html', params='', query='', fragment='')

Process finished with exit code 0

"""


"""
/usr/bin/python3.12 /home/harveymei/PycharmProjects/crawler/example-3-13.py 
<class 'urllib.parse.ParseResult'>
ParseResult(scheme='https', netloc='docs.python.org', path='/3/library/urllib.parse.html', params='', query='', fragment='')
scheme值为： https
netloc值为： docs.python.org
path值为： /3/library/urllib.parse.html
params值为： 
query值为： 
fragment值为： 

Process finished with exit code 0

"""