# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:01:30 2024

@author: EVOO
"""

class User :
    def __init__(self,ism, familiya, email, tel_raqam):
        self.ism=ism
        self.familiya=familiya
        self.email=email
        self.tel_raqam=tel_raqam
    def get_name(self):
        return self.ism
    def get_surname(self):
        return self.familiya
    def malumot(self):
        return (f"foydalanuvchi haqida malumot:\n"
                f"ismi {self.ism}\n"
                f"familiyasi {self.familiya}\n"
                f"emaili {self.email}\n"
                f"telefon raqami {self.tel_raqam}\n"
                )


ishlatuvchi1=User("Xasan", 'Sodiqov', 'sodiqovxasan99@gmail.com', 998901370571)
print(ishlatuvchi1.malumot())