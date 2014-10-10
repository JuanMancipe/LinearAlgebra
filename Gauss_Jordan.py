# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 17:59:06 2014

@author: juanmanlass
"""

import numpy as np

def inter_fila(my_array, fil1, fil2):
    tempFilaUno = np.copy(my_array[fil1,:])
    my_array[fil1, :] = my_array[fil2,:]
    my_array[fil2,:] = tempFilaUno


tamanoMatriz = int(raw_input("Por favor ingrese el tamaño de la matriz cuadrada: "))

matrizAleatoria = np.arange(tamanoMatriz*(tamanoMatriz+1),dtype = float)
valor = 0

for x in matrizAleatoria:
    valor = float(np.random.randint(-100,100))
    matrizAleatoria[x] = valor
    
matrizATrabajar = matrizAleatoria.reshape(tamanoMatriz, tamanoMatriz+1)
print '\tLa matriz generada aleatoriamente de tamaño (%iX%i)' %(tamanoMatriz,tamanoMatriz)
print matrizATrabajar

columnaInicial = matrizATrabajar[:,0]

posicionUno = 0

for x in xrange(0,tamanoMatriz,1):
    if (columnaInicial[x] == 1):
        posicionUno = x
        break
    
inter_fila(matrizATrabajar,0,posicionUno)
pibote = 0    
for x in xrange(0,tamanoMatriz,1):
    if (matrizATrabajar[x,x] != 0):
        matrizATrabajar[x,:] = matrizATrabajar[x,:] * (1./matrizATrabajar[x,x])
    for y in xrange(0,tamanoMatriz,1):  
        if ((y != x) and (matrizATrabajar[y,x] != 0)):
            pibote = matrizATrabajar[y,x]
            for z in xrange(0,tamanoMatriz+1,1):
                matrizATrabajar[y,z] = (-pibote*matrizATrabajar[x,z]) + matrizATrabajar[y,z]
                                
            
                
print '\tLa matriz de solución es: '              
print matrizATrabajar
           
            
        
        
        











    
        


    