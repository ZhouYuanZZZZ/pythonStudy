import mysql.connector

connect = None


def test0():
    global connect
    connect = mysql.connector.connect(host='10.2.0.67', port=3306,
                                      user='root', password='root',
                                      database='python_test')

def test1():
    sql = '''
            create table maoyan_top_100
            (
                item_id int auto_increment,
                item_name varchar(50) null,
                stars varchar(100) null,
                rank_position int null,
                issue_time datetime null,
                score int null,
                constraint maoyan_top_100_pk
                    primary key (item_id)
            )'''

    cursor = connect.cursor()

    cursor.execute(sql)

    cursor.close()
    connect.close()




if __name__ == '__main__':
    test0()
    #test1()
