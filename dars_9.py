# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:00:39 2024

@author: EVOO
"""

# python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'}
# for key, values in sorted(python_words.items()):
#     print(f"kalit: {key}")
#     print(f"qiymat: {values}")

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}
# for davlat in sorted(davlatlar.keys()):
#     print(davlat.upper())
# for davlat in sorted(davlatlar.values()):
#     print(davlat.title())

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}
# davlat=input("Davlat nomini kiriting>>>").lower()
# poytaxt=davlatlar.get(davlat,'Bizda bunday ma\'lumot yo\'q')
# print(poytaxt.title())

menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input(f"{n+1} chi taom nomini yozing:").lower())
for taom in buyurtmalar :
    if taom in menu.keys() :
        print(f"{taom} narxi {menu[taom]} so'm ")
    else:
        print(f"bizda {taom} yo'q")

    




