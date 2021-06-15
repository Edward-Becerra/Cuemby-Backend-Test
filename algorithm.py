"""
Escriba un programa para verificar si una matriz se puede dividir en una posición 
tal que la suma del lado izquierdo de la división sea igual a la suma del
lado derecho.

"""
from random import randint

print('Digite el tamaño del arreglo: ')
t=int(input())

list_1=[randint(1,10) for i in range(t)]
listLeft = []
listRight=[]

print(list_1)

def sumarLista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

suma_numeros_lista = sumarLista(list_1)
print(suma_numeros_lista) 

def canBeSplitted(lista:list)->int:    
    resultado = 0
    if suma_numeros_lista % 2 == 0:
        suma_izq = int(suma_numeros_lista / 2)
        print("************* suma izquierda*************")
        print(suma_izq)

        pos = 0

        while sumarLista(listLeft) != suma_izq:
            listLeft.append(list_1[pos])
            pos +=1

        cont2 = pos+1

        while sumarLista(listRight) != suma_izq:
            listRight.append(list_1[cont2])
            cont2 +=1

        print(listLeft)
        print(listRight)
        resultado = 1
    else:
        print("El arreglo no se puede dividir")
    
    return resultado

canBeSplitted(list_1)