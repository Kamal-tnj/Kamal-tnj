
from bs4 import BeautifulSoup
import requests

page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
soup= BeautifulSoup(page.content)

t   =  "restnt-info cursor"      # first_title=soup.find_all('div', class_="restnt-info cursor")
l   =  "restnt-loc ellipsis"     # first_location = soup.find('div',class_="restnt-loc ellipsis")
p   =  "double-line-ellipsis"    # price = soup.find_all('span',class_="double-line-ellipsis")
img   =  "no-img"                # images = soup.find_all("img",class_='no-img')


titles=[]
for i in soup.find_all('div',class_=t):
    titles.append(i.text)

location=[]
for i in soup.find_all('div',class_=l):
    location.append(i.text)

price=[]
for i in soup.find_all('span', class_=p):
    price.append(i.text)

imageUrl=[]
for i in soup.find_all("img",class_=img):
    imageUrl.append(i['data-src'])


import pandas as pd
df = pd.DataFrame({"Titles": titles, "Location":location,"Price":price,"Images_url":imageUrl})

print(df)