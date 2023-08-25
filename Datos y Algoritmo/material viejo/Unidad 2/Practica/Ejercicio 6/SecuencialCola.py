from typing import Any
import numpy as np

class Cola:
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
    cola=Cola(3)

    cola.add(1)
    cola.add(2)
    cola.add(3)

    cola.remove()
    cola.watch()


