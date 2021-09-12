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

"""    
4. Una fábrica ha sido sometida a un programa de control de
contaminación para lo cual se efectúa una revisión de los puntos de
contaminación generados por la fábrica. El programa de control de
contaminación consiste en medir los puntos que emite la fábrica en
cinco días de una semana y si el promedio es superior a los 170
puntos entonces tendrá la sanción de parar su producción por una
semana y una multa del 50% de las ganancias diarias cuando no se
detiene la producción. Si el promedio obtenido de puntos es de 170 o
menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
desea saber cuanto dinero perderá después de ser sometido a la
revisión.
"""
dinero_fabrica = float (input ('Digite la cantidad de dinero que tiene la fabrica : $ '))
punto_uno = float(input('Digite los puntos del dia uno : '))
punto_dos = float(input('Digite los puntos del dia dos : '))
punto_tres = float(input('Digite los puntos del dia tres : '))
punto_cuatro = float(input('Digite los puntos del dia cuatro : '))
punto_cinco = float(input('Digite los puntos del dia cinco : '))
promedio = (punto_uno + punto_dos + punto_tres + punto_cuatro + punto_cinco)/5
if (promedio > 170):
    descuento = dinero_fabrica * 0.50
    perdidas = dinero_fabrica + descuento
    print (f'El total de dinero que perdera la fabrica es de : ${perdidas}')
elif(promedio <= 170):
    print ('La fabrica no tendra ninguna perdida')
    
""" 
5. Una persona se encuentra con un problema de comprar un automóvil
o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
mientras el automóvil se devalúa, con el terreno sucede lo contrario.
Esta persona comprará el automóvil si al cabo de tres años la
devaluación de este no es mayor que la mitad del incremento del valor del terreno. Ayúdale a esta pesona a determinar si debe o no
comprar el automóvil.
""" 
precio = float (input('Digite el valor del terrono y el carro : $ '))
devaluo_carro = float (input('Digite el devaluo del carro por años : $ '))
incremento_terreno = float (input('Digite el incremenento del terreno por años : $ '))

comprar_automovil = (precio - (devaluo_carro * 3))
comprar_terreno = precio + (incremento_terreno * 3)
mitad = comprar_automovil / 2
if(comprar_automovil < mitad):
    print('Comprar el carro')
else:
    print ('Comprar el terreno')
    
"""
6. En una fábrica de computadoras se planea ofrecer a los clientes un
descuento que dependerá del número de computadoreas que
compre. Si las computadoras son menos de cinco se les dará un 10%
de descuento sobre el total de la compra; si el número de
computadoras es mayor o igual a cinco pero menos de diez se le
otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
precio de cada computadora es de $11.000.
"""


numero_pc = int (input('Digite el numero de pc compradas : '))
valor = numero_pc * 11000
if (numero_pc < 5):  
    descuento_uno = valor * 0.10
    total_uno = valor - descuento_uno
    print (f'El valor total que debe pagar el cliente es de : {total_uno}')
elif (numero_pc >= 5 and numero_pc <10):    
    descuento_dos = valor * 0.20
    total_dos = valor - descuento_dos
    print(f'El valor total que debe pagar el cliente es de : ${total_dos}')
else:
    descuento_tres = valor * 0.40
    total_tres = valor - descuento_tres
    print (f'El valor que debe pagar el cliente es de : ${total_tres} ')
    
"""    
7. Un proveedor de estéreos ofrece un descuento del 10% sobre el
precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
independientemente de esto, ofrece un 5% de descuento si la marca
es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
cualquiera por la compra de su aparato. IVA es del 16%.
"""
precio_producto = float( input('Digite el precio del producto : $ '))
marca_producto = input('Digite la marca del producto : ')
if(precio_producto >= 2000 and marca_producto == 'NOSY'):
    sin_iva = (precio_producto - (precio_producto*0.10))
    con_iva = (sin_iva * 0.16) + sin_iva
    marca_nosy = con_iva - (con_iva * 0.05)
    print (f'El total a pagar el producto NOSY es de : ${marca_nosy}')   
