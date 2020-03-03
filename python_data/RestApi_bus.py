import json
import requests
import xmltodict
def Bus_score(address):
    distance=[]
    url = "https://dapi.kakao.com/v2/local/search/address.json?"
    apikey = "15423876a0c084fd44724b06f11395a9"
    # query = "도봉구 도봉로110마길 51"
    query=address
    r1 = requests.get( url, params = {'query':query}, headers={'Authorization' : 'KakaoAK ' + apikey } )
    rj=r1.json()
    # print(r1.json())
    # print(jf)
    ApiKey = "Kiwi2pN6JTYhSH8JhTv7aeC7Q5KPRFaIf1bapYhVS327aQmpRpDinZg1vE72zOaHTYy5p2Urxur315ERhuRbFw%3D%3D"
    x=rj["documents"][0]["x"]
    y=rj["documents"][0]["y"]
    # print(x)
    # print(y)
    radius='500'
    # url = "http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getCtyCodeList?serviceKey=" + ApiKey + "&_type=json"
    url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos?serviceKey=" + ApiKey + "&tmY=" + y + "&tmX=" + x +"&radius=" + radius + "&_type=json"
    # print(url)
    r1 = requests.get(url)
    # print(r1.url)
    # print(r1.request)
    # print(r1.content)
    # print(r1.text)
    # with open('test3.xml', 'w', encoding='utf-8') as make_file:
    #     make_file.write(r1.text)
    # with open("test3.xml", 'r', encoding='utf-8') as f:
    #     xmlString = f.read()
    xmlString=r1.text
    jsonString = json.dumps(xmltodict.parse(xmlString), ensure_ascii=False, indent=4)
    # print(type(jsonString))
    # print(jsonString)
    # print(type(json.loads(jsonString)))
    jsonStrJson=json.loads(jsonString)
    # print(jsonStrJson["ServiceResult"]["msgBody"]["itemList"])
    busCnt = len(jsonStrJson["ServiceResult"]["msgBody"]["itemList"])
    for i in range(len(jsonStrJson["ServiceResult"]["msgBody"]["itemList"])):
        distance.append(jsonStrJson["ServiceResult"]["msgBody"]["itemList"][i]["dist"])

    # print(min(distance))  # 가장 가까운 버스정류장까지 거리
    # print(busCnt)  # 반경 내 버스 정류장 갯수

    # with open("jsonFile\\bus.json", 'w', encoding='utf-8') as f:
    #     f.write(jsonString)
    return "버스정류장",min(distance), busCnt