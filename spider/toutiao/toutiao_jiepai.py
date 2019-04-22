import requests
from urllib.parse import urlencode
import re
from requests import codes
import os
from hashlib import md5

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'p3-tt.bytecdn.cn',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}


def get_page(offset):
    params = {
        'aid': '24',
        'offset': offset,
        'format': 'json',
        # 'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    base_url = 'https://www.toutiao.com/api/search/content/?keyword=%E8%A5%BF%E5%AE%89'
    url = base_url + urlencode(params)
    try:
        resp = requests.get(url)
        print(url)
        if 200 == resp.status_code:
            print(resp.json())
            return resp.json()
    except requests.ConnectionError:
        return None


items = []


def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            title = item.get('title')
            images = item.get('image_list')

            if title is None or images is None:
                continue

            for image in images:
                origin_image = re.sub("list/300x196/", "origin/", image.get('url'))

                print(image.get('url'))
                print(origin_image)
                print("---")

                # 返回一个生成器
                map = {
                    # 'image': origin_image,
                    'image': origin_image,
                    'title': title
                }

                items.append(map)


def save_image(item):
    # 获取文件系统分隔符
    img_path = '/Users/zzzz/Desktop/image' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image'), headers)
        if codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')
            if not os.path.exists(file_path):

                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)


def main(offset):

    for offset in range(0,100,20):
        json = get_page(offset)
        get_images(json)
        for item in items:
            save_image(item)


main(0)
