from math import *
from sympy import *

# 주어지 위도 경도를 기준으로 거리에 따른 위도 경도 구하기
def axis_x_dist(axis_x, axis_y,dist):
    R = 6373.0
    x=Symbol('x')
    lat1 = radians(axis_x)
    lon1 = radians(axis_y)
    lat2 = x
    lon2 = radians(axis_y)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    c=dist/R
    # a=tan(c)**2/(1+tan(c)**2)

    equation=(tan(c/2)**2/(1+tan(c/2)**2))-(sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2)
    # print(equation)
    # print(solve(equation,x, dict=True))
    sol=solve(equation,x, dict=True)
    return degrees(sol[0][x]), degrees(sol[1][x])

def axis_y_dist(axis_x, axis_y, dist):
    R = 6373.0
    x = Symbol('x')
    lat1 = radians(axis_x)
    lon1 = radians(axis_y)
    lat2 = radians(axis_x)
    lon2 = x

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    c = dist / R
    # a=tan(c)**2/(1+tan(c)**2)

    equation = (tan(c / 2) ** 2 / (1 + tan(c / 2) ** 2)) - (
                sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2)
    # print(equation)
    # print(solve(equation, x, dict=True))
    sol = solve(equation, x, dict=True)
    return degrees(sol[0][x]), degrees(sol[1][x])
# -------------------------------------------------

def distance_m(axis_x, axis_y, axis_x1, axis_y1):
    R = 6373.0
    lat1 = radians(axis_x)
    lon1 = radians(axis_y)
    lat2 = radians(axis_x1)
    lon2 = radians(axis_y1)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    # print("Result:", distance, "km")
    return distance*1000