import pymysql
import random

def insert_test(test_obj):
    conn = pymysql.connect(host='localhost', user='root', password='apmsetup', db='findHome', charset='utf8')
    try:
        with conn.cursor() as curs:
            sql = 'insert into product values(%s, %s, now(), %s, %s, %s, %s)'
            curs.execute(sql, (test_obj.num, test_obj.title, test_obj.address,test_obj.size,test_obj.content,test_obj.unum ))
        conn.commit()
    finally:
        conn.close()


address=["서울특별시 강북구 인수봉로 278-2","서울특별시 강북구 도봉로13길 37-10","서울특별시 은평구 은평터널로 169-18","서울 은평구 응암동 750-18","서울특별시 용산구 청파로77길 28","서울특별시 강남구 역삼로 462","서울 동작구 사당동 1139",
         "서울 관악구 신림동 1409-18","서울특별시 서초구 서초중앙로 200","서울 강남구 수서동 745-4","서울 강동구 성내동 434-34","서울특별시 강북구 한천로124나길 46-7","서울 노원구 중계동 358","서울시 도봉구 도봉로110마길 51","서울 도봉로106길 48"]

class obj:
    num=0
    title=""
    address=""
    size=0
    content=""
    unum=1

for i in range(len(address)):
    a=obj()
    a.num=i
    a.title="더미데이터"+str(i)
    a.address=address[i]
    a.size=random.randrange(10,80)
    a.content="더미데이터입니다"+str(i)
    a.unum=1
    insert_test(a)