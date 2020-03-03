import RestApi_bank
import RestApi_bus
import RestApi_cafe
import RestApi_convenience
import RestApi_food
import RestApi_hospital
import RestApi_mart
import RestApi_school
import RestApi_subway
import mysqltest

class score:
    snum=0
    pnum=0
    scontent=""
    srate=0

def score_trans(num,score):
    num2=num/5
    if score<num2:
        return 1
    elif score<2*num2 and score>=num2:
        return 2
    elif score<3*num2 and score>=2*num2:
        return 3
    elif score<4*num2 and score>=3*num2:
        return 4
    elif score>=4*num2:
        return 5

score_func=[RestApi_mart.mart_score, RestApi_convenience.convenience_score, RestApi_school.school_score, RestApi_subway.subway_score, RestApi_food.food_score,RestApi_cafe.cafe_score, RestApi_bus.Bus_score, RestApi_bank.bank_score, RestApi_hospital.hospital_score]
address=mysqltest.select_product("paddress")
# print(address)
# print(type(address))
num=0
for i in range(len(address)):
    address_a=address[i][0]
    print(address_a)
    for j in range(len(score_func)):
        result=score_func[j](address_a)
        print(result)
        s=score()
        s.snum=num
        s.pnum=i
        s.scontent=result[0]
        # s.srate = str(list(result[1:]))
        # print(list(result[1:]))
        if result[0]=='지하철':
            s.srate=(score_trans(1000, float(result[1]))+score_trans(5, result[2]))/2
        elif result[0]=='버스정류장':
            s.srate=(score_trans(500, float(result[1]))+score_trans(50, result[2]))/2
        elif result[0]=='편의점':
            s.srate=(score_trans(500, float(result[1]))+score_trans(5, result[2]))/2
        elif result[0]=='마트':
            s.srate=score_trans(2000, float(result[1]))
        elif result[0]=='학교':
            s.srate=(score_trans(1000, float(result[1]))+score_trans(1000, float(result[2]))+score_trans(1000, float(result[3]))+score_trans(1000, float(result[4])))/4
        elif result[0]=='은행':
            s.srate=(score_trans(500, result[1])+score_trans(20, result[2]))/2
        elif result[0]=='음식점':
            s.srate=score_trans(500,result[1])
        elif result[0]=='카페':
            s.srate=score_trans(300,float(result[1]))
        elif result[0]=='병원':
            s.srate=score_trans(200,result[1])
        mysqltest.insert_score(s)
        num+=1

# for i in range(len(score_func)):
#     print(score_func[i](address[0]))
#     result=score_func[i](address[0])
#     s = score()
#     s.snum = num
#     s.pnum = i
#     s.scontent = result[0]
#     s.srate = result[1:]
#     # mysqltest.insert_score(s)
#     print(s.scontent)
#     print(s.srate)
#     num += 1

