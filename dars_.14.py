# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:39:29 2024

@author: EVOO
"""

# def mijoz_info( ism, familiya, tyil, tjoy, email='', telefon=None):
#     info={
#         'ism': ism,
#         'familiya': familiya,
#         'tugilgan_yili': tyil,
#         'tugilgan joyi': tjoy,
#         'email': email,
#         'telefon': telefon}
#     return info


# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
#           f"{2024-mijoz['tugilgan_yili']} yoshda, telefoni: {mijoz['telefon']}")




# def tekshirish(x,y,z):
#     if x>y and x>z :
#         print(f"eng katta son bu {x}")
#     elif y>z and y>x :
#         print(f"eng katta son bu {y}")
#     elif z>y and z>x:
#         print(f"eng katta son bu {z}")


# tekshirish(5,6,7)





# def kattasi(x,y,z) :
#     max=x
#     if y>=max:
#         max=y
#     if z>=max:
#         max=z
#     return max
# kata_son=kattasi(5, 6, 7)
# print(kata_son)







# def aylan_parametrlari(r):
#     aylana={
#         'radiusi':r,
#         'diametr':r*2,
#         'perimetr':2*3.14*r,
#         'yuzasi':3.14*r**2
#         }
#     return aylana


# aylana=aylan_parametrlari(10)
# print(aylana)



# def tub_sonlar(min,max):
#     tub_sonlar=[]
#     for n in range(min,max+1):
#         ishora=True
#         if n==1 :
#             ishora=False
#         elif n==2:
#             ishora=True
#         else:
#             for x in range(2,n):
#                 if n%x==0 :
#                     ishora=False
#         if ishora:
#             tub_sonlar.append(n)
#     return tub_sonlar



# tub_sonlar=tub_sonlar(1, 20)
# print(tub_sonlar)     


# def tub_sonlar(min_val, max_val):
#     tub_sonlar = []
#     for n in range(min_val, max_val + 1):
#         ishora = True
#         if n < 2:
#             ishora = False
#         else:
#             for x in range(2, int(n**0.5) + 1):  # Проверяем делители до квадратного корня
#                 if n % x == 0:
#                     ishora = False
#                     break  # Прекращаем цикл, если нашли делитель
#         if ishora:
#             tub_sonlar.append(n)
#     return tub_sonlar

# # Пример использования
# tub_sonlar = tub_sonlar(1, 20)
# print(tub_sonlar)           



def fibonachi(n):
    x=1
    i=1
    y=1
    fibonachi=[x,y]
    for i in range(2,n):
        z=x+y
        x=y
        y=z
        fibonachi.append(z)
        i+=1
        
    return fibonachi


a=fibonachi(10)
print(a)

