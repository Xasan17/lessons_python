# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:15:21 2024

@author: EVOO
"""

# oylaazolarim={'ot_ism': 'Abdurahmon', 'ot_t_yili': 1971, 'ot_yoshi': 46,
#               'on_ism': 'Aziza', 'on_t_yili': 1977, "on_yoshi": 46,
#               'uk_ism': 'Xusan', 'uk_t_yili': 1999, 'uk_yoshi': 25,}
# print(oylaazolarim['ot_ism'])


# yoqtirgan_taomlar={
#     "ali": 'osh',
#     'vali': 'chuchvara',
#     'g\'ani': 'shilpildo',
#     'alisher': 'shorva',
#     'xasan': 'manti'}

# sevimli=yoqtirgan_taomlar['ali']
# print(f"Alining sevimli taomi {sevimli.title()}")

python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
soz=input("Biron bir soz yozing:")
kalit=python_izohli_lugati.get(soz.lower(),'Bunday soz lugata mavjud emas')
print(kalit)

# if soz.lower() in python_izohli_lugati :
#     print(python_izohli_lugati[soz.lower()])
# else:
#     print("Lug'ata bunday soz yoq")

