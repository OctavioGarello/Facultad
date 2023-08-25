"""Ejercicio Nº 3: Escriba un programa iterativo, que usando una pila, 
calcule el factorial de un número n. """
import numpy as np
import os

class pilaSecuencial:
    __arreglo : np.ndarray
    __tope : int
    __cantidad : int

    def __init__(self, cantidad):
        self.__arreglo = np.empty(cantidad, dtype= int)
        self.__tope = 0
        self.__cantidad = cantidad

    def vacio (self):
        return self.__tope == 0
    
    def lleno (self):
        return self.__tope == self.__cantidad
    
    def insertar(self, elemento):
        if self.lleno():
            raise Exception("Pila Llena")
        else:
            self.__arreglo[self.__tope] = elemento
            self.__tope += 1
    
    def suprimir (self):
        if self.vacio():
            raise Exception("Pila Vacia")
        else:
            self.__tope -= 1
            elementoRemovido = self.__arreglo[self.__tope]

            return(elementoRemovido)
    
    def recorrer(self):
        i = self.__tope-1
        while i>=0:
            print(self.__arreglo[i])
            i-=1

def cargarPila(pila, num):
    i=1

    while i<=num:
        pila.insertar(i)
        i+=1

def generarFactorial(pila):
    factorial=1

    while not pila.vacio():
        factorial *= pila.suprimir()

    return(factorial)

if __name__ == "__main__":
    os.system("cls")

    num=int(input("Ingrese un numero para calcular su Factorial: "))
    pila= pilaSecuencial(num)

    #print("#Cargar Pila\n")
    cargarPila(pila,num)

    #print("#Mostrar:")
    #pila.recorrer()

    fac= generarFactorial(pila)

    print("\nEl Factorial de {} es: {} \n".format(num,fac))


