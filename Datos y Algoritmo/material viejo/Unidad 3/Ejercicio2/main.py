from __future__ import annotations
import numpy as np
class Node:
    __value:int
    __next:int 

    def __init__(self,value,next):
        self.__value=value
        self.__next=next

    def getValue(self):
        return self.__value
    
    def getNext(self):
        return self.__next
    
    def setValue(self,value):
        self.__value=value
    
    def setNext(self,next):
        self.__next=next



class ListCursor:
    __items:np.ndarray
    __start:int 
    __emptyStart:int 
    __size:int 

    def __init__(self,size):
        self.__items=np.empty(size,dtype=Node)
        self.__start=-1
        self.__emptyStart=0
        self.__size=size
        self.load()

    def load(self):
        for i in range(0,self.__size):
            self.__items[i]=Node(None,i+1)
        
        self.__items[self.__size-1].setNext(-1)
    
    
    def watch(self):
        for i in range(0,self.__size):
            print("{}   {}   {}".format(i,self.__items[i].getValue(),self.__items[i].getNext()))
    
    def watch2(self):
        pos = self.__start
        cont=0
        while pos != -1:
            print(self.__items[pos].getValue())
            pos = self.__items[pos].getNext()
    
    def previous(self,pos):
        ant = self.__start
        while pos!=0:
            ant = self.__items[ant].getNext()
            pos-=1
        return ant

            
    def insert(self,value,pos=-1):
        if pos==-1:
            self.__items[self.__emptyStart].setValue(value)
            aux=self.__items[self.__emptyStart].getNext()
            self.__items[self.__emptyStart].setNext(self.__start)
            self.__start=self.__emptyStart
            self.__emptyStart=aux
        
        else:
            self.__items[self.__emptyStart].setValue(value)
            aux=self.__items[self.__emptyStart].getNext()
            p=self.previous(pos-1) #obtengo la posicion real, no el previo
            n=self.__items[p].getNext()
            self.__items[p].setNext(self.__emptyStart)
            self.__items[self.__emptyStart].setNext(n)
            self.__emptyStart=aux
        
    def suppress(self,pos=-1):
        itemSuppress=0
        if pos==-1 or pos==1:
            itemSuppress=self.__items[self.__start].getValue()
            self.__emptyStart=self.__start
            self.__items[self.__start].setValue(None)
            self.__start=self.__items[self.__start].getNext()
        
        else:
            p=self.previous(pos-1) #obtengo la posicion real, no el previo
            print(self.__items[p].getValue())
            n=self.__items[p].getNext()
            aux=self.previous(pos-2)
            self.__items[aux].setNext(n)
            self.__items[p].setValue(None)
            self.__emptyStart=p
            
        return itemSuppress
        


        

            
        
        
if __name__=="__main__":
    list=ListCursor(5)
    list.insert(100)
    list.insert(200)
    list.insert(300)
    list.insert(400)
    list.insert(500,1)
    
    list.watch()
    list.suppress(5)
    print("///")
    #list.insert(800)
    list.watch2()