elif(precio_producto >= 2000 and marca_producto != 'NOSY'):
    sin_iva = (precio_producto - (precio_producto*0.10))
    con_iva = (sin_iva * 0.16) + sin_iva
    print (f'El total a pagar el producto de marca {marca_producto} : ${con_iva}')   
elif(precio_producto < 2000 and marca_producto == 'NOSY'):
   con_iva = (precio_producto * 0.16) + precio_producto
   marca_nosy = con_iva -(con_iva * 0.05)
   print (f'El total a pagar el producto NOSY es de : ${marca_nosy}') 
elif(precio_producto < 2000 and marca_producto != 'NOSY'):
   con_iva = (precio_producto * 0.16) + precio_producto   
   print (f'El total a pagar el producto de marca {marca_producto} : ${con_iva}')

""" 
8. Una empresa quiere hacer una compra de varias piezas de la misma
clase a una fábrica de refacciones. La empresa, dependiendo del
monto total de la compra, decidirá que hacer para pagar al fabricante.
Si el monto total de la compra excede de $500.000 la empresa tendrá
la capacidad de invertir de su propio dinero un 55% del monto de la
compra, pedir prestado al banco un 30% y el resto lo pagará
solicitando un crédito al fabricante. Si el monto total de la compra no
excede de $500.00 la empresa tendrá capacidad de invertir de su
propio dinero un 70% y el restante 30% lo pagará solicitando crédito
al fabricante. El fabricante cobra por concepto de interes un 20%
sobre la cantidad que se le pague a crédito. Obtener la cantidad a
inverir, valor del préstamo, valor del crédito y los intereses.
""" 

monto_total = float (input('Digite el monto total de la compra : $ '))
if(monto_total > 500000):
    capacidad_invertir = monto_total * 0.55
    pedir_prestamo = monto_total * 0.30
    credito_fabricante = monto_total * 0.20
    interes = credito_fabricante * 0.20
    credito_total = credito_fabricante + interes        
    print (f'la cantidad a invertir es de : ${capacidad_invertir} ')
    print(f'El valor del prestamos es de: ${pedir_prestamo} ')
    print(f'El valor del credito es de  : ${interes}')
    print(f'El valor del interes es de: ${credito_total} ')

elif(monto_total < 500000):
    capacidad_invertir = monto_total * 0.70
    credito_fabricante = monto_total * 0.30
    interes = credito_fabricante * 0.20
    total_interes = credito_fabricante + interes
    print (f'la cantidad a invertir es de : ${capacidad_invertir} ')   
    print(f'El valor del credito es de  : ${interes}')
    print(f'El valor del interes es de: ${credito_total} ')
    

""" 
9. Leer 2 números; si son iguales que lo multiplique, si el primero es
mayor que el segundo que los reste y sino que los sume.
""" 
numero_uno = float(input('Digite un numero : '))
numero_dos = float(input('Digite un numero : '))
if(numero_uno == numero_dos):
    resultado = numero_uno * numero_dos
    print(f'El resultado total es de : {resultado}')
elif(numero_uno > numero_dos):
   resultado = numero_uno - numero_dos
   print(f'El resultado total es de : {resultado}')
elif(numero_uno < numero_dos):
    resultado = numero_uno + numero_dos
    print(f'El resultado total es de : {resultado}')

"""     
10. Leer tres números diferentes e imprimir el número mayor de los
tres
""" 
numero_uno = float(input('Digite un numero : '))
numero_dos = float(input('Digite un numero : '))
numero_tres = float(input('Digite un numero: '))
if(numero_uno > numero_dos and numero_uno > numero_tres):
    print(f'El número mayor es: {numero_uno}')
elif(numero_dos >  numero_uno and numero_dos > numero_tres):
    print(f'El número mayor es: {numero_dos}')
elif(numero_tres >  numero_uno and numero_tres > numero_uno):
    print(f'El número mayor es: {numero_tres}')
  
         
       
       
    
    