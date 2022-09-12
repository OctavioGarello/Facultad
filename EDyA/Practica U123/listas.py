from __future__ import annotations
from typing import Any
import numpy as np
import os

class Node:
    __value=None 
    __next=None 
    def __init__(self,value):
        self.__value=value
        self.__next=None

    def getValue(self):
        return self.__value 

    def getNext(self):
        return self.__next
    
    def setValue(self,value):
        self.__value=value

    def setNext(self,next:Node|None):
        self.__next=next

class LinkedList:
    __items=None
    __size:int

    def __init__(self):
        self.__items=None
        self.__size=0

    def late(self,pos):
        aux=self.__items
        while pos!=0:
            aux=aux.getNext()
            pos-=1

        return(aux)


    def append(self,value,pos=0):
        mynode=Node(value)

        if self.__size==0 or pos==0:
            mynode.setNext(self.__items)
            self.__items=mynode
            
        
        else:
            l=self.late(pos-1)
            aux=l.getNext()
            mynode.setNext(aux)
            l.setNext(mynode)

        self.__size+=1
     
    def remove(self,pos=0):
        if self.__size==0:
            print("No hay elementos")
        
        else:
            if pos==0:
                itemRemove=self.__items.getValue()
                self.__items=self.__items.getNext()
                
            else:
                l=self.late(pos-1)
                itemRemove=l.getNext().getValue()
                l.setNext(l.getNext().getNext())

            self.__size-=1
            print("El item removido es:[%d]"%itemRemove)
            return(itemRemove)

    def watch(self):
        mynode=self.__items
        cont=0
        while mynode!=None:
            print("posiciones:[%d]= [%d]"%(cont,mynode.getValue()))
            cont+=1
            mynode=mynode.getNext()

class ListaSequential:
    __items:np.ndarray
    __head:int
    __size:int

    def __init__(self,size):
        self.__items=np.empty(size,dtype=int)
        self.__head=0
        self.__size=size
    
    def append(self,value,pos=-1):
        if pos==-1:
            pos=self.__head
        
        for i in range(self.__head,pos,-1):
            print(i)
            self.__items[i]=self.__items[i-1]
            
            
        self.__items[pos]=value
        self.__head+=1
    
    def remove(self,pos=-1):
        if pos==-1:
            pos=self.__head
            
        for i in range(pos,self.__head-1):
            self.__items[i]=self.__items[i+1]
            
        self.__head-=1

   
    def watch(self):
        for i in self.__items:
            print(i)

if __name__=="__main__":

    test=ListaSequential(6)
    test.append(600)
    test.append(500)
    test.append(400)
    test.append(300)
    test.append(200)
    test.append(1,1)

    test.remove()
    print("\nElementos que quedan:")
    test.watch()

    