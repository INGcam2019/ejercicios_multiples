# -*- coding: utf-8 -*-
"""
Created on Tue May  3 18:35:18 2022

@author: Cami89
"""

#numero primo

primeMumber=int(input("enter a positive number"))
cont=0

if primeMumber>0:
    for i in range(1,primeMumber):
        
        if primeMumber%i==0:
            cont+=1
    if cont==1:
        print(f"{primeMumber} es un numero primo")
    else:
        print(f"{primeMumber} no es un numero primo")
else:
    print(f"{primeMumber} no es un numero positivo")