import requests
import re
import time
import os
import mysql.connector
from bs4 import BeautifulSoup

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
    html = BeautifulSoup(html, "lxml")
    html = html.select("dd")

    for item in html:
        map = parse_item(item)

        print(map)

        data_list.append(map)


def write_data_txt(datas):
    with open('top100.txt', 'w', encoding='utf-8') as file:
        for item in datas:
            file.write(item['item_name'] + os.linesep)
            file.write(item['star'] + os.linesep)
            file.write(str(item['score']) + os.linesep)
            file.write(str(item['rank']) + os.linesep)
            file.write(item['releasetime'] + os.linesep)
            file.write('---------------------------------------------------------------''\n')


def write_data_mysql(datas):
    connect = mysql.connector.connect(host='10.2.0.67', port=3306,
                                      user='root', password='root',
                                      database='python_test')

    cursor = connect.cursor()

    sql = '''insert into maoyan_top_100(item_name,stars,rank_position,score,issue_time)
                values(%s,%s,%s,%s,%s)'''
    for item in datas:
        data = (item['item_name'], item['star'], item['rank'], item['score'], item['releasetime'])
        cursor.execute(sql, data)

    connect.commit()

    cursor.close()
    connect.close()


def create_table():
    print(0)


def main():
    for i in range(10):
        url = 'http://maoyan.com/board/4?offset=' + str(i * 10)
        html = get_one_page(url)
        parse_one_page(html)
        time.sleep(1)

    write_data_mysql(data_list)


def parse_item(dd):
    item_name = dd.select_one("img:nth-child(2)").attrs["alt"]

    star = dd.select_one("p.star").get_text()
    star = star.strip()
    star = star[3:]

    issue_time = dd.select_one("p.releasetime").get_text().strip()
    m = re.search(releasetime_re, issue_time)
    releasetime = m.group()
    if (len(releasetime) == 4):
        releasetime = releasetime + "-01-01"

    score = dd.select_one("i.integer").get_text().strip() + dd.select_one("i.fraction").get_text().strip()

    rank = dd.select_one("i.board-index").get_text().strip()

    map = {"item_name": item_name,
           "star": star,
           "releasetime": releasetime,
           "score": float(score),
           "rank": int(rank)
           }

    return map


def test0():
    for i in range(10):
        time.sleep(0.1)

        url = 'http://maoyan.com/board/4?offset=' + str(i * 10)
        html = get_one_page(url)

        parse_one_page(html)

    write_data_txt(data_list)
    write_data_mysql(data_list)


if __name__ == '__main__':
    test0()
