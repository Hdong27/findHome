import mysqltest


prio_1='지하철'
prio_2='마트'
prio_3='은행'

prio_list=[]

# print(mysqltest.select_score('srate',prio_1))
temp1=mysqltest.select_score('srate', prio_1)
temp2=mysqltest.select_score('srate', prio_2)
temp3=mysqltest.select_score('srate', prio_3)

for i in range(len(temp1)):
    prio_list.append([float(temp1[i][0]),float(temp2[i][0]),float(temp3[i][0])])
    # print(float(mysqltest.select_score('srate', prio_1)[i][0]))

prio_list.sort(reverse=True)
print(prio_list)





