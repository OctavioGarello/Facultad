from __future__ import annotations
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

    def setNext(self,next:Node|None):
        self.__next=next 

class PilaLinkedList:
    __items=None
    __size:int

    def __init__(self):
        self.__items
        self.__size=0
    
    def append(self,value):
        mynode=Node(value)
        if self.__size==0:
            self.__items=mynode
        else:
            mynode.setNext(self.__items)
            self.__items=mynode
        self.__size+=1
    
    def remove(self):
        if self.__size==0:
            print("No hay elementos")
        else:
            itemRemove=self.__items.getValue()
            self.__items=self.__items.getNext()
            self.__size-=1
            print("Se elimino item [%d]"%(itemRemove))
            return(itemRemove)
        
    def watch(self):
        mynode=self.__items
        cont=0
        while mynode!=None:
            print(("[%d]:[%d]")%(cont,mynode.getValue()))
            cont+=1
            mynode=mynode.getNext()
        
class PilaSequential:
    __items:np.ndarray
    __first:int
    __size:int 

    def __init__(self,size):
        self.__items=np.empty(size,dtype=int)
        self.__first=0
        self.__size=size
    
    def append(self,value):
        if self.__first==self.__size:
            print("No hay mas espacio")
        else:
            self.__items[self.__first]=value
            self.__first+=1
    
    def remove(self):
        if self.__first==-1:
            print("No hay mas elementos a eliminar")
        
        else:
            self.__first-=1 #claro se incremento hasta el valor de size y necesitas decrementar primero
            itemRemove=self.__items[self.__first]
            print("Se elimino item [%d]"%itemRemove)
            self.__items[self.__first]=0
            
            
    
    def watch(self):
        for i in range(self.__first,0 ,-1):
            print(self.__items[i-1])

class ColaLinkedList:
    __items=None
    __end=None
    __size:int
    
    def __init__(self):
        self.__items=None
        self.__end=None
        self.__size=0
    
    def append(self,value):
        mynode=Node(value)
        if self.__size==0:
            self.__items=mynode
            self.__end=mynode 
        
        else:
            self.__end.setNext(mynode)
            self.__end=self.__end.getNext()

        self.__size+=1
    
    def remove(self):
        if self.__size==0:
            print("No hay elementos a remover")
        
        else:
            itemRemove=self.__items.getValue()
            self.__items=self.__items.getNext()

            print("Se removio el item [%d]"%itemRemove)
            return(itemRemove)

    def watch(self):
        aux=self.__items
        cont=0
        while aux!=None:
            print("[%d] [%d]"%(cont,aux.getValue()))
            cont+=1
            aux=aux.getNext()

class ColaSequential:
    __items:np.ndarray
    __end:int
    __size:int

    def __init__(self,size):
        self.__items=np.empty(size,dtype=int)
        self.__end=0
        self.__size=size
    
    def append(self,value):
        
        if self.__end==self.__size:
            print("No hay mas espacio")
        else:
            if self.__end==0:
                self.__items[self.__end]=value
                
            else:
                self.__items[self.__end]=value
            self.__end+=1

    def remove(self):
        itemRemove=self.__items[0]
        for i in range(0,self.__size-1):
            self.__items[i]=self.__items[i+1]
        
        self.__end-=1

        print("Se removio el item [%d]"%itemRemove)
        return itemRemove

    def watch(self):
        for i in range(0,self.__end):
            print(self.__items[i])


if __name__=="__main__":
    os.system("cls")
    
    op=int(input("""Eliga Test:
    1>>Pila Lista Enlazada
    2>>Pila Secuencial

    3>>Cola Lista Enlazada
    4>>Cola Secuencial

    0>>End Test
    Opcion>> """))
    while(op!=0):
        os.system("cls")

        if op==1:
            test=PilaLinkedList()
        elif op==2:
            test=PilaSequential(4)
        elif op==3:
            test=ColaLinkedList()
        elif op==4:
            test=ColaSequential(4)
        test.append(1)
        test.append(2)
        test.append(3)
        test.append(4)
        test.remove()
        print("\nElementos que quedan:")
        test.watch()
        op=int(input("""\n Eliga Test:
    1>>Pila Lista Enlazada
    2>>Pila Secuencial

    3>>Cola Lista Enlazada
    4>>Cola Secuencial

    0>>End Test
    Opcion>> """))