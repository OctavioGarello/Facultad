#Pila secuencial
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
    
    def watch(self):
        for i in range(self.__end,0 ,-1):
            print(self.__items[i-1])
    
if __name__=="__main__":
    pila=Pila(3)
    print("\n #Cargo(1,2,3)")
    pila.add(1)
    pila.add(2)
    pila.add(3)
    pila.remove()
    print("\n #Mostrar(2,1)")
    pila.watch()