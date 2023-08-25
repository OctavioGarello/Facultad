from __future__ import annotations
import numpy as np
from typing import Any 

class Node:
    __value=None
    __next=None

    def __init__(self,value,next):
        self.__value=value
        self.__next=next

    def setValue(self,value):
        self.__value=value

    def getValue(self):
        return self.__value

    def setNext(self,node:Node):
        self.__next=node

    def getNext(self):
        return self.__next   

class LinkedListCursor:
    __items:np.ndarray
    __first:int
    __empty:int 
    __size:int

    def __init__(self,size):
        self.__items= np.empty(size,dtype=Node)
        self.__first=-1
        self.__empty=0
        self.__size=0

        self.initialize(size)
    
    def initialize(self,size):
        for i in range(size-1):
            self.__items[i]=Node(None,i+1)

        self.__items[size-1]=Node(None,-1)

    def validPosicion(self,pos):
        return 0<=pos<=self.__size

    def full(self):
        return self.__empty==-1
    
    def empty(self):
        return self.__first==-1
    
    def getSize(self):
        return self.__size
    
    def assign(self, value):
        pos=self.__empty
        item=self.__items[pos]

        item.setValue(value)
        self.__empty=item.getNext()

        return(item,pos)
    
    def previous(self,pos):
        mynode = self.__first
        
        while pos != 0:
            mynode = self.__items[mynode].getNext()
            pos -= 1

        return self.__items[mynode]

    def insert(self, value, pos=-1):
        if pos==-1:
            pos=self.__size
        
        (item,pos)=self.assign(value)

        if pos==0:
            item.setNext(self.__first)
            self.__first=pos
        
        else:
            previous=self.previous(pos-1)
            item.setNext(previous.getNext())
            previous.setNext(pos)
        
        self.__size+=1
    
    def supress(self,pos):
        if pos == 0:
            mynode = self.__first
            self.__first = self.__items[mynode].getNext()
            self.__items[mynode].setNext(self.__empty)
            self.__empty = mynode
        else:
            previous = self.previous(pos - 1)
            mynode = previous.getNext()
            previous.setNext(self.__items[mynode].getNext())
            self.__items[mynode].setNext(self.__empty)
            self.__empty = mynode

    def watch(self,size=4):
        for i in self.__items:
            print(i.getValue())



if __name__=="__main__":
    list=LinkedListCursor(4)

    list.insert(1)
    list.insert(3)
    list.insert(2)
    list.insert(4)
    list.supress(2)
    list.watch()





         


    
