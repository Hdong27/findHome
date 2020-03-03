import pymysql

# select all
def select_all():
    conn = pymysql.connect(host='localhost', user='root', password='apmsetup', db='findHome', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = "select * from users"
            curs.execute(sql)
            rs = curs.fetchall()
            # for row in rs:
            #     print(row)
    finally:
        conn.close()
    return rs

# select
def select_product(colname):
    conn = pymysql.connect(host='localhost', user='root', password='apmsetup', db='findHome', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = "select "+colname+" from product"
            curs.execute(sql)
            rs = curs.fetchall()
            # for row in rs:
            #     print(row)
    finally:
        conn.close()
    return rs

# select
def select_score(colname, content):
    conn = pymysql.connect(host='localhost', user='root', password='apmsetup', db='findHome', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = "select "+colname+" from scores where scontent=%s"
            curs.execute(sql,(content))
            rs = curs.fetchall()
            # for row in rs:
            #     print(row)
    finally:
        conn.close()
    return rs


# insert
def insert_score(score):
    conn = pymysql.connect(host='localhost', user='root', password='apmsetup', db='findHome', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = 'insert into scores values(%s, %s, %s, %s)'
            curs.execute(sql, (score.snum, score.pnum, score.scontent, score.srate))
        conn.commit()
    finally:
        conn.close()



# num칼럼으로 DB Delete
def delete_test(num):
    conn = pymysql.connect(host='localhost', user='root', password='apmsetup', db='findHome', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = 'delete from users where num=%s'
            curs.execute(sql, num)
        conn.commit()
    finally:
        conn.close()



#DB Update
def update_test(test_obj):
    conn = pymysql.connect(host='localhost', user='root', password='apmsetup', db='findHome', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = 'update users set name=%s where num=%s'
            curs.execute(sql, (test_obj.name, test_obj.num))
        conn.commit()
    finally:
        conn.close()
