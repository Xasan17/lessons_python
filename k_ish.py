# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:27:03 2024

@author: EVOO
"""

import datetime as dt
from dateutil.relativedelta import relativedelta
import re

# for i in  range(10) :
#     bugun=dt.date.today()
#     x=14
#     keyingi_2hafta=bugun+dt.timedelta(days=i*x)
#     print(keyingi_2hafta)
    
# ramazon=dt.date(2021,4,13)
# kurbon_hayit=dt.date(2021,6,22)
# farq=kurbon_hayit-ramazon
# print(farq)

# bugun=dt.date.today()
# t_kun=dt.date(2025,9,2)
# difference=relativedelta(t_kun,bugun)
# print(difference)
# print(f"{difference.months} month and {difference.days} days")

# nomerlar=[]

# while True:
#     raqam=input("telefon raqamingizni kiriting:\n")
#     phone_pattern = r'^\+998\d{9}$'
#     if re.match(phone_pattern, raqam) :
#         if raqam in nomerlar:
#             print("bunday raqam mavjud")
#         else:
#             nomerlar.append(raqam)
#             print("telefon raqamingiz bazaga kiritildi")
#     else:
#         print("Bunday raqam mavjut emas")
#     javob=input("yana nomer kiritasizmi ha(1)/yoq(0)")
#     if javob=='1' :
#         continue
#     elif javob=='0':
#         break

# print(nomerlar)

matn=("Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi:"
    " https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida "
    "klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz." 
    "Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test")

def web_check(text):
    urllar=[]
    url_pattern =r'https?://[a-zA-Z0-9./-]+'
    matches=re.findall(url_pattern, text)
    if matches :
        urllar.extend(matches)
        return urllar
    else:
        return "textda web saxifaga yonaltiradigan url yo'q"


result=web_check(matn)
print(result)



