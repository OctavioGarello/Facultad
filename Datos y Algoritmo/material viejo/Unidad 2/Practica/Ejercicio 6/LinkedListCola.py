from __future__ import annotations
from typing import Any

class Node:
    __value=Any 
    __next=None 

    def __init__(self, value):
        self.__value=value
        self.__next=None
    
    def getValue(self):
        return self.__value
    
    def getNext(self):
        return self.__next
    
    def setNext(self, node:Node):
        self.__next=node

class Cola:
    __first=None
    __tail=None
    __size=0

    def __init__(self):
        self.__first=None
        self.__tail=None
        self.__size=0

    def getSize(self):
        return self.__size


    def append(self, value):
        mynode=Node(value)

        if self.__size==0:
            self.__first=mynode
            self.__tail=mynode

        else:
            self.__tail.setNext(mynode)
            self.__tail=self.__tail.getNext()
        self.__size+=1
    
    def remove(self):
        self.__first=self.__first.getNext()
        self.__size-=1


    def watch(self):

        while self.__first!=None:
            print(self.__first.getValue())
            self.__first=self.__first.getNext()


if __name__=="__main__":
    cola=Cola()
    cola.append(1)
    cola.append(2)
    cola.append(3)
    cola.remove()
    cola.watch()    




    