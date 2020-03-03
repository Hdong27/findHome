import json
import requests
def school_score(address):
    elem_distance = []
    mid_distance = []
    high_distance = []
    univercity_distance = []
    elem_school=[]
    mid_school=[]
    high_school=[]
    univercity=[]
    url = "https://dapi.kakao.com/v2/local/search/address.json?"
    apikey = "15423876a0c084fd44724b06f11395a9"
    query = address # 입력 주소
    r1 = requests.get( url, params = {'query':query}, headers={'Authorization' : 'KakaoAK ' + apikey } )
    rj=r1.json()
    # print(r1.json())
    x=r1.json()['documents'][0]["x"]
    y=r1.json()['documents'][0]["y"]
    n=1
    while(True):
        url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
        apikey = "15423876a0c084fd44724b06f11395a9"
        query = "학교"
        # 지하철SW8, 버스정류장, 편의점CS2, 마트MT1, 학교SC4, 은행BK9, 음식점FD6, 카페CE7, 병원HP8
        category_group_code = "SC4"
        radius=1000
        page=n # 마지막 페이지 이후 남은 페이지는 마지막 페이지와 같은 결과만 나옴
        size=15
        r = requests.get(url, params = {'query':query,'category_group_code':category_group_code,'radius':radius,'page':page,'size':size,'x':x,'y':y, 'sort': 'distance'}, headers={'Authorization' : 'KakaoAK ' + apikey } )
        r.json()
        # print(r.json())
        # print(r.json()["meta"]["total_count"]) # 총 검색된 데이터 수
        if r.json()["meta"]["total_count"]==0:
            print("검색된 데이터가 없습니다.")
            return None
        for i in range(len(r.json()["documents"])):
            # print(r.json()["documents"][i]["distance"])
            category_name=r.json()['documents'][i]['category_name']
            if category_name=='교육,학문 > 학교 > 초등학교':
                elem_distance.append(r.json()['documents'][i]['distance'])
                elem_school.append(r.json()['documents'][i])
            elif category_name=='교육,학문 > 학교 > 중학교':
                mid_distance.append(r.json()['documents'][i]['distance'])
                mid_school.append(r.json()['documents'][i])
            elif category_name=='교육,학문 > 학교 > 대학교':
                univercity_distance.append(r.json()['documents'][i]['distance'])
                univercity.append(r.json()['documents'][i])
            else:
                high_distance.append(r.json()['documents'][i]['distance'])
                high_school.append(r.json()['documents'][i])

        is_end = r.json()["meta"]["is_end"]
        # with open('jsonFile\\school'+str(n)+'.json', 'w', encoding='utf-8') as make_file:
        #     json.dump(r.json(), make_file, ensure_ascii=False, indent="\t")
        if is_end:
            break
        n+=1

    # print(distance)

    if len(elem_school)==0:
        elem_distance.append(9999)
    if len(mid_school)==0:
        mid_distance.append(9999)
    if len(high_school)==0:
        high_distance.append(9999)
    if len(univercity)==0:
        univercity_distance.append(9999)

    # print(elem_school)
    # print(min(elem_distance))  # 가장 가까운 초등학교까지 거리
    # print(mid_school)
    # print(min(mid_distance))  # 가장 가까운 중학교까지 거리
    # print(high_school)
    # print(min(high_distance))  # 가장 가까운 고등학교까지 거리
    # print(univercity)
    # print(min(univercity_distance))  # 가장 가까운 대학교까지 거리

    return query,min(elem_distance),min(mid_distance),min(high_distance),min(univercity_distance)