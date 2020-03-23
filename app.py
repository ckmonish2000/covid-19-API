from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup




a=requests.get("https://www.worldometers.info/coronavirus/")
print(a)
soup=BeautifulSoup(a.text,'html.parser')

# print(soup)

b=soup.find(class_='maincounter-number')

print(b)

c=soup.select('tbody')
for x in c:
    # print(x)
    y=x.select('tr')
    for td in y:
        v=td.findAll('td')
        print(v[0].get_text())
    
    