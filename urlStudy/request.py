import urllib.request
import urllib.error
import urllib.parse
import socket


def test0():
    response = urllib.request.urlopen('https://www.baidu.com')
    print(response.status)
    print(response.getheaders())
    print(response.getheader('Server'))
    print(response.getheader('Content-Type'))


def test1():
    try:
        data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
        response = urllib.request.urlopen('http://httpbin.org/post', data=data, timeout=0.1)
        print(response.read().decode())
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('time out')


def test2():
    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIES.S;Windows NT)',
        'Host': 'httpbin.org'
    }

    data = bytes(urllib.parse.urlencode({'name': 'zy'}), encoding='utf8')
    req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(req)
    print(response.read().decode())


test2()
