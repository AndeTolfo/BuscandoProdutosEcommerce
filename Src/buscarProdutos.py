import requests
from bs4 import BeautifulSoup
import pandas as pd

url_default = 'https://www.med4.com.br/'
product_name_search = input('Search Product Name:')

response = requests.get(url_default + 'search/?q=' + product_name_search)

site = BeautifulSoup(response.text, 'html.parser') 

list_products = []

products = site.findAll('div', attrs={'class': 'item-description py-4 px-3'})

for product in products:
    product_name = product.find('div', attrs={'class': 'js-item-name item-name mb-3'})
    product_price = product.find('span', attrs={'class': 'js-price-display item-price'})
    product_link = product.find('a', attrs={'class': 'item-link'}).get('href')
    list_products.append([product_name.text.strip(), product_price.text.strip(), product_link])  

"""    if product_name:
        print(product_name.text.strip())
    if product_price:    
        print(product_price.text.strip())
    if product_link:
        print(product_link)
"""        

products_data = pd.DataFrame(list_products, columns=['name', 'price', 'link'])
products_data.to_excel('Products.xlsx', index=False)

print('Resultados:')
print(products_data)





