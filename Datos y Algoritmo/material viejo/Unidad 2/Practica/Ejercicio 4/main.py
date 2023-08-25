#Ejercicio Nº 4: Realizar un programa que permita la manipulación de dos pilas en un mismo espacio de memoria.
from __future__ import annotations
from typing import Any
import numpy as np

class Pila:
    __head1=None
    __head2=None
    __items=np.ndarray 

    def __init__(self,size):
        self.__head1=0
        self.__head2=size-1
        self.__items=np.empty(size, dtype=int)
        self.waxy(size)

    def waxy(self,size):
        for i in range(size):
            self.__items[i]=0
    
    def watch(self):
        for i in range(len(self.__items)):
            print(self.__items[i])

    def getSizeHead1(self):
        return self.__head1

    def getSizeHead2(self):
        return self.__head2

    def getFreeSize(self):
        return self.__head2-self.__head1

    def add1(self, item):
        if self.getFreeSize()==0:
            raise Exception("No queda espacio")

        else:
            self.__items[self.__head1]=item 
            self.__head1+=1
            
    def add2(self, item):
        if self.getFreeSize()==0:
            raise Exception("No queda espacio")

        else:
            self.__items[self.__head2]=item 
            self.__head2-=1

    def remove1(self):
        self.__items[self.getSizeHead1()-1]=0
        self.__head1-=1


    def remove2(self):
        self.__items[self.getSizeHead2()+1]=0
        self.__head2+=1


        


if __name__=="__main__":
    pila=Pila(5)
    pila.add1(1)
    pila.add1(2)

    pila.add2(1)
    pila.add2(2)

    pila.watch()

    print("\n remove")

    pila.remove1()
    pila.remove2()

    pila.watch()