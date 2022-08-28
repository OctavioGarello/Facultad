#Ejercicio Nº 3: Escriba un programa iterativo, que usando una pila, calcule el factorial de un número n.
#Pila secuencial
from re import I
from typing import Any
from unittest import result

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
        self.__pila.pop()
    
    def watch(self):
        i=0
        for i in range(self.getSize(),0,-1): 
            print(self.__pila[i-1])

    
    def factorial(self, num):
        while num!=0:
            self.add(num)
            num-=1
        i=0
        result=1
        for i in range(self.getSize(),0,-1):
            result=result*self.__pila[i-1]
            

        print(result)
    
if __name__=="__main__":
    pila=Pila()
    pila.factorial(10)