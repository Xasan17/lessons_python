# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:01:25 2024

@author: EVOO
"""
# a=int(input("Juft son kiriting:\n>>>"))
# if a%2==0 :
#     print("Rahmat!")
# else:
#     print("Bu son juft emas")

# yosh=int(input("Yoshingizni kiriting:"))
# if yosh <4 or yosh>60 :
#     print('Muzey siz uchun bepul')
# elif yosh<18 :
#     print('Bilet narhi 10000 s\'om')
# else:
#     print('Bilet narhi 20000 s\'om')

# a=int(input("1-chi sonni kiriting:"))
# b=int(input("2-chi sonni kiriting:"))
# if a==b :
#     print("Sonlar teng")
# elif a<b :
#     print("2-chi son katta")
# else:
#     print("1-chi son katta")


# mahsulotlar=["go'sht", "asal", "shakar", "novot", "qant", 
#              'shaftoli', 'kartoshka', 'sabzi', "qovin", "tarvuz"]
# print("savatga kamida 5 ta mahsulot kiriting:")
# # a1=input('1-chi mahsulot:')
# # a2=input('2-chi mahsulot:')
# # a3=input('3-chi mahsulot:')
# # a4=input('4-chi mahsulot:')
# # a5=input('5-chi mahsulot:')
# savat=[input('1-chi mahsulot:'), input('2-chi mahsulot:'),
# input('3-chi mahsulot:'), input('4-chi mahsulot:'),
# input('5-chi mahsulot:')]
# print(savat)
# for mahsulot in savat:
#     if mahsulot in mahsulotlar :
#         print(f"{mahsulot} do'konimizda bor")
#     else:
#         print(f"{mahsulot} do'konimizda yo'q")

# mahsulotlar=["go'sht", "asal", "shakar", "novot", "qant", 
#              'shaftoli', 'kartoshka', 'sabzi', "qovin", "tarvuz"]
# print("savatga kamida 5 ta mahsulot kiriting:")
# savat=[]
# mahsulot_borlar=[]
# mahsulot_yoqlar=[]
# for n in range(5): 
#     savat.append(input(f"{n+1}-chi mahsulot:")) 
# for mahsulot in savat:
#     if mahsulot in mahsulotlar :
#         mahsulot_borlar.append(mahsulot)   
#     else:
#        mahsulot_yoqlar.append(mahsulot)
# if mahsulot_yoqlar==[] :
#     print("Hamma mahsulotlar dokonimizda bor")
# else:
#     print(f"Do'konimizda quyidagi mahsulotlar yo'q:\n{mahsulot_yoqlar} ")


# foydalanuvchilar=['xasan17', 'alisher1999', 'nodir23', '24akmal', 'boxodir2000']
# login=input('loginingizni yozing:')
# if login.lower() in foydalanuvchilar :
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {login.title()} !")

son=int(input('Istalgan sonni kiriting:'))
for n in range(2,11):
    if son%n==0 :
        input(f"{son}-soni {n} soniga qoldiqsiz bolinadi.")

        
    
    
    
    
    
    
    
    