# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:43:20 2021

@author: Atakul
"""

import operator

sayac=0
isimler=[]
soyadlar = []
vizeler = []
finaller = []
odevler = []
kimlikbilgileri = []
notortalamalari = []

while (sayac<5):
    isim = input("Öğrenci Adı:")
    soyad= input("Öğrenci Soyadı:")
    vize= int(input("Vize Notu:"))
    final = int(input("Final Notu:"))
    odev = int(input("Ödev Notu:"))
    
    isimler.append(isim)
    soyadlar.append(soyad)
    vizeler.append(vize)
    finaller.append(final)
    odevler.append (odev)
    
    sayac=sayac+1
    

for i in range (len(isimler)):
    kimlikbilgileri.append(isimler[i]+" "+soyadlar[i])
    
for a in range (len(vizeler)):
    notortalamalari.append((vizeler[a]+finaller[a]+odevler[a])/3)
    

notort= dict(zip(kimlikbilgileri,notortalamalari))

sirali=sorted(notort.items(),reverse=True,key=operator.itemgetter(1))


print ("Tebrikler ", sirali [0] [0], "!", sirali[0][1] , "aldınız")