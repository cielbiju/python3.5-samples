#######################################
print("Quiz 1-2")

Transaction = int(input("중개료를 입력하세요(천원 단위) : "))

if   Transaction < 250 :    # Transaction : 천원 단위
    Commision = 3 + Transaction * 0.017    # Commision : 천원 단위
elif Transaction < 600 :
    Commision = 6 + Transaction * 0.0066
elif Transaction < 2000 :
    Commision = 8 + Transaction * 0.0034
elif Transaction < 5000 :
    Commision = 10 + Transaction * 0.0022
elif Transaction < 50000 :
    Commision = 15 + Transaction * 0.0011
else :
    Commision = 20 + Transaction * 0.0009

#A

Commision = int(Commision * 1000)

print("거래액 {}천원에 대한 길동에게 지불할 중개료는 {}원입니다.".format(Transaction, Commision))
print("계산인: 내이름 20160001 (G1)")


#########################################
print("Quiz 3")


import datetime, time
import urllib.request
import re

f = urllib.request.urlopen('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1144060000')
data = str(f.read())

pat = re.compile(r"<tm>(\d*)<\/tm>")  #<tm>숫자들</tm> 형태의 패턴을 찾는다
                                      # (  )로 둘러싼 부분을 추출해준다
m = pat.search(data)
if m:
    print(m.group(0)) # (0)는 매칭 성공한 라인 전체 (1)~ 부터는 ( )로 둘러싼 부분에 매칭된 항목들
    dd = m.group(1)
    d2 = dd   #A
else:
    dd = "no data"

pat = re.compile(r"<hour>(\d*)<\/hour>\\n\s*<day>(\d*)<\/day>\\n\s*<temp>([-\.\d]*)<\/temp>")
m = pat.search(data)
if not m:
    print("no data")
else:
    print(m.group(0))
    hh = m.group(1) + ":00"
    temp = m.group(3)

    print("예보시간은 ", d2)
    print(hh, "시의 예측온도는 ", temp)

###########################################
print("과제 #19")

import datetime, time
import urllib.request
import re

f = urllib.request.urlopen('http://openapi.seoul.go.kr:8088/(인증키)/xml/ListAirQualityByDistrictService/1/5/111201/')
data = str(f.read())

pat = re.compile(r"정규식완성")  #<MSRDATE>숫자들</MSRDATE> 형태의 패턴을 찾는다
                               # (  )로 둘러싼 부분을 추출해준다
m = pat.search(data)
if m:
    print(m.group(0)) # (0)는 매칭 성공한 라인 전체 (1)~ 부터는 ( )로 둘러싼 부분에 매칭된 항목들
    dd = m.group(1)
    d2 = dd   #A 포맷완성
else:
    dd = "no data"

pat = re.compile(r"정규식완성")  #<PM25>숫자들</PM25> 형태의 패턴을 찾는다
                               # (  )로 둘러싼 부분을 추출해준다
m = pat.search(data)
if not m:
    print("no data")
else:
    print(m.group(0))
    pm25 = m.group(1) 

    print(dd)   #포맷완성
    print(pm25)  #포맷완성





