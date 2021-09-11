# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:23:38 2021

@author: Usuario
"""
"""
1. Hacer un algoritmo que calcule el total a pagar por la compra de
camisas. Si se compran tres camisas o mas se aplica un descuento
del 30% sobre el total de la compra y si son menos de tres camisas
un descuento del 10%.
"""
valor_camisa = float(input('Digite el valor de la camisa : $ '))
numero_Camisa = int(input('Digite la cantidad de camisa que desea comprar : '))
if(numero_Camisa >= 3):
    total_camisa = valor_camisa * numero_Camisa
    descuento = total_camisa * 0.30
    total_pago = total_camisa - descuento
    print(f'El valor total que debe pagar es de : ${total_pago} ')
elif(numero_Camisa < 3):
    total_camisa = valor_camisa * numero_Camisa
    descuento_dos = total_camisa * 0.10
    total_pagar =  total_camisa - descuento_dos
    print (f'El valor total que debe pagar es de : ${total_pagar}')
