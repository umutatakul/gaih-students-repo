# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:08:18 2021

@author: Atakul
"""
import random

AsalListe=[]

for a in range (2,101):
    flag=False
    for b in range (2,a):
        if(a%b==0):
            flag=True        
    if (not flag):
        AsalListe.append(a)
        
        
        


matris =[["a", "b", "c"],["d", "e", "f"], ["g", "h", "i"]]

for i in range(0,3):
    for j in range (0,3):
        sayiuretici = AsalListe [random.randint (0,len(AsalListe)-1)]
        matris [i][j]=sayiuretici
        
               
                