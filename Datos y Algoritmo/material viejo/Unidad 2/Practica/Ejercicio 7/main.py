"""Ejercicio Nº 7:

Una entidad bancaria que realiza el cobro de servicios, 
habilita una caja que atiende a una cola de clientes. 
Cada cliente avanza para realizar su pago cuando la caja está desocupada. 
Considerar que el tiempo de atención del cajero es de 5 minutos y la frecuencia de llegada de los clientes es de 2 minutos. 
Realizar un programa que simule esta realidad.

Obtener el tiempo máximo de espera de los clientes en la cola.

Nota: Ingresar el tiempo de atención de cajero y la frecuencia de llegada de los clientes a la cola."""

from typing import Any
import numpy as np
import os
class Cola:
    __items: np.ndarray
    __end:int
    __size:int

    def __init__(self,size):
        self.__items=np.empty(size, dtype=int)
        self.__end=0
        self.__size=size

    def getSize(self):
            return self.__end
    
    def add(self,item):
        if self.__end==self.__size:
            raise Exception("Error sin espacio")
        else:
            self.__items[self.__end]=item
            self.__end+=1
    
    def remove (self):
        if self.__end==0:
            raise Exception("Error no hay elementos")
        else:
            itemRemove=self.__items[0]

            for i in range(self.__end-1): #se ejecuta 2 veces
                self.__items[i]=self.__items[i+1]
    
            self.__end-=1  #3-1
            self.__items[self.__end]=0 #self.__item[2]=0

            #solo quedaria self.__item[0], self.__item[1]
            
        return itemRemove
    
    def watch(self):
        for i in range(self.__end):
            print(self.__items[i])


if __name__=="__main__":
    os.system("cls")
    ts=int(input("Ingrese el tiempo de simulacion: "))
    ta=int(input("Ingresar el tiempo atencion de cajero: "))
    fr=int(input("ingresar la frecuencia de llegada de los clientes: "))

    size=ts//fr

    cola=Cola(size)
    i=0
    j=0
    te=0 #tiempo de espera total

    for i in range(ts):
        te+=cola.getSize()
        if i%fr==0:  
            j+=1
            cola.add(j)
            print("Llego el Cliente [%d]"%j)
        
        if i%ta==0:
            print("Se atendio al cliente [%d] y fue removido"%cola.remove())

    average=te/j

    print("El Promedio de espera es: [%.2f] min"%average)





    

    

