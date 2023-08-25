from __future__ import annotations

class Nodo:
    __value=None
    __next=None
    def __init__(self, value):
        self.__value=value
        self.__next= None
    
    def getValue(self):
        print(self.__value)

    def getNext(self):
        return self.__next
    
    def setNext(self,value:None|Nodo):
        self.__next=value
        