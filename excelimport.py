# import requests
# import time
# import xlsxwriter
# from pathlib import Path
# import csv
# import json
# import os
# import pandas as pd


# ###
# jsonResGlobal = {}
# ###

# DIR = os.path.dirname(__file__)
# DIR_ROOT = os.path.dirname(DIR)


# options = {}
# with open(DIR+'/options.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     for rows in reader:
#         options[rows[0]] = rows[5]

# categories = []

# readExcel = pd.read_excel(DIR+'/import_excel.xlsx', header=None, na_filter = False)
# items = readExcel.values

# pPrices = {}
# if (len(items)):
#     for rows in items:

#         if(rows[0] == 'Артикул'):
#             continue

#         # ['0-Внешний код; 1-Артикул; 2-Наименование номенклатуры; 3-ВидНоменклатуры;4-ЕдиницаИзмерения;5-Бренд;6-Тип;7-Серия;8-Модель;9-Цвет;10-Высота;11-Ширина;12-Толщина;13-Стекло;13-Эксклюзив;14-Стиль;15-Путь к фото;16-Цена ЦФО Оптовая;Цена СЗФО Оптовая;Цена СФО Оптовая;Цена ЮФО Оптовая;Цена УФО Оптовая;Цена ЦФО Розница;Цена СЗФО Розница;Цена СФО Розница;Цена ЮФО Розница;Цена УФО Розница;Цена ДВФО Розница;']


#         if rows[0] not in pPrices:
#             pPrices[ rows[0] ] = [ ]

#         pPrices[ rows[0] ].append( rows[15] )
#         attrsOpt = []

#         color = ''
#         if(rows[5] and str(rows[5]) != 'nan' and str(rows[5]).strip() != ''):
#             color = str(rows[5]).strip()
#             attrsOpt.append(color)


#         mir = ''
#         if(rows[9] and str(rows[9]) != 'nan' and str(rows[9]).strip() != ''):
#             mir = str(rows[9]).strip()
#             attrsOpt.append(mir)


#         vstav = ''
#         if(str(rows[11]) and str(rows[11]) != 'nan'  and str(rows[11]).strip() != '') :
#             vstav = str(rows[11]).strip()
#             attrsOpt.append(vstav)

#         data = {
#             'ID': rows[0],
#             'IDBase': rows[0],
#             'Артикул': rows[0],
#             'НоменклатурнаяГруппа': '',
#             'Наименование': rows[1],
#             'ПолноеНаименование': rows[1],
#             'СсылкаНаКартинку': rows[14],
#             'ТипПолотна': '',
#             'Толщина': rows[8],
#             'Покрытие': rows[10],
#             'СторонаОткрывания': '',
#             'Ссылка': '',
#             'Раздел': rows[0],
#             'Серия': rows[3],
#             'Цвет': color,
#             'Материал':'',
#             'Ширина': rows[7],
#             'Бренд': rows[2],
#             'ВариантСтекла': mir,
#             'Высота': rows[6],
#             'Цена': rows[15],
#             'Стиль': rows[10],
#             'Вставка': vstav,
#             'Описание': rows[16],
#         }

#         iID = data['ID']
#         if(len(attrsOpt)):
#             iID += '-'
#             iID += '-'.join(str(x) for x in attrsOpt)

#         data['IDBase'] = iID
#         categories.append(data)

# ###
# workbook = xlsxwriter.Workbook(DIR_ROOT+'/admin/uploads/1.xlsx')
# worksheet = workbook.add_worksheet()
# ###
# row = 0
# start_time = time.time()



# products = {

# }



# for item in categories:
#     id = item['IDBase']
#     sku = item['Артикул']

#     priceOpt = item['Цена']

#     if sku not in products:
#         products[sku] = {
#             'sku': item['Артикул'],
#             'cat': item['НоменклатурнаяГруппа'],
#             'name': item['ПолноеНаименование'],
#             'images': item['СсылкаНаКартинку'],
#             'cat3': item['Серия'],
#             'price': min(pPrices[sku]),
#             'discountPrice': 0,
#             'manufacturer': 'profildors',
#             'count': '',
#             'h1': 'ПРОФИЛЬ ДОРС ' + item['Артикул'],
#             'tmp1': 3999,
#             'tmp2': item['Описание'],
#             'options': { },
#             'offers': { },
#     }

#     offerOptions = {

#     }

#     products[sku]['offers'][id]={
#         'id': id,
#         'options': [],
#         'image': item['СсылкаНаКартинку'],
#     }

#     offersScheme = ['Вариант стекла', 'Цвет', 'Вставка']

#     for key in item:
#         skipProps = ['Ссылка', 'ID', 'Артикул', 'Наименование', 'Раздел', 'НоменклатурнаяГруппа', 'Серия', 'Бренд', 'Цена', 'СсылкаНаКартинку', 'ПолноеНаименование', 'Ширина', 'Высота']
#         optionsScheme = ['ТипПолотна', 'Толщина', 'Покрытие', 'СторонаОткрывания', 'Цвет', 'Материал', 'ВариантСтекла', 'Вставка']
#         keyValue=item[key]
#         if key in optionsScheme and isinstance(keyValue, str):
#             if key == 'СторонаОткрывания':
#                 key =  'Сторона открывания'
#             elif key == 'ВариантСтекла':
#                 key =  'Вариант стекла'
#             elif key == 'Толщина':
#                 key =  'Толщина двери'
#             elif key == 'ТипПолотна':
#                 key =  'Тип полотна'
#             elif key == 'Вставка':
#                 key =  'Вставка'
#             ## Опция
#             if key not in products[sku]['options']:
#                 products[sku]['options'][key] = {
#                     'name': key,
#                     'values': [],
#                     'images': [],
#                     'prices': [],
#                 }

#             if not isinstance(keyValue, str):
#                 exit()
#             products[sku]['offers'][id]['options'].append({'n': key, 'v': keyValue})

#             img = ''
#             if keyValue in options:
#                 img = options[keyValue]

#             if keyValue not in products[sku]['options'][key]['values']:
#                 products[sku]['options'][key]['values'].append(keyValue)
#                 products[sku]['options'][key]['images'].append(img)

# for sku in products:
#     product = products[sku]

#     for offerId in product['offers']:
#         pr = product['offers'][offerId]
#         offerOptions = pr['options']

#         otionsCleared = []
#         for opt in offerOptions:
#             optOrign = len(product['options'][ opt['n'] ]['values'])
#             if opt['n'] in offersScheme:
#                 otionsCleared.append(opt['n']+ ':' + opt['v'])

#         products[sku]['offers'][offerId]['options'] = otionsCleared

#     if 'oimgs' not in product:
#         products[sku]['oimgs'] = {}

#     for offerId in product['offers']:
#         pr = product['offers'][offerId]
#         img = pr['image']
#         if img not in products[sku]['oimgs']:
#             products[sku]['oimgs'][img] = pr


#     product['offers'] = products[sku]['oimgs']
#     products[sku]['oimgs'] = {}

#     minP = min(pPrices[sku])

#     for optionKey in product['options']:
#         vals = product['options'][optionKey]['values']
#         product['options'][optionKey]['values'] = ';'.join(vals)
#         product['options'][optionKey]['images'] = ';'.join(product['options'][optionKey]['images'])

#         product['options'][optionKey]['prices'] = ';'.join(str(x-minP) for x in pPrices[sku])

#     #print(product)
#     #exit()

# jsonResGlobal['count'] = len(products)
# pos = 1
# all = len(products)

# with open(DIR_ROOT+'/admin/uploads/data.json', 'w', encoding='utf-8') as f:
#     json.dump(products, f, ensure_ascii=False, indent=4)

# for itemKey in products:
#     item = products[itemKey]
#     col = 0
#     colOffers = 0
#     if(row == 0):
#         for headerTitle in item.keys():
#             worksheet.write(row, col, headerTitle)
#             col += 1
#         col = 0
#         row = 1
#     for key in item.keys():
#         value = item[key]
#         if key == 'options':
#             col += 5
#             options = item['options']
#             for optionkey in options:
#                 option = options[optionkey]
#                 worksheet.write_string(row, col, str(option['name']))
#                 col += 1
#                 worksheet.write_string(row, col, str(option['values']))
#                 col += 1
#                 worksheet.write_string(row, col, str(option['images']))
#                 col += 1
#                 worksheet.write_string(row, col, str(option['prices']))
#                 col += 2
#         elif key not in ['offers', 'oimgs'] :
#             worksheet.write_string(row, col, str(value))
#             col += 1
#     row += 1
#     pos+=1

# workbook.close()

# ###
# ### Сохраняем
# ###
# jsonResGlobal['success'] = 1
# json_object = json.dumps(jsonResGlobal, indent = 4)
# print(json_object)

import requests
import time
import xlsxwriter
from pathlib import Path
import csv
import json
import os
import pandas as pd


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

categories = []

readExcel = pd.read_excel(DIR+'/import_excel.xlsx')
items = readExcel.values

