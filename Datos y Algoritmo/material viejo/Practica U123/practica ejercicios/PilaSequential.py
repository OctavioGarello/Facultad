import numpy as np

class PilaSequential:
    __items: np.ndarray
    __head: int
    __size: int

    def __init__(self,size):
        self.__items=np.empty(size,dtype=int)
        self.__head=0
        self.__size=size 

    def insert(self,item):
        if self.__head==self.__size:
            print("Error: sin espacio")
        else:
            self.__items[self.__head]=item
            self.__head+=1

    def supress(self):
        if self.__head==0:
            print("Error no hay elementos")
        else:
            self.__head-=1

    def watch(self):
        for i in range(self.__head,0,-1):
            print(self.__items[i-1])
    

if __name__=="__main__":
    ps=PilaSequential(4)    
    ps.insert(1)
    ps.insert(2)
    ps.insert(3)
    ps.insert(4)
    ps.supress()
    ps.watch()