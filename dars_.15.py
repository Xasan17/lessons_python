# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 06:28:32 2024

@author: EVOO
"""

# def katta_harf(matnlar):
#     matnlar=matnlar[:]
#     matnlar=[matn.capitalize() for matn in matnlar]
#     return matnlar

# talabalar=['ali','vali','hasan', 'husan' ]
# katta=katta_harf(talabalar)
# print(katta)
# print(talabalar)

def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=int(input(f"{ism} ning bahosini kiriting: "))
        baholar[ism]={baho}
    return baholar
talabalar=['ali','vali','hasan', 'husan' ]
katta=bahola(talabalar)
print(katta)
print(talabalar)