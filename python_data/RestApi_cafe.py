import json
import requests

def cafe_score(address):
    category_name = []
    distance = []
    url = "https://dapi.kakao.com/v2/local/search/address.json?"
    apikey = "15423876a0c084fd44724b06f11395a9"
    query = address
    r1 = requests.get( url, params = {'query':query}, headers={'Authorization' : 'KakaoAK ' + apikey } )
    rj=r1.json()
    # print(r1.json())
    x=r1.json()['documents'][0]["x"]
    y=r1.json()['documents'][0]["y"]
    n=1
    while(True):
        url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
        apikey = "15423876a0c084fd44724b06f11395a9"
        query = "카페"
        # 지하철SW8, 버스정류장, 편의점CS2, 마트MT1, 학교SC4, 은행BK9, 음식점FD6, 카페CE7, 병원HP8
        category_group_code = "CE7"
        radius=300
        page=n # 마지막 페이지 이후 남은 페이지는 마지막 페이지와 같은 결과만 나옴
        size=15
        r = requests.get( url, params = {'query':query,'category_group_code':category_group_code,'radius':radius,'page':page,'size':size,'x':x,'y':y, 'sort': 'distance'}, headers={'Authorization' : 'KakaoAK ' + apikey } )
        r.json()
        # print(r.url)
        # print(r.json())
        # print(r.json()["meta"]["total_count"]) # 총 검색된 데이터 수
        totalCnt=r.json()["meta"]["total_count"]
        if r.json()["meta"]["total_count"]==0:
            print("검색된 데이터가 없습니다.")
            return None
        else:
            for i in range(len(r.json()['documents'])):
                distance.append(r.json()['documents'][i]['distance'])
        is_end = r.json()["meta"]["is_end"]
        with open('jsonFile\\cafe'+str(n)+'.json', 'w', encoding='utf-8') as make_file:
            json.dump(r.json(), make_file, ensure_ascii=False, indent="\t")
        if is_end:
            break
        n+=1
    ditance_min=min(distance)
    return query, ditance_min