"""Ejercicio Nº 2:Realizar un programa para implementar la conversión de un número decimal a 
su representación binaria utilizando el método de las divisiones sucesivas."""

from __future__ import annotations
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
    
    def setNext(self, node:Node|None):
        self.__next=node


class Pila: #Lifo
    __first=None
    __size: int=0
    def __init__(self):
        self.__first=None
        self.__size

    def getSize(self):
        return self.__size

    def append(self, item):
        mynode=Node(item)
        if self.getSize()==0:
            self.__first=mynode
        else:
            mynode.setNext(self.__first)
            self.__first=mynode

        self.__size+=1    

    def remove(self):
        if self.getSize()==0:
            raise Exception("Error no hay elementos")
        else:
            self.__first=self.__first.getNext() #type: ignore
    
    def watch(self):
        current=self.__first
        print("[",end="")
        while current!=None: 
            print(current.getValue(),end="")
            current=current.getNext()
        print("]")            

    def split(self, number):
        if type(number) is not int:
            raise Exception("El valor ingresado no es un Numero")
        else:
            quotient=number
            while quotient!=0:
                rest=quotient%2
                quotient=quotient//2
                self.append(rest)
            
            

if __name__=="__main__":
    os.system("cls")
    pila=Pila()
    pila.split(100)
    pila.watch()
    





