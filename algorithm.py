"""
Escriba un programa para verificar si una matriz se puede dividir en una posición 
tal que la suma del lado izquierdo de la división sea igual a la suma del
lado derecho.

"""
from random import randint

print("Digite el tamaño del arreglo : ")
t = int(input())
# list_1=[randint(1,10) for i in range(t)]

list_1 = []
for i in range(t):
    valor = int(input("Ingrese un valor entero: "))
    list_1.append(valor)

print(f"Su arreglo es: {list_1}")
list_1.sort()
listLeft = list_1.copy()
listRight = list_1.copy()


def sumarLista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma


def canBeSplitted(lista: list):  # ->int
    resultado = 0
    sumLista = sumarLista(lista)
    if sumLista % 2 == 0:
        suma_izq = sumLista // 2
        terminado = False

        while not terminado:
            if sumarLista(listLeft) != suma_izq:
                listLeft.pop()
            if sumarLista(listRight) != suma_izq:
                cont = 0
                listRight.pop(cont)
                cont += 1
            else:
                terminado = True
        print("************* izquierda ***********")
        print(listLeft)
        print("************* derecha *************")
        print(listRight)
        resultado = 1
        return resultado
    else:
        print("No es posible....")
        return resultado


print(
    f"El resultado de intentar dividir el arreglo en dos partes es: \n{canBeSplitted(list_1)}"
)