pPrices = {}
if (len(items)):
    for rows in items:

        if(rows[0] == 'Артикул'):
            continue

        # ['0-Внешний код; 1-Артикул; 2-Наименование номенклатуры; 3-ВидНоменклатуры;4-ЕдиницаИзмерения;5-Бренд;6-Тип;7-Серия;8-Модель;9-Цвет;10-Высота;11-Ширина;12-Толщина;13-Стекло;13-Эксклюзив;14-Стиль;15-Путь к фото;16-Цена ЦФО Оптовая;Цена СЗФО Оптовая;Цена СФО Оптовая;Цена ЮФО Оптовая;Цена УФО Оптовая;Цена ЦФО Розница;Цена СЗФО Розница;Цена СФО Розница;Цена ЮФО Розница;Цена УФО Розница;Цена ДВФО Розница;']


        if rows[0] not in pPrices:
            pPrices[ rows[0] ] = [ ]


        pPrices[ rows[0] ].append( rows[15] )
        attrsOpt = []

        color = ''
        if(rows[5] and str(rows[5]) != 'nan' and str(rows[5]).strip() != ''):
            color = str(rows[5]).strip()
            attrsOpt.append(color)


        mir = ''
        if(rows[9] and str(rows[9]) != 'nan' and str(rows[9]).strip() != ''):
            mir = str(rows[9]).strip()
            attrsOpt.append(mir)


        vstav = ''
        if(str(rows[11]) and str(rows[11]) != 'nan'  and str(rows[11]).strip() != '') :
            vstav = str(rows[11]).strip()
            attrsOpt.append(vstav)

        data = {
            'ID': rows[0],
            'IDBase': rows[0],
            'Артикул': rows[0],
            'НоменклатурнаяГруппа': '',
            'Наименование': rows[1],
            'ПолноеНаименование': rows[1],
            'СсылкаНаКартинку': rows[14],
            'ТипПолотна': '',
            'Толщина': rows[8],
            'Покрытие': rows[10],
            'СторонаОткрывания': '',
            'Ссылка': '',
            'Раздел': rows[0],
            'Серия': rows[3],
            'Цвет': color,
            'Материал':'',
            'Ширина': rows[7],
            'Бренд': rows[2],
            'ВариантСтекла': mir,
            'Высота': rows[6],
            'Цена': rows[15],
            'Стиль': rows[10],
            'Вставка': vstav,
            'Описание': rows[16],
        }

        iID = data['ID']
        if(len(attrsOpt)):
            iID += '-'
            iID += '-'.join(str(x) for x in attrsOpt)

        data['IDBase'] = iID
        categories.append(data)

###
workbook = xlsxwriter.Workbook(DIR_ROOT+'/admin/uploads/1.xlsx')
worksheet = workbook.add_worksheet()
###
row = 0
start_time = time.time()



products = {

}



for item in categories:
    id = item['IDBase']
    sku = item['Артикул']

    priceOpt = item['Цена']

    if sku not in products:
        products[sku] = {
            'sku': item['Артикул'],
            'cat': item['НоменклатурнаяГруппа'],
            'name': item['ПолноеНаименование'],
            'images': item['СсылкаНаКартинку'],
            'cat3': item['Серия'],
            'price': min(pPrices[sku]),
            'discountPrice': 0,
            'manufacturer': 'profildors',
            'count': '',
            'h1': 'ПРОФИЛЬ ДОРС ' + item['Артикул'],
            'tmp1': 3999,
            'tmp2': item['Описание'],
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

    offersScheme = ['Вариант стекла', 'Цвет', 'Вставка']

    for key in item:
        skipProps = ['Ссылка', 'ID', 'Артикул', 'Наименование', 'Раздел', 'НоменклатурнаяГруппа', 'Серия', 'Бренд', 'Цена', 'СсылкаНаКартинку', 'ПолноеНаименование', 'Ширина', 'Высота']
        optionsScheme = ['ТипПолотна', 'Толщина', 'Покрытие', 'СторонаОткрывания', 'Цвет', 'Материал', 'ВариантСтекла', 'Вставка']
        keyValue=item[key]
        if key in optionsScheme and isinstance(keyValue, str):
            if key == 'СторонаОткрывания':
                key =  'Сторона открывания'
            elif key == 'ВариантСтекла':
                key =  'Вариант стекла'
            elif key == 'Толщина':
                key =  'Толщина двери'
            elif key == 'ТипПолотна':
                key =  'Тип полотна'
            elif key == 'Вставка':
                key =  'Вставка'
            ## Опция
            if key not in products[sku]['options']:
                products[sku]['options'][key] = {
                    'name': key,
                    'values': [],
                    'images': [],
                    'prices': [],
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

    minP = min(pPrices[sku])

    for optionKey in product['options']:
        vals = product['options'][optionKey]['values']
        product['options'][optionKey]['values'] = ';'.join(vals)
        product['options'][optionKey]['images'] = ';'.join(product['options'][optionKey]['images'])

        product['options'][optionKey]['prices'] = ';'.join(str(x-minP) for x in pPrices[sku])

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
                col += 1
                worksheet.write_string(row, col, str(option['prices']))
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


