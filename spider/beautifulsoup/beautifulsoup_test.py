from bs4 import BeautifulSoup

html = """
   <html><head><title>The Dormouse's story</title></head>
   <body>
   <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
   <p class="story">Once upon a time there were three little sisters; and their names were
   <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
   <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
   <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
   and they lived at the bottom of a well.</p>
   <p class="story">...</p>
   </body>
   """
soup = BeautifulSoup(html,'html.parser')


def test0():

    print(soup.title)
    # <title>The Dormouse's story</title>
    print(soup.head)
    # <head><title>The Dormouse's story</title></head>
    print(soup.a)

    # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
    print(soup.p)

    # <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    print (type(soup.p))
    # <class 'bs4.element.Tag'>

def test1():
    print(soup.a.name)

def test2():
    print(soup.p.string)
    print(type(soup.p.string))

def test3():
    list = soup.body.contents
    print(type(list))
    print(len(list))
    print(list)

def test4():
    p = soup.select("p")
    print(type(p[0]))

test4()
