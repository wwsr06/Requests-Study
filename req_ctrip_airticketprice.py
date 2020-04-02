#coding=utf-8
import sys  
import requests
import json
import time
import urllib2
reload(sys)  
sys.setdefaultencoding('utf8')


url = "https://flights.ctrip.com/itinerary/api/12808/products"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
"Content-Type": "application/json",
"Cookie": "",
"Connection": "keep-alive",
}
request_payload = {
    "flightWay": "Oneway",
    "classType": "ALL",
    "hasChild": False,
    "hasBaby": False,
    "searchIndex": 1,
    "date": "2020-04-05",
    "airportParams": [
        {"dcity": "SHA", "acity": "SYX", "dcityname": "上海", "acityname": "三亚", "date": "2020-04-05", "dcityid": 1, "acityid": 2},],
 	
}

# post请求
response = requests.post(url, data=json.dumps(request_payload), headers=headers,verify=False)
#print response.status_code
#print response.text

#request = urllib2.Request(url, data=json.dumps(request_payload) , headers=headers)
#response = urllib2.urlopen(request)
#print response
    
#raw_input()
#f = open('html.txt','w')
#print >> f , response
#f.close()
#raw_input()
#f = open('html.txt','r')
#response = f.read()
#f.close()
    
# 很多航班信息在此分一下
routeList = json.loads(response.text).get('data').get('routeList')

# 依次读取每条信息
outbuf = []
for route in routeList:
    #判断是否有信息，有时候没有会报错
    if len(route.get('legs')) == 1:
        legs = route.get('legs')
        flight = legs[0].get('flight')
        # 提取想要的信息
        airlineName = flight.get('airlineName')
        flightNumber = flight.get('flightNumber')
        departureDate = flight.get('departureDate')
        arrivalDate = flight.get('arrivalDate')
        departureCityName = flight.get('departureAirportInfo').get('cityName')
        departureAirportName = flight.get('departureAirportInfo').get('airportName')
        arrivalCityName = flight.get('arrivalAirportInfo').get('cityName')
        arrivalAirportName = flight.get('arrivalAirportInfo').get('airportName')
        punctualityRate = flight.get('punctualityRate')
        mealType = flight.get('mealType')
        
        
        cabins = legs[0].get('cabins')
        cabin = cabins[0]
        price = cabin.get('price').get('price')
        rate = cabin.get('price').get('rate')
        
        info = [airlineName,flightNumber,departureDate,arrivalDate,departureCityName,arrivalCityName,price,rate,punctualityRate,mealType]
       	outbuf.append(info)
        
        print (airlineName + \
        '|' + flightNumber +	\
        '|' + departureDate +	\
        '|' + arrivalDate +	\
        '|' + departureCityName +	\
        '|' + arrivalCityName + \
        '|' + str(price) + \
        '|' + str(rate))



#----------------- Main FLow -------------------------------------------
#print sys.argv[1]
#print sys.argv[2]
#print sys.argv[3]


		
