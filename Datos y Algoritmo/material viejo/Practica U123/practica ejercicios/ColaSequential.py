import numpy as np

class ColaSequential:
    __items: np.ndarray
    __head:int=0
    __size:int
    
    def __init__(self,size):
        self.__items=np.empty(size,dtype=int)
        self.__head
        self.__size=size
    
    def insert(self,item):
        if self.__head==self.__size:
            print("Error: sin espacio")

        else:
            self.__items[self.__head]=item
            self.__head+=1
    
    def supress(self):

        if self.__head==-1:
            print("No hay mas elementos")

        else:
            for i in range(1,self.__head):
                self.__items[i-1]=self.__items[i]
            self.__head-=1
            
    def watch(self):
        for i in range(0,self.__head):
            print(self.__items[i])
    
if __name__=="__main__":
    ps=ColaSequential(4)    
    ps.insert(1)
    ps.insert(2)
    ps.insert(3)
    ps.insert(4)
    ps.supress()
    ps.watch()
