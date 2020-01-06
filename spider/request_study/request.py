import requests
import json


def test0():
    r = requests.post('https://httpbin.org/post', data={'key': 'value'})
    print(r.status_code)


def test1():
    r = requests.get('https://api.github.com/events')
    print(r.text)
    print(type(r.text))
    print("------------")
    print(r.content)
    print(type(r.content))


def test2():
    response = requests.get("http://www.baidu.com/")
    cookiejar = response.cookies
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

    print(cookiejar)
    print(cookiedict)


test1()
