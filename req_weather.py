#######################################################################
# http://worldweather.wmo.int/en/city.html?cityId=338
# 简单的get请求，获取json反馈数据，解析相关字段
#
########################################################################

#coding=utf-8
import sys  
import requests
import json
reload(sys)  
sys.setdefaultencoding('utf8')

url = "http://worldweather.wmo.int/en/json/338_en.xml"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
"Content-Type": "application/json",
"Cookie": "",
}
request_payload = {
}

# post请求
r = requests.get(url)
#f = open('html.txt','w')
#print >> f , r.text
#f.close()
print r.status_code
#print r.text.encode("GBK","ignore")
#ctx_json = r.text.encode("GBK")

ctx_json = json.loads(r.text).get('city')
print ctx_json.get('cityName')
print ctx_json.get('forecast').get('forecastDay')[0].get('minTemp')