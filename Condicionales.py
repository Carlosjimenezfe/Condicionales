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

"""    
2. En un supermercado se hace una promoción, mediante la cual el
cliente obtiene un descuento dependiendo de un número que se
escoge al azar. Si el número escogido es menor que 74 el descuento
es del 15% sobre el total de la compra, si es mayor o igual a 74 el
descuento es del 20%. Obtener cuanto dinero se le descuenta.
"""

valor_compra = float(input ('Digite el total de la compra : $  '))
numero_escogido = int(input ('Digite el numero escogido : '))
if (numero_escogido < 74):
    descuento = valor_compra * 0.15
    print (f'El descuento que se le hara es de  : ${descuento} ')
elif (numero_escogido >= 74):
    descuento_dos = valor_compra * 0.20
    print (f'El descuento que se le hara es de : ${descuento_dos}')

"""     
3. Una compañía de seguros está abriendo un departamento de
finanzas y estableció un programa para captar clientes, que conssite
en lo siguiente: Si el monto por el que se efectúa la fianza es menor
que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
es mayor que $50.000 la cuota a pagar será el 2% del monto. La
afianzadora desea determinar cual será la cuota que debe pagar al
cliente.
""" 
monto_fianza = float(input('Digite el monto de la fianza : $ '))
if(monto_fianza < 50000):
   cuota = monto_fianza * 0.03
   print (f'La cuota que debe pagar el cliente es de : ${cuota}')
elif (monto_fianza > 50000):
    cuota_dos = monto_fianza * 0.02
    print (f'La cuota que debe pagar el cliente es de : ${cuota_dos}')
