import json
import requests
from distance_axis import *
class stop(BaseException): pass

def bank_score(address):
    category_name = []
    distance = []
    url = "https://dapi.kakao.com/v2/local/search/address.json?"
    apikey = "15423876a0c084fd44724b06f11395a9"
    query = address
    r1 = requests.get( url, params = {'query':query}, headers={'Authorization' : 'KakaoAK ' + apikey } )
    rj=r1.json()
    # print(r1.json())
    x1=r1.json()['documents'][0]["x"]
    y1=r1.json()['documents'][0]["y"]
    # n=1

    x2,x3=axis_x_dist(float(x1),float(y1),1)
    y2,y3=axis_y_dist(float(x1),float(y1),1)

    # while(True):
    # url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
    apikey = "CB30983B-5DE0-3612-9FEC-3CBB65431B2C"
    query = "은행"
    size = "1000"
    category="070305" # 은행 카테고리 번호
    url = "http://api.vworld.kr/req/search?service=search&request=search&version=2.0&crs=EPSG:4326&bbox="+str(x2)+","+str(y2)+","+str(x3)+","+str(y3)+"&size="+size+"&page=1&query=" + query + "&type=place&category="+category+"&format=json&errorformat=json&key=" + apikey
    # print(url)
    r = requests.get(url)
    # print(r1.url)
    # print(r1.request)
    # print(r.json())
    # print(r.json()["response"]["record"]["total"]) # 총 검색된 데이터 수
    try:
        if r.json()["response"]["record"]["total"]==0:
            print("검색된 데이터가 없습니다.")
            raise stop
    except stop:
        pass
    for i in range(len(r.json()["response"]["result"]["items"])):
        category_name.append(r.json()["response"]["result"]["items"][i]["title"][:4])
        x4=r.json()["response"]["result"]["items"][i]["point"]["x"]
        y4=r.json()["response"]["result"]["items"][i]["point"]["y"]
        distance.append(round(distance_m(float(x1),float(y1),float(x4),float(y4))))
    category_name = list(set(category_name))
    # print(category_name)
    # print(distance)
    # print(min(distance)) # 가장 가까운 은행까지 거리
    # print(len(category_name)) # 반경내에 은행 종류 갯수

    # with open('jsonFile\\bank.json', 'w', encoding='utf-8') as make_file:
    #     json.dump(r.json(), make_file, ensure_ascii=False, indent="\t")

    return query,min(distance),len(category_name)
