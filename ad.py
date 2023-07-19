##
##
## https://www.axeldoors.ru/catalog/seriya_chdk/in13/
##
##

import requests
from bs4 import BeautifulSoup
import time
import re
import xlsxwriter
import pathlib
from pathlib import Path
import sys
import json
import urllib3
urllib3.disable_warnings()
import urllib.parse
import itertools


###
from requests_html import HTMLSession

###


prefix = 'ad'

##
###


products = {}
path = Path(prefix+'-offers.json')
if(path.is_file()):
    f = open(prefix+'-offers.json')
    products = json.load(f)


##
##
def parseProduct(productUrl, force = False):

    productUrl = 'https://www.axeldoors.ru'+productUrl

    if( productUrl in products and not force):
        print('cache')
        return products[productUrl]

    print(productUrl)
    r = requests.get(productUrl)
    if(r.status_code != 200):
        return False


    soup = BeautifulSoup(r.text, 'lxml')
    options = []
    optionValueKeys = {}
    optionNameKeys = {}
    offers = {}

    comps = {

    }

    configOffersEl = soup.find('div', class_='c-catalog-element')
    id = ''
    offersData = []
    offersProperties = {}
    if( configOffersEl and configOffersEl['data-data'] and configOffersEl['data-properties'] ):
        id = json.loads(configOffersEl['data-data'])['id']
        offersData = json.loads(configOffersEl['data-data'])['offers']
        offersProperties = json.loads(configOffersEl['data-properties'])

    #for offerTest in offersData:
    #    print('')
    optionNameKeys = {}
    optionKeys = {}

    if( len(offersProperties) ):
        for option in offersProperties:
            itemImages = []
            itemValues = []

            for optionItem in option['values']:
                if not optionItem['id']:
                    continue

                opt = []

                img = optionItem['picture']
                if( img ):
                    img = 'https://www.axeldoors.ru'+img
                else:
                    img = ';'

                optionValue = optionItem['name']
                optionKeys[ option['code']+'|'+str(optionItem['id']) ] = optionValue
                itemValues.append( optionValue )
                itemImages.append( img )
            optionNameKeys[ option['code'] ] = option['name']
            options.append({
                'name': option['name'],
                'values': ';'.join(itemValues),
                'images': ';'.join(itemImages)
            })

    offers = {}
    images = {}
    for galleryEl in soup.find_all('div', class_='catalog-element-gallery'):
         img = galleryEl.find('a', class_='catalog-element-gallery-picture')
         if img and galleryEl['data-offer']:
            images[ galleryEl['data-offer'] ] = 'https://www.axeldoors.ru'+img['href']


    for offer in offersData:
        offerOptions = []
        for key in offer['values']:
            prop = offer['values'][key]
            name = optionNameKeys[key]
            valKey = optionKeys[ key +'|' + prop ]

            offerOptions.append( name+':'+valKey )
        img = ''
        if str(offer['id']) in images:
            img = images[ str(offer['id']) ]


        offers[ offer['id'] ] = {
            'id': offer['id'],
            'options': ';'.join(offerOptions),
            'image': img
        }


    desc = ''
    #descEl = soup.find('div', class_='tab-content-padding')
    #if descEl:
    #    desc = descEl.decode_contents()

    img = ''
    if(len(offers) and  next(iter(offers)) ):
        img = offers[  next(iter(offers)) ]['image']


    leng = 0
    col = ''
    cat = ''
    for bread in soup.find_all('div', class_='breadcrumb-item'):
        link = bread.find('a')
        if(link):
            leng+=1
            if(leng == 3):
                cat=link.text.strip()
            if(leng == 4):
                col = link.text.strip()

    product = {
        'id': id,
        'sku': prefix + '-'+str( id ),
        'cat': cat,
        'url': productUrl,
        'price': 0,
        'discountPrice': 0,
        'name': soup.find('h1').text.strip(),
        'description': 'desc',
        'collection': col,
        'images': img,
        'manufacturer': 'axeldoors',
        'options': options,
        'offers': offers,
    }
    return product

#product = parseProduct('https://www.axeldoors.ru/catalog/kollektsiya_q/q522/', True)
#print(product)
#exit()

###
###
def getCategories():

    path = Path(prefix+'-data.json')
    if(path.is_file()):
        f = open(prefix+'-data.json')
        return json.load(f)


    items = []
    prodCatLinks = ['https://www.axeldoors.ru/catalog/?PAGEN_1=1', 'https://www.axeldoors.ru/catalog/?PAGEN_1=2', 'https://www.axeldoors.ru/catalog/?PAGEN_1=3', 'https://www.axeldoors.ru/catalog/?PAGEN_1=4']

    for catUrl in prodCatLinks:
        perPageItems = getCategoryPage(catUrl)
        items = items + perPageItems
        print(len(perPageItems))


    with open(prefix + '-data.json', 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=4)

    return items

def getCategoryPage(catUrl):
    r = requests.get(catUrl)
    if(r.status_code != 200):
        return []

    print(catUrl)
    res = []

    soup = BeautifulSoup(r.text, 'lxml')
    prods = soup.find_all('a', class_='catalog-section-item-image-wrapper')
    for n, prodEl in enumerate(prods, start=1):
        res.append( {
            'url': prodEl['href']
        })
    return res



categories = getCategories()
print('Парсинг кол-во ' + str(len(categories)))


print('Начинаем разбор обьявлений')
pos = 1
all = len(categories)

###
workbook = xlsxwriter.Workbook(prefix+'-prices.xlsx')
worksheet = workbook.add_worksheet()
##

workbookOffer = xlsxwriter.Workbook(prefix+'-offers.xlsx')
worksheetOffers = workbookOffer.add_worksheet()
###
row = 0
start_time = time.time()


for prodBase in categories:
    item = parseProduct(prodBase['url'])
    if(not item):
        continue
    print(item)
    products[ item['url'] ] = item
    with open(prefix+'-offers.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)


    col = 0
    colOffers = 0
    if(row == 0):
        for headerTitle in item.keys():
            worksheet.write(row, col, headerTitle)
            col += 1
        col = 0
        row = 1
        #
        #worksheet.write(row, col + 1, cost)
    for key in item.keys():

        if key == 'options':
            col += 5
            options = item[key]
            for option in options:
                worksheet.write_string(row, col, str(option['name']))
                col += 1
                worksheet.write_string(row, col, str(option['values']))
                col += 1
                worksheet.write_string(row, col, str(option['images']))
                col += 2
        elif key == 'offers':
            offers = item[key]
            worksheetOffers.write_string(row, colOffers, str(item['sku']) )
            colOffers +=3
            for offerId in offers:
                offer = offers[offerId]
                worksheetOffers.write_string( row, colOffers, 'offer' )
                colOffers +=1
                worksheetOffers.write_string(row, colOffers, str(offer['id']) )
                colOffers +=1
                worksheetOffers.write_string(row, colOffers, str(offer['options']) )
                colOffers +=1
                worksheetOffers.write_string(row, colOffers, str(offer['image']))
                colOffers +=3

            ####
        else:
            value = item[key]
            worksheet.write_string(row, col, str(value))
            col += 1
    row += 1

    print('Строка %s, Общий процесс %s за %s '  % (row, (pos*100/all), time.time()-start_time)  )
    #items.append(item)
    pos+=1

print('сохраняем')
workbook.close()
workbookOffer.close()
