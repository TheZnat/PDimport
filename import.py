import requests
import time
import xmltodict
import xlsxwriter
from pathlib import Path
import csv
import json
import os


###
jsonResGlobal = {}
###

DIR = os.path.dirname(__file__)
DIR_ROOT = os.path.dirname(DIR)


options = {}
with open(DIR+'/options.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        options[rows[0]] = rows[5]


path = Path(DIR+'/toimport.xml')
if(path.is_file()):
    with open(DIR+'/toimport.xml', 'r') as f:
        xmlData = f.read()
else:
    exit()



my_dict = xmltodict.parse(xmlData)
categories = my_dict['СписокТоваров']['Товар']


###
workbook = xlsxwriter.Workbook(DIR_ROOT+'/admin/uploads/1.xlsx')
worksheet = workbook.add_worksheet()
###
row = 0
start_time = time.time()



products = {

}

for item in categories:
    id = item['ID']
    sku = item['Раздел']


    if sku not in products:
        products[sku] = {
            'sku': item['Раздел'],
            'cat': item['НоменклатурнаяГруппа'],
            'name': item['ПолноеНаименование'],
            'images': item['СсылкаНаКартинку'],
            'cat3': item['Серия'],
            'price':item['Цена'],
            'discountPrice': 0,

            'manufacturer': 'profildors',
            'count': '',
            'h1': 'ПРОФИЛЬ ДОРС ' + item['Раздел'],
            'tmp1': '',
            'tmp2': '',
            'options': { },
            'offers': { },
    }

    offerOptions = {

    }

    products[sku]['offers'][id]={
        'id': id,
        'options': [],
        'image': item['СсылкаНаКартинку'],
    }

    offersScheme = ['Вариант стекла', 'Цвет']

    for key in item:
        skipProps = ['Ссылка', 'ID', 'Артикул', 'Наименование', 'Раздел', 'НоменклатурнаяГруппа', 'Серия', 'Бренд', 'Цена', 'СсылкаНаКартинку', 'ПолноеНаименование', 'Ширина', 'Высота']
        optionsScheme = ['ТипПолотна', 'ТолщинаДвери', 'Покрытие', 'СторонаОткрывания', 'Цвет', 'Материал', 'ВариантСтекла']
        keyValue=item[key]
        if key in optionsScheme and isinstance(keyValue, str):
            if key == 'СторонаОткрывания':
                key =  'Сторона открывания'
            elif key == 'ВариантСтекла':
                key =  'Вариант стекла'
            elif key == 'ТолщинаДвери':
                key =  'Толщина двери'
            elif key == 'ТипПолотна':
                key =  'Тип полотна'
            ## Опция
            if key not in products[sku]['options']:
                products[sku]['options'][key] = {
                    'name': key,
                    'values': [],
                    'images': [],
                }

            if not isinstance(keyValue, str):
                exit()
            products[sku]['offers'][id]['options'].append({'n': key, 'v': keyValue})

            img = ''
            if keyValue in options:
                img = options[keyValue]

            if keyValue not in products[sku]['options'][key]['values']:
                products[sku]['options'][key]['values'].append(keyValue)
                products[sku]['options'][key]['images'].append(img)


for sku in products:
    product = products[sku]

    for offerId in product['offers']:
        pr = product['offers'][offerId]
        offerOptions = pr['options']

        otionsCleared = []
        for opt in offerOptions:
            optOrign = len(product['options'][ opt['n'] ]['values'])
            if opt['n'] in offersScheme:
                otionsCleared.append(opt['n']+ ':' + opt['v'])

        products[sku]['offers'][offerId]['options'] = otionsCleared

    if 'oimgs' not in product:
        products[sku]['oimgs'] = {}

    for offerId in product['offers']:
        pr = product['offers'][offerId]
        img = pr['image']
        if img not in products[sku]['oimgs']:
            products[sku]['oimgs'][img] = pr


    product['offers'] = products[sku]['oimgs']
    products[sku]['oimgs'] = {}
    for optionKey in product['options']:
        vals = product['options'][optionKey]['values']

        product['options'][optionKey]['values'] = ';'.join(vals)
        product['options'][optionKey]['images'] = ';'.join(product['options'][optionKey]['images'])

    #print(product)
    #exit()


jsonResGlobal['count'] = len(products)
pos = 1
all = len(products)

with open(DIR_ROOT+'/admin/uploads/data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

for itemKey in products:
    item = products[itemKey]
    col = 0
    colOffers = 0
    if(row == 0):
        for headerTitle in item.keys():
            worksheet.write(row, col, headerTitle)
            col += 1
        col = 0
        row = 1
    for key in item.keys():
        value = item[key]
        if key == 'options':
            col += 5
            options = item['options']
            for optionkey in options:
                option = options[optionkey]
                worksheet.write_string(row, col, str(option['name']))
                col += 1
                worksheet.write_string(row, col, str(option['values']))
                col += 1
                worksheet.write_string(row, col, str(option['images']))
                col += 2
        elif key not in ['offers', 'oimgs'] :
            worksheet.write_string(row, col, str(value))
            col += 1
    row += 1
    pos+=1

workbook.close()

###
### Сохраняем
###
jsonResGlobal['success'] = 1
json_object = json.dumps(jsonResGlobal, indent = 4)
print(json_object)
