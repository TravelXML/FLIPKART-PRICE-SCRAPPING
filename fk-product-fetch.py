#@Author: Sapan Mohanty
#email:ctoattraveltech@gmail.com
import requests
from bs4 import BeautifulSoup
import csv

currentPage = 1
maxPageNoToExe = 100

productCount =1
writeToData = []
header = ['PRODUCT COUNT', 'PRODUCT NAME', 'PRICE']



while currentPage < maxPageNoToExe:

    print('--------------------------')
    print('#PAGE:',currentPage)
    print('--------------------------')
    pageNoToAppend = currentPage
    url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(pageNoToAppend)
    print(url)

    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    name_box = soup.find_all('div', attrs={'class':'_4rR01T'})
    price_box = soup.find_all('div', attrs={'class':'_30jeq3 _1_WHN1'})

    productCountByPage = 0

    for product in zip(name_box,price_box):
        name,price=product
        name_proper=name.text.strip()
        price_proper=price.text.strip()        
        #print('\n',productCount,'#',name_proper,'-',price_proper,'\n')
        writeToData.insert( productCount-1,[ productCount,  name_proper ,  price_proper ])
        productCountByPage = productCountByPage+1        
        productCount = productCount + 1 
    if productCountByPage == 0:
        with open('reports.csv', 'w', encoding='UTF8') as f:
            # create the csv writer
            writerCsv = csv.writer(f)
            # write a row to the csv file
            writerCsv.writerow(header)
            print('Now READY to write CSV...')
            writerCsv.writerow(writeToData) 
            print('Now Your CSV file is READY View')
      
        break           
    currentPage = currentPage + 1
