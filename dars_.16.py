# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 07:09:20 2024

@author: EVOO
"""

# def kopaytirma(*sonlar):
#     kopaytma=1
#     for son in sonlar:
#         kopaytma=kopaytma*son
#     return kopaytma

# x=kopaytirma(1,2,5)
# print(x)


def anketa(familiya,ism,**malumotlar):
    malumotlar['familiya']=familiya
    malumotlar['ism']=ism
    return malumotlar

talabalar=anketa('sodiqov', 'xasan', email='sodiqovxasan99',nomer=901370571)
print(talabalar)