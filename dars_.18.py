# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:52:56 2024

@author: EVOO
"""

from uzwords import words
import random

def get_word():
    word=random.choice(words)
    while "-" in word or " " in word:
        word=random.choice(words)
    return word.upper()
    
def display(user_letters,word):
    display_letter=""
    for letter in word :
        if letter in user_letters.upper() :
            display_letter+=letter
        else:
            display_letter+="_"
    return display_letter

def play() :
    word=get_word()
    word_letters=set(word)
    user_letters=""
    print(f"Men {len(word)} xonali soz oyladim. Topa olasizmi? kirilchada yozing! ")
    while len(word_letters)>0 :
        print (display(user_letters,word))
        if len(user_letters)>0 :
            print(f"Shu vaqtgacha kiritgan hariflariz {user_letters}")
        letter=input("Harf kiriting: ").upper()
        if letter in user_letters :
            print("Bu harifni oldin kiritgansiz. Boshqa harif kiriting")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harif togri.")
        else:
            print("Bunday harif yoq")
        user_letters+=letter
    print(f"Tabriklayman siz {word} sozni {len(user_letters)} ta urinishda toptingiz")

answer=1        
while answer:
    play()
    answer=int(input("Yana oynaysizmi ha(1)/yoq(0)"))