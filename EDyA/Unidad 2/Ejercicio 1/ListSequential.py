#Pila secuencial
from typing import Any

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
    
if __name__=="__main__":
    pila=Pila()
    print("\n #Cargo(1,2,3)")
    pila.add(1)
    pila.add(2)
    pila.add(3)
    print("\n #Mostrar(3,2,1)")
    pila.watch()
    print("\n #Eliminar(3)")
    pila.remove()
    print("\n #Mostrar(2,1)")
    pila.watch()