import json
from bs4 import BeautifulSoup
import requests
#from selenium import webdriver
import lxml
import json
import xml.etree.ElementTree as ET
from pymysql import connect,cursors

conn = connect (
    host ="localhost",
    user="green",
    password="green1234",
    db="greendb",
    charset="utf8"
)
cursor = conn.cursor(cursors.DictCursor)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}



html= requests.get("http://openAPI.seoul.go.kr:8088/66594a6c6c6d697335304d4b584b43/xml/RealtimeCityAir/1/25/",headers= headers)



soup= BeautifulSoup(html.text, 'html.parser')
msrdt_data= soup.find_all("msrdt")
print(soup.find_all("msrdt")[1])
print(soup.find_all("msrrgn_nm")[2])
print(soup.find_all("pm10")[24])
print(soup.find_all("pm25")[5])
print(soup.find_all("o3")[8])
print(soup.find_all("no2")[11])
print(soup.find_all("co")[13])
print(soup.find_all("so2")[14])
print(soup.find_all("idex_nm")[16])
print(soup.find_all("idex_mvl")[19])

datas=[]
for i in range (len(msrdt_data)):
    msrdt = soup.find_all("msrdt")[i].string.strip()
    msrrgn_nm = soup.find_all("msrrgn_nm")[i].string.strip()
    msrste_nm = soup.find_all("msrste_nm")[i].string.strip()
    pm10=  soup.find_all("pm10")[i].string.strip()
    pm25=  soup.find_all("pm25")[i].string.strip()
    o3 =  soup.find_all("o3")[i].string.strip()
    no2=  soup.find_all("no2")[i].string.strip()
    co=  soup.find_all("co")[i].string.strip()
    so2=  soup.find_all("so2")[i].string.strip()
    idex_nm=  soup.find_all("idex_nm")[i].string.strip()
    idex_mvl=  soup.find_all("idex_mvl")[i].string.strip()
    
    
    data = [msrdt,msrrgn_nm,msrste_nm,pm10,pm25,o3,no2,co,so2,idex_nm,idex_mvl]
    datas.append(data)

sql=   "INSERT INTO weather(msrdt,msrrgn_nm,msrste_nm,pm10,pm25,o3,no2,co,so2,idex_nm,idex_mvl)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
cursor.executemany(sql, datas)
conn.commit()


#print (datas)

#print(soup.find_all("msrrgn_nm"))

#data = ET.fromstring(soup)

#print (soup)

#print (data)
#data = soup.select("realtimecityair")
#print (data)
#wheather_data = soup.find("table",{'id' :'AXGridTarget_AX_gridBodyTable'})

#print(wheather_data)


