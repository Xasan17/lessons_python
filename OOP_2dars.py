# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 07:32:28 2024

@author: EVOO
"""

class Avto():
    def __init__(self, model, rang, korobka, narh):
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narh=narh
        self.killometr=0
    def get_model(self) :
        return self.model
    
    def get_rang(self) :
        return self.rang
    
    def get_korobka(self) :
        return self.korobka
    
    def get_narx(self) :
        return self.narx
    
    def get_info(self):
        return (f"Avtomobilni modeli {self.model} rangi {self.rang} "
                f"{self.korobka} toliq narxi {self.narh} probegi {self.killometr} km")
    
    def set_model(self, yangi_model) :
        self.model=yangi_model
    
    def set_rang(self, yangi_rang) :
        self.rang=yangi_rang
    
    def set_korobka(self, yangi_korobka) :
        self.korobka=yangi_korobka
    
    def set_narh(self, yangi_narh) :
        self.narh=yangi_narh
    
    def update_killometr(self, yangi_killometr) :
        self.killometr=yangi_killometr
    


class Avtosalon():
    def __init__(self, salon_nom, manzil):
        self.salon_nom=salon_nom
        self.manzil=manzil
        self.avtolar=[]
    
    def get_salon_nom(self) :
        return self.salon_nom
    
    def get_manzil(self) :
        return self.manzil
    
    def add_avto(self, avto):
        self.avtolar.append(avto)
    
    def get_avto(self) :
        return [x.get_info() for x in self.avtolar]


avtomobil1=Avto('malibu', 'qora', 'avtomat', '23000$')
gm=Avtosalon('GM', "Toshkent")
gm.add_avto(avtomobil1)

def see_methods(klass) :
    return[method for method in dir(klass) if method.startswith('__')  is False ]
    
  
    
    