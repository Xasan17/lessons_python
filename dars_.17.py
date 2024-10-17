# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:21:27 2024

@author: EVOO
"""
import random as r
print("Keling oylangan sonni topish oynaymiz")
def game():
    ishora=True
    n=1
    son=r.randint(1, 10)
    a=int(input("1 dan 10 gacha son oyladim. Topa olasizmi?: "))
    while ishora:
        if son>a :
            a=int(input(f"Xato men oylagan son kattaroq. Yana urunib koring: "))
            n+=1
        elif son<a :
            a=int(input("Xato men oylagan son kichikroq. Yana urunib koring: "))
            n+=1
        else:
            print(f"TOPTINGIZ! {son} sonini oylagan edim. {n} ta taxmin bilan toptingiz. Tabriklayman!!")
            print("1 dan 10 gacha son oylang men topishga harakat qilaman.")
            input("Son oylagan bolsangiz istalgan tugmani bosing")
            m=1
            pastki_chegara=1
            tepadagi_chegara=10
            tahmin=r.randint(pastki_chegara,tepadagi_chegara)
            while True:
                b=input(f"Siz {tahmin} sonini oyladingiz: to'g'ri (t), "
                         f"men oylagan son kattaroq (+), yoki kichikroq (-)?? ")
                if b=="+" :
                    pastki_chegara=tahmin+1
                    tahmin=r.randint(pastki_chegara,tepadagi_chegara)
                    m+=1
                elif b=="-" :
                    tepadagi_chegara = tahmin-1
                    tahmin=r.randint(pastki_chegara,tepadagi_chegara)
                    m+=1
                elif b=="t" :
                    if n<m:
                        print(f"Siz yutingiz!! Oylagan soningizni {m} tahmin bilan topdim")
                    elif n>m :
                        print(f"Men yutim!! Oylagan soningizni {m} tahmin bilan topdim")
                    else:
                        print(f"Durang!! Oylagan soningizni {m} tahmin bilan topdim")
                    return
                    
while True:
    game()
    taklif=input("Yana oynaysizmi ha(1)/yoq(0)?: ")
    if taklif=="1" :
        continue
    elif taklif=="0" :
            break
                    
                 
    
   
    
                