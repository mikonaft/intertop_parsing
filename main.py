#default modules
import csv
import json
import time
import random
import datetime
from os import system

#created module
from core.config import DOMEN, URL, HEADERS

#downloaded modules 
import requests
from bs4 import BeautifulSoup

#---------------------------------------------------------------------
#get response
count_page = int(input("Сколько страниц спарсить: "))

for count in range(1, count_page + 1):
    response = requests.get(url=URL, headers=HEADERS, params={"page": f"page-{count}"}) 
    with open("core/html/index.html", "a", encoding="UTF-8") as file:
        file.write(response.text)
        
for count in range(1, count_page + 1):
    with open("core/html/index.html", "r") as file:
        src = file.read()
        
    soup = BeautifulSoup(src, "html.parser").find_all("div", class_="product-item-container")

    with open("core/html/index.html", "w") as file:
        file.write(str(soup))
#---------------------------------------------------------------------

with open("core/html/index.html", "r") as file:
    src = file.read()
    
soup = BeautifulSoup(src, "html.parser").find_all("a")

product_info = []
for item in soup:
    item_url = DOMEN + item.get('href')
    item_name = item.get("data-name")
    item_category = item.get("data-category").replace("/", " ")
    item_new_price = item.find('span', class_='new-product__new-price').text.strip()
    
    
    information = {
        "url": item_url,
        'name': item_name,
        'category': item_category,
        'price': item_new_price
    }
#     print(f"""
# Товар:      {item_name},
# Категория:  {item_category}, 
# Ссылка:     {item_url}
# Цена:       {item_new_price}\n""")
    
    product_info.append(information)

with open(f"core/alpha_industry.json", "w", encoding="UTF-8") as file:
    json.dump(product_info, file, indent=4, ensure_ascii=False)
