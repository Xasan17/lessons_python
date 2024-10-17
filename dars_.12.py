# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:07:17 2024

@author: EVOO
"""

# print("qaysi maxsulotlarni sotib olmoqchisiz tugatmoqchi bolsangiz exit ni yozing")
# savat=[]
# ishora=True
# n=1
# while ishora:
#     maxsulot=input(f"{n} mahsulotni yozing: ")
#     if maxsulot.lower()=='exit' :
#        break
#     savat.append(maxsulot)
#     n+=1
# print(f"sizning savatdagi mahsulotlaringiz")
# for tovar in savat :
#     print(f"{tovar}")


print("qaysi maxsulotlarni sotib olmoqchisiz. Tugatmoqchi bolsangiz exit ni yozing")
savat={}
n=1
while True:
    maxsulot=input(f"{n} mahsulotni yozing: ")
    narx=input(f"{maxsulot} mahsulotni narxini yozing yozing: ")
    savat[maxsulot]=narx
    n+=1
    javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
    if javob != 'ha':
        break
s=0
for maxsulot,narx in savat.items():
    s=s+int(narx)
    print(f'{maxsulot} ning narxi {narx}')
print(f"jami: {s} so'm")
    