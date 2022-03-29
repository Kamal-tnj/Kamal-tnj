
from bs4 import BeautifulSoup
import requests

page=requests.get('https://www.bewakoof.com/men-printed-tshirts')
# 10 product details which include product name , price , Image URL from
soup= BeautifulSoup(page.content,"html.parser")

productTag  =   "productCardDetail" # inside h3 tage
priceTag    =  "discountedPriceText"
imgTag      =  "productImgTag"


product=[]
for i in soup.find_all('h3'):
    product.append(i.text)

price=[]
for i in soup.find_all('span', class_=priceTag):
    price.append(i.text)

imageUrl=[]
for i in soup.find_all("img",class_=imgTag):
    imageUrl.append(i["src"])

import pandas as pd
df = pd.DataFrame({"Product_Name": product, "Price":price,"Images_url":imageUrl})
print(df)

