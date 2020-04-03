#writen by WSJ
#coding=utf-8
import sys  
import requests
import json
import re
import time
from bs4 import BeautifulSoup
reload(sys)  
sys.setdefaultencoding('utf8')



def crow_page1_firsthalf():
		url='https://search.jd.com/Search?keyword=%E5%84%BF%E7%AB%A5%E6%89%8B%E8%A1%A8&enc=utf-8&pvid=255e823a6d0a475a971486d8cc0ae7db'
		headers = {
		'authority': 'search.jd.com',
		'method': 'GET',
		'path': '/Search?keyword=%E5%84%BF%E7%AB%A5%E6%89%8B%E8%A1%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%84%BF%E7%AB%A5%E6%89%8B%E8%A1%A8&page=3&s=61&click=0',
		'scheme': 'https',
		'referer': '',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest',
		'Cookie':''
		}
		
		# post请求
		r = requests.get(url,headers=headers)
		r.encoding='utf-8'
		print r.status_code
		
		#f = open('html.txt','w')
		#print >> f , r.text
		#f.close()
		#f = open('html.txt','r')
		#r = f.read()
		#f.close()
		
		paser_productitem(r.text)

	
def crow_page_firsthalf(n):
		
		url='https://search.jd.com/s_new.php?keyword=%E5%84%BF%E7%AB%A5%E6%89%8B%E8%A1%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=' #7&s=181&click=0'
		url += str(2*n-1)
		url += '&s='
		url += str(1+60*(n-1))
		url += '&click=0'
		#print url
		#raw_input()
		
		headers = {
		'authority': 'search.jd.com',
		'method': 'GET',
		'path': '/s_new.php?keyword=%E5%84%BF%E7%AB%A5%E6%89%8B%E8%A1%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=5&s=121&click=0',
		'scheme': 'https',
		'accept': '*/*',
		#'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'zh-CN,zh;q=0.9',
		'referer': 'https://search.jd.com/Search?keyword=%E5%84%BF%E7%AB%A5%E6%89%8B%E8%A1%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=5&s=121&click=0',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'x-requested-with': 'XMLHttpRequest',
		'Cookie':'shshshfpa=e827ba58-975f-9aa7-a2b0-eeacfad16b2c-1585407708; __jdv=122270672|qdan.me|-|-|not set|1585407708824; __jdu=1231924428; areaId=2; ipLoc-djd=2-2825-0-0; PCSYCityID=CN_310000_310100_310115; shshshfpb=i6%203cd7q3w6U5YGmLIJrWMA%3D%3D; xtest=4572.cf6b6759; qrsc=3; rkv=V0800; __jdc=122270672; shshshfp=fd21732d1a95680c1173748647be0007; 3AB9D23F7A4B3C9B=R4PCDSC7UIPDWAHWS2Z2LKZETH6FXFH6ITPNCKGRUFX2ZWKGKSS3WQN74Q7UWHZUHISJ7WIFUYXAQY4CHHRF557UA4; __jda=122270672.1231924428.1584597159.1585876243.1585880613.8'
		}
		
		# post请求
		r = requests.get(url,headers=headers)
		r.encoding='utf-8'
		print r.status_code
		
		#tmp_fname = str(n)+'.txt'
		#f = open(tmp_fname,'w')
		#print >> f , r.text
		#f.close()
		#f = open('2.txt','r')
		#r = f.read()
		#f.close()
		#paser_productitem(r)	
		
		paser_productitem(r.text)			

def crow_page_lasthalf(n):
		url='https://search.jd.com/s_new.php?keyword=%E5%84%BF%E7%AB%A5%E6%89%8B%E8%A1%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=' #=4&s=91&scrolling=y&log_id=1585893878.93568'
		
		url += str(2*n)
		url += '&s='
		url += str(31+60*(n-1))
		url += '&scrolling=y&log_id='
		a=time.time()
		b='%.5f'%a
		url += str(b)
		#print url
		
		#raw_input()
		#return
		
		headers = {
		'authority': 'search.jd.com',
		'method': 'GET',
		'path': '/s_new.php?keyword=%E5%84%BF%E7%AB%A5%E6%89%8B%E8%A1%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=5&s=121&click=0',
		'scheme': 'https',
		'accept': '*/*',
		#'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'zh-CN,zh;q=0.9',
		'referer': 'https://search.jd.com/Search?keyword=%E5%84%BF%E7%AB%A5%E6%89%8B%E8%A1%A8&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=5&s=121&click=0',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'x-requested-with': 'XMLHttpRequest',
		'Cookie':'shshshfpa=e827ba58-975f-9aa7-a2b0-eeacfad16b2c-1585407708; __jdv=122270672|qdan.me|-|-|not set|1585407708824; __jdu=1231924428; areaId=2; ipLoc-djd=2-2825-0-0; PCSYCityID=CN_310000_310100_310115; shshshfpb=i6%203cd7q3w6U5YGmLIJrWMA%3D%3D; xtest=4572.cf6b6759; qrsc=3; rkv=V0800; __jdc=122270672; shshshfp=fd21732d1a95680c1173748647be0007; 3AB9D23F7A4B3C9B=R4PCDSC7UIPDWAHWS2Z2LKZETH6FXFH6ITPNCKGRUFX2ZWKGKSS3WQN74Q7UWHZUHISJ7WIFUYXAQY4CHHRF557UA4; __jda=122270672.1231924428.1584597159.1585876243.1585880613.8'
		}
		
		# post请求
		r = requests.get(url,headers=headers)
		r.encoding='utf-8'
		print r.status_code
		
		#tmp_fname = str(n)+'_last.txt'
		#f = open(tmp_fname,'w')
		#print >> f , r.text
		#f.close()
		#f = open('2.txt','r')
		#r = f.read()
		#f.close()
		#paser_productitem(r)	
		
		paser_productitem(r.text)			

def paser_productitem(rsptext):
		soup = BeautifulSoup(rsptext,"html.parser")
		
		search_div = soup.findAll(attrs={"class":"gl-i-wrap"})
		for ss in search_div:
			ss_1 = ss.find(attrs={"class":"p-name p-name-type-2"})
			ss_11 = ss_1.a
			#f = open('ss_11.txt','w')
			#print >> f , ss_11
			#f.close()
			#raw_input()
			
			#search product name
			ss_111 = re.search( r'<em>(.*?)</em>',str(ss_11), re.S) #get string from "xxx" to "xxx"
			ss_1111 = ss_111.group()[4:-5]	
			p_name = re.sub(r'<.*?>','',ss_1111)
			#print p_name.decode('utf-8')
			
			#search product price
			ss_1 = ss.find(attrs={"class":"p-price"})
			ss_11 = re.findall(r"<i>(.+?)</i>",str(ss_1))
			if ss_11 == []:
				ss_11 = re.findall(r'data-price=\"(.+?)\"><em>',str(ss_1))
			
	
			p_price = ss_11[0]
			#print p_price
		
			print >> fo , p_name + ',' + p_price

#-----------------------main flow---------------------------------------------------------
fo = open('product.txt','w')
crow_page1_firsthalf()
time.sleep(2)
crow_page_lasthalf(1)

for i in range(2,101):
		print 'processing page ' + str(i)
		crow_page_firsthalf(i)
		time.sleep(1)
		crow_page_lasthalf(i)
		time.sleep(1)

fo.close()
print 'DONE'



