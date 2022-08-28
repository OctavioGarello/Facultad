"""Ejercicio Nº 7:

Una entidad bancaria que realiza el cobro de servicios, 
habilita una caja que atiende a una cola de clientes. 
Cada cliente avanza para realizar su pago cuando la caja está desocupada. 
Considerar que el tiempo de atención del cajero es de 5 minutos y la frecuencia de llegada de los clientes es de 2 minutos. 
Realizar un programa que simule esta realidad.

Obtener el tiempo máximo de espera de los clientes en la cola.

Nota: Ingresar el tiempo de atención de cajero y la frecuencia de llegada de los clientes a la cola."""

from typing import Any
import os
class Cola:
    __cola: list[Any]

    def __init__(self):
        self.__cola=[]

    def add(self, item):
        self.__cola.append(item)
    
    def remove(self):
        return self.__cola.pop(0)

    
    def getSize(self):
        return(len(self.__cola))
    
    def getValue(self):
        return self.__cola

    def watch(self):
        for i in self.__cola:
            print(i)

if __name__=="__main__":
    os.system("cls")
    ts=int(input("Ingrese el tiempo de simulacion: "))
    ta=int(input("Ingresar el tiempo atencion de cajero: "))
    fr=int(input("ingresar la frecuencia de llegada de los clientes: "))

    cola=Cola()
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



    

    

