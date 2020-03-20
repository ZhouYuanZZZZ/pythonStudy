import mysql.connector


def test0():
    print(mysql.connector)
    print(mysql.connector)


def test1():
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        port='3306',
        database='hr')
    print(conn)

    c = conn.cursor()
    sql = '''
        create table USER_TB(
            user_id int primary key auto_increment,
            name varchar(255),
            pass varchar(255),
            remark varchar(500)
        )
    '''
    c.execute(sql)

    c.close()
    conn.close()


def test2():
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        port='3306',
        database='hr')
    print(conn)

    c = conn.cursor()

    sql = '''insert into USER_TB values(null,%s,%s,%s)'''
    c.execute(sql, ('zy0', 'pass0', '1'))

    conn.commit()
    c.close()
    conn.close()


test2()
