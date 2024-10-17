# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 07:34:51 2024

@author: EVOO
"""

# ismlar=['Xasan', 'Xusan', 'Ali', 'Vali', "G'ani"]
# n=0
# for ism in ismlar:
#     n=n+1
#     print(f"Tabriklaymiz siz olimpiyadada galaba qozondingiz {ism}")
# print(f"kod {n} marta takrorlandi")  


# sonlar=list(range(11,100,2))
# son_kublari=[]
# for son in sonlar:
#     son_kublari.append(son**3)
# print(son_kublari)

# filmlar=[]
# print("5 ta eng yoktirgan filimlaringiz qaysi?")
# for n in range(5):
#     filmlar.append(input(f"{n+1}-filmingizni kiriting:"))
# print(filmlar)


uchrashuvlar=[]
i=int(input("bugun nechta odam bilan uchrashtingiz?"))
for n in range(i):
    uchrashuvlar.append(input(f"{n+1}-chi uchrashgan odam ismini kiriting:"))
print(uchrashuvlar)