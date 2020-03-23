import requests
from bs4 import BeautifulSoup

def totalscrape():
    val=[]
    a=requests.get("https://www.worldometers.info/coronavirus/")
    soup=BeautifulSoup(a.text,'html.parser')

    x=soup.select('.maincounter-number')

    for i in x:
        b=i.findAll('span')
        for d in b:
            val.append(d.get_text())


    val2={"TotalCases":val[0],"Deaths":val[1],"Recovered":val[2]}
    
    return val2
