import requests
from bs4 import BeautifulSoup


def scrape():
    lst=[]
    a=requests.get("https://www.worldometers.info/coronavirus/")
    print(a)
    soup=BeautifulSoup(a.text,'html.parser')

    # print(soup)

    

    c=soup.select('tbody')
    for x in c:
        # print(x)
        y=x.select('tr')
        for td in y:
            v=td.findAll('td')
            lst.append({'country':str(v[0].get_text()),'TotalCases':str(v[1].get_text()),'NewCases':str(v[2].get_text()),'TotalDeath':str(v[3].get_text()),'NewDeath':str(v[4].get_text()),'TotalRecovery':str(v[5].get_text()),'ActiveCases':str(v[6].get_text()),'Critical':str(v[7].get_text())})
    return lst

            
        
        
        