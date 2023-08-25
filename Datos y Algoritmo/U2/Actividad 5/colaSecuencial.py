"""Ejercicio Nº 5: Implementar el TDA  Cola, con sus operaciones 
Abstractas en Representación secuencial y encadenada."""
import numpy as np
import os

class colaSecuencial:
    __primero : int
    __ultimo : int
    __cantidad : int
    __dimension : int
    __arreglo : np.ndarray

    def __init__(self, dimension):
        self.__primero = 0
        self.__ultimo = 0
        self.__cantidad = 0
        self.__dimension = dimension
        self.__arreglo = np.empty(dimension,dtype=int)

    def vacia(self):
        return self.__cantidad == 0

    def lleno(self):
        return self.__cantidad == self.__dimension
    
    def insertar(self, elemento):

        if self.lleno():
            raise Exception("Cola llena")
        
        else:
            self.__arreglo[self.__ultimo] = elemento
            self.__ultimo = (self.__ultimo + 1) % self.__dimension
            self.__cantidad += 1
        
    def suprimir(self):
        
        if self.vacia():
            raise Exception("Cola Vacia")
        
        else:
            self.__primero = (self.__primero + 1) % self.__dimension
            self.__cantidad -= 1
    
    def recorrer(self):

        i = self.__primero
        j = 0
        while j < self.__cantidad:
            print("Elemento: {}".format(self.__arreglo[i])) 
            i = (i+1)%self.__dimension
            j += 1

if __name__ == "__main__":
    
    os.system("cls")

    cola=colaSecuencial(5)
    print("#Se Inserta: 1 2 3 4 5 en este orden\n")

    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)
    cola.insertar(5)

    print("#Mostrar:\n")
    cola.recorrer()

    print("\n#Se Elimina el primero el 1\n")
    cola.suprimir()

    print("#Mostrar:\n")
    cola.recorrer()