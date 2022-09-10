from __future__ import annotations
import typing as Any


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
    
    def setNext(self, node:Node):
        self.__next=node

class LinkedList:
    __first:Node|None
    __size:int

    def __init__(self):
        self.__first= None
        self.__size= 0
    
    def validPosicion(self,pos):
        return 0<=pos<=self.__size
    
    def validSize1(self):
        return self.__size==0
    
    def __iter__(self):
        mynodo = self.__first
        while mynodo is not None:
            yield mynodo.getValue()
            mynodo = mynodo.getNext()
    
    def previous(self, pos):
        mynode=self.__first
        for i in range(pos):
            mynode=mynode.getNext()
        return mynode
    
    def firstItem(self):
        if self.validSize1()==False:
            return print(self.__first.getValue())
        else: 
            return None 
    
    def latestItem(self):
        if self.validSize1()==False:
            mynode=self.previous(self.__size-1)
            return print(mynode.getValue())
        else:
            return None
    
    def insert(self,value,pos=0):
        
        if self.validPosicion(pos)==False:
            print("Index out")
        
        self.__size += 1
        mynode=Node(value)
        if pos == 0:
            self.__first = mynode
        else:
            previous = self.previous(pos - 1)
            mynode.setNext(previous.getNext())
            previous.setNext(mynode)
    
    def remove(self,pos):
        if self.validPosicion(pos)==False:
            print("Index out")
        
        self.__size-=1
        if pos==0:
            mynode=self.__first.getNext()
            self.__first=mynode
        
        else:
            previous= self.previous(pos-1)
            mynodo = previous.getNext()
            previous.setNext(mynodo.getNext())


    
    def watch(self):
        current=self.__first
        while current!=None:
            print(current.getValue())
            current=current.getNext()
            

if __name__=="__main__":
    list=LinkedList()
    list.insert(1,0)
    list.insert(2,1)
    list.insert(3,1)
    list.remove(2)
    list.watch()
    print("----")
    list.firstItem()
    list.latestItem()
    
