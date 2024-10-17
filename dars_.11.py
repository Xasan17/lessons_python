# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 06:59:54 2024

@author: EVOO
"""

# savol="Yoktirgan kitobingizni kiriting:\n"
# savol+="Dasturni tugatish uchun stop ni yozing>>" 
# kitob=' '
# while kitob!='stop' :
#     kitob=input(savol)
#     if kitob!='stop':
#        print(f"{kitob} nomli kitobingiz kompyutirga saqlandi")
# print('Dastur muafaqiyatli tugatildi')


# yosh='yoshingizni kiriting:\n'
# yosh+="Dasturni tugatish uchun exit ni yozing>>"
# qiymat=' '
# while qiymat!='exit' :
#     qiymat=input(yosh)
#     if qiymat=='exit' :
#         print('Dastur muafaqiyatli tugatildi')
#         break
#     else:
#         if int(qiymat)<=7 :
#            print("bilet narhi 2000so'm")
#         elif int(qiymat)>7 and int(qiymat)<18 :
#            print("bilet narhi 3000so'm")
#         elif int(qiymat)>=18 and int(qiymat)<65 :
#            print("bilet narhi 1000so'm")
#         else:
#            print("siz uchun bilet narxi tekin")


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol) 
    if qiymat.lower()=='exit':
        print('Dastur muafaqiyatli tugatildi')
        break
    else:
        if float(qiymat)<0:
            continue
        else:
            ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
