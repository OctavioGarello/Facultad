#Ejercicio Nº 3: Escriba un programa iterativo, que usando una pila, calcule el factorial de un número n.
#Pila secuencial
from typing import Any
import numpy as np

class Pila: #Lifo
    __items: np.ndarray
    __end:int
    __size:int

    def __init__(self,size):
        self.__items=np.empty(size, dtype=int)
        self.__end=0
        self.__size=size

    def getSize(self):
        if self.__end==0:
            raise Exception("Error no hay elementos")
        else: 
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
            self.__end-=1
            itemRemove=self.__items[self.__end]
        return itemRemove
    
    def getValue(self, index):
        return self.__items[index]    
        
    def watch(self):
        for i in range(self.__end,0 ,-1):
            print(self.__items[i-1])

    
def factorial(num):
    pila=Pila(num)
    while num!=0:
        pila.add(num)
        num-=1
    i=0
    result=1    
    for i in range(pila.getSize(),0 ,-1):
        result*=pila.getValue(i-1)
    print(result)
    
if __name__=="__main__":
    factorial(5)