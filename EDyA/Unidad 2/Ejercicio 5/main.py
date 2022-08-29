"""Ejercicio Nº 5:

Realizar un programa que simule el juego de las torres de Hanoi.

El juego de las tres torres de Hanoi   consiste en  una configuración de tres pilas numeradas como 1, 2 y 3, 
con ‘n’ discos de tamaño creciente. Los discos se representarán mediante  enteros. 
Los discos más grandes utilizarán valores mayores y los discos más pequeños valores menores.

El objetivo del juego es trasladar los discos de la pila 1, a la pila 3, usando la pila 2 como auxiliar.
Para realizar este traslado se deben cumplir siempre los siguientes requisitos:

a) Sólo se puede mover una pieza cada vez; y para tomar una segunda pieza se debe dejar  primero la anterior en alguna torre.

b) Sólo puede apilar una pieza encima de una más grande.

Se deberá ingresar el número de discos con el que se va a jugar y mostrar por pantalla el estado inicial del juego 
(todas las piezas colocadas en la pila 1 y las pilas 2 y 3vacías).

A partir de ahí, pedirá sucesivamente pares de números indicando la pila origen desde la que tomará la pieza y 
la pila destino a la que se  quiere realizar el movimiento. El programa analizará si la jugada es factible. 
Si el resultado del análisis es positivo moverá la ficha de una pila a otra. Si no lo es, 
indicará que es una jugada imposible, indicando el por qué y pedirá un nuevo movimiento.

El juego terminará cuando las pilas 1 y 2 estén vacías y todos los discos se encuentren en la pila 3,  
mostrando el número de jugadas realizadas y el número mínimo de jugadas (2^n –1) en el que se podría haber realizado."""


#Pila secuencial
from typing import Any
import os

class Pila: #Lifo
    __pila: list[Any]

    def __init__(self):
        self.__pila=[]

    def getSize(self):
        if len(self.__pila) is None:
            raise Exception("Error no hay elementos")
        else: return(len(self.__pila))
    
    def add(self,item):
        self.__pila.append(item)
    
    def remove (self):
        return self.__pila.pop()
    
    def getLastValue(self):
        if len(self.__pila)==0:
            return 1000
        else:
            return self.__pila[len(self.__pila)-1] 


    def getIndexValue(self, index):
        if len(self.__pila)<=index:
            return 0
        else:
            return self.__pila[index]
    


class ManejadorTDH:
    __torre1=None
    __torre2=None
    __torre3=None

    def __init__(self,size):
        self.__torre1=Pila()
        self.__torre2=Pila()
        self.__torre3=Pila()
        self.load(size)
        self.watch(size)
    
    def load(self,size):
        
        for i in range(size,0,-1):
            self.__torre1.add(i)
    
    def watch (self,size):
        print("\n\n")
        for i in range(size,0,-1):
            print("[ %d"%self.__torre1.getIndexValue(i-1), end=" ]")
            print("[ %d"%self.__torre2.getIndexValue(i-1), end=" ]")   
            print("[ %d"%self.__torre3.getIndexValue(i-1),"]")   
    
        print("===============")
        print("\n")

        x=int(input("de Torre: "))
        y=int(input("a la Torre: "))

        self.modify(x,y)    
        self.watch(size)
            
    def modify(self,x,y):
        if 0<x<=3 and 0<y<=3:
            if x==1:
                m=self.__torre1.remove()
            elif x==2:
                m=self.__torre2.remove()
            elif x==3:
                m=self.__torre3.remove()

            if y==1 and self.__torre1.getLastValue()>x:
                self.__torre1.add(x)
            elif y==2 and self.__torre2.getLastValue()>x:
                self.__torre2.add(x)
            elif y==3 and self.__torre3.getLastValue()>x:
                self.__torre3.add(x)
            else:
                print("No se puede poner un disco de mayor peso sobre otro de menor peso")
                if x==1:
                    self.__torre1.add(m)
                elif x==2:
                    self.__torre1.add(m)
                elif x==3:
                    self.__torre1.add(m)               
                
        else:
            print("Movimiento Invalido")

            
if __name__=="__main__":
    os.system("cls")
    size=int(input("Ingrese cantidad de Discos: "))
    manejador=ManejadorTDH(size)



    