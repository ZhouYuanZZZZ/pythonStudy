import requests
import pyquery
import re
import time

releasetime_re = '(\d{4}-\d{2}-\d{2}){1}|(\d){4}'
actors_re = '(主演：)(.+)'

data_list = []


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML,like Gecko) Chrome / 65.0.3325.162 Safari / 537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_one_page(html):
    doc = pyquery.PyQuery(html)

    dd = doc('dd')

    for item in dd.items():
        name = item('a:first').attr('title')
        rank = item('i:first').text()
        score = item('p[class=score]').eq(0).text() + item('p[class=score]').eq(1).text()
        actors = item('p[class=star]').text()

        actors_text = re.search(actors_re, actors).group(2)

        releasetime = item('p[class=releasetime]').text()
        releasetime_text = re.search(releasetime_re, releasetime).group()

        print(name)
        print(rank)
        print(score)
        print(actors_text)
        print(releasetime_text)
        print('---------------------------------------')

        data = {'name': name, 'rank': rank, 'score': score, 'actors_text': actors_text,
                'releasetime_text': releasetime_text}
        data_list.append(data)


def write_data(datas):
    with open('top100.txt', 'w', encoding='utf-8') as file:
        for item in datas:
            file.write(item['name']+'\n')
            file.write(item['rank']+'\n')
            file.write(item['score']+'\n')
            file.write(item['actors_text']+'\n')
            file.write(item['releasetime_text']+'\n')
            file.write('---------------------------------------------------------------''\n')


def main():
    for i in range(10):
        url = 'http://maoyan.com/board/4?offset=' + str(i * 10)
        html = get_one_page(url)
        parse_one_page(html)
        time.sleep(1)

    write_data(data_list)


main()
