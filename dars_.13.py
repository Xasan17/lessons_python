# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:01:42 2024

@author: EVOO
"""

# def tugilgan_yil_hisob(ism,tugilgan_yil) :
#     """Tug'ilgan yilini hisoblaydigan funksiya"""
#     yosh=2024-int(tugilgan_yil)
#     print(f"{ism.title()} ning yoshi {yosh} da")
# tugilgan_yil_hisob(ism='xasan', tugilgan_yil=1999)

# def kvadkub_hisoblash(a):
#     """Kvadrati va kubini hisoblaydigan funksiya"""
#     print(f"(a) sonning kvadrati {a**2} ga teng" )
#     print(f"{a} sonning kubi {a**3} ga teng")


# kvadkub_hisoblash(5)


# def tok_juft_aniqlash(a):
#     """Tok yoki juftligini aniqlaydigan funksiya"""
#     if a%2==0:
#         print(f"{a} soni juft son" )
#     else:
#         print(f"{a} soni toq son" )

# tok_juft_aniqlash(1222256875)


def katta_soni_aniqlash(a,b):
    """Katta soni aniqlaydigan funksiya"""
    if a>b:
        print(f"{a} soni katta" )
    elif a==b:
        print(f"sonlar teng" )
    else:
        print(f"{b} soni katta")


katta_soni_aniqlash(5, 10)