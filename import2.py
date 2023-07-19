# import requests
# import time
# import xmltodict
# import xlsxwriter
# import csv
# from pathlib import Path

# path = Path('orgin.xml')
# if(path.is_file()):
#     with open('orgin.xml', 'r') as f:
#         xmlData = f.read()
# else:
#     exit()


# with open('options.csv', mode='r') as infile:
#     reader = csv.reader(infile)

# print(reader)
# exit


# print('Парсинг кол-во ' + str(len(categories)))
# print('Начинаем разбор товаров')
# pos = 1
# all = len(my_dict)

# ###
# workbook = xlsxwriter.Workbook('price.xlsx')
# worksheet = workbook.add_worksheet()
# ###
# row = 0
# start_time = time.time()

# products = {

# }
# for item in categories:
#     id = item['ID']
#     sku = item['Раздел']
#     if sku not in products:
#         products[sku] = {
#             'sku': item['Раздел'],
#             'cat': item['НоменклатурнаяГруппа'],
#             'cat3': item['Серия'],
#             'options': {

#             },
#             'manufacturer': 'profildors',
#             'tmp1': '',
#             'tmp2': '',
#             'tmp3': '',
#             'tmp4': ''
#     }

#     attrs = []
#     for key in item:
#         skipProps = ['Ссылка', 'ID', 'Артикул', 'Наименование', 'Раздел', 'НоменклатурнаяГруппа', 'Серия', 'Бренд', 'Цена', 'СсылкаНаКартинку', 'ПолноеНаименование']
#         attrsScheme = ['ТипПолотна', 'ТолщинаДвери', 'Покрытие', 'СторонаОткрывания', 'Цвет', 'Материал', 'Ширина', 'ВариантСтекла', 'Высота']
#         keyValue=item[key]
#         if key in attrsScheme:
#             if key not in products[sku]['options']:
#                 products[sku]['options'][key] = {'name': key, 'values': []}


#             products[sku]['options'][key]['values'].append(keyValue)
#         elif key not in skipProps:
#             print('******' + key )

#     print(products[sku])
#     exit()
#     product = {
#             'id': id,

#             'price':item['Цена'],
#             'discountPrice': 0,
#             'name': item['ПолноеНаименование'],
#             'description': '',
#             'images': item['СсылкаНаКартинку'],

#             'attrs': attrs,

#         }
#     products.append(product)

# for item in products:

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
#         if key == 'attrs':
#             for attr in value:
#                 worksheet.write_string(row, col, str( attr['name'] ))
#                 col += 1
#                 worksheet.write_string(row, col, str( attr['value'] ))
#                 col += 1
#         else:
#             worksheet.write_string(row, col, str(value))
#             col += 1
#     row += 1

#     print('Строка %s, Общий процесс %s за %s '  % (row, (pos*100/all), time.time()-start_time)  )
#     #items.append(item)
#     pos+=1

# print('сохраняем')
# workbook.close()


import requests
import time
import xmltodict
import xlsxwriter
import csv
from pathlib import Path

path = Path('orgin.xml')
if(path.is_file()):
    with open('orgin.xml', 'r') as f:
        xmlData = f.read()
else:
    exit()


with open('options.csv', mode='r') as infile:
    reader = csv.reader(infile)

print(reader)
exit


print('Парсинг кол-во ' + str(len(categories)))
print('Начинаем разбор товаров')
pos = 1
all = len(my_dict)

###
workbook = xlsxwriter.Workbook('price.xlsx')
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
            'cat3': item['Серия'],
            'options': {

            },
            'manufacturer': 'profildors',
            'tmp1': '',
            'tmp2': '',
            'tmp3': '',
            'tmp4': ''
    }

    attrs = []
    for key in item:
        skipProps = ['Ссылка', 'ID', 'Артикул', 'Наименование', 'Раздел', 'НоменклатурнаяГруппа', 'Серия', 'Бренд', 'Цена', 'СсылкаНаКартинку', 'ПолноеНаименование']
        attrsScheme = ['ТипПолотна', 'ТолщинаДвери', 'Покрытие', 'СторонаОткрывания', 'Цвет', 'Материал', 'Ширина', 'ВариантСтекла', 'Высота']
        keyValue=item[key]
        if key in attrsScheme:
            if key not in products[sku]['options']:
                products[sku]['options'][key] = {'name': key, 'values': []}


            products[sku]['options'][key]['values'].append(keyValue)
        elif key not in skipProps:
            print('******' + key )

    print(products[sku])
    exit()
    product = {
            'id': id,

            'price':item['Цена'],
            'discountPrice': 0,
            'name': item['ПолноеНаименование'],
            'description': '',
            'images': item['СсылкаНаКартинку'],

            'attrs': attrs,

        }
    products.append(product)

for item in products:

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
        if key == 'attrs':
            for attr in value:
                worksheet.write_string(row, col, str( attr['name'] ))
                col += 1
                worksheet.write_string(row, col, str( attr['value'] ))
                col += 1
        else:
            worksheet.write_string(row, col, str(value))
            col += 1
    row += 1

    print('Строка %s, Общий процесс %s за %s '  % (row, (pos*100/all), time.time()-start_time)  )
    #items.append(item)
    pos+=1

print('сохраняем')
workbook.close()

