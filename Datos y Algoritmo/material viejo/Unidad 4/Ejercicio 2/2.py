"""Ejercicio Nº2: Teniendo en cuenta que la frontera de un árbol binario es el conjunto de nodos terminales de éste, 
tomados de izquierda a derecha; implemente un método que muestre la frontera de un ABB."""

from __future__ import annotations
import os

class Node:
    __value: int|None
    __left: Node|None
    __right: Node|None 

    def __init__(self,value):
        self.__value=value
        self.__left=None 
        self.__right=None
    
    def setValue(self,value:int|None):
        self.__value=value
    
    def setLeft(self,node:Node|None):
        self.__left=node

    def setRight(self,node:Node|None):
        self.__right=node

    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def getValue(self):
        return self.__value
    
class ABB:
    __items: Node|None 
    __size: int 

    def __init__(self):
        self.__items=None
        self.__head=None 
        self.__heightLeft=0
        self.__heightRight=0
    
    def getRaiz(self):
        return self.__items

    def recover(self):
        self.__head=self.__items

    def maxHeight(self):
        if self.__heightLeft<self.__heightRight:
            return self.__heightRight
        else:
            return self.__heightLeft
    
    def getDegree(self,raiz):
        degree=0
        if raiz.getLeft()!=None:
            degree+=1
        if raiz.getRight()!=None:
            degree+=1
        return degree
    
    def searchMajorMinor(self,raiz):
        if raiz!=None:
            if raiz.getRight()!=None:
                return self.searchMajorMinor(raiz.getRight())
            else:
                return raiz
        else:
            return None

    def insert(self,value):
        mynode=Node(value)
        if self.__items==None:
            self.__items=mynode
            self.__head=mynode
            self.__heightLeft+=1
            self.__heightRight+=1
        
        else:
            if self.__head.getValue()>mynode.getValue():
                if self.__head.getLeft()==None:
                    self.__head.setLeft(mynode)
                    self.__head=self.__items
                else:    
                    self.__head=self.__head.getLeft()
                    self.insert(value)
                    self.__heightLeft+=1

            else:
                if self.__head.getRight()==None:
                    self.__head.setRight(mynode)
                    self.__head=self.__items
                else:    
                    self.__head=self.__head.getRight()
                    self.insert(value)
                    self.__heightRight+=1
    
    def suppress(self,raiz,item,previous=None):
        if raiz!=None:
            if item==raiz.getValue():
                degree=self.getDegree(raiz)
                if degree==0:
                    if previous.getLeft()==raiz:
                        previous.setLeft(None)
                    else:
                        previous.setRight(None)
                elif degree==1:
                    if raiz.getLeft()!=None:
                        child=raiz.getLeft()
                        if previous.getRight()==raiz:
                            previous.setRight(child)
                        else:
                            previous.setLeft(child)
                        del raiz 
                    elif raiz.getRight()!=None:
                        child=raiz.getRight()
                        if previous.getRight()==raiz:
                            previous.setRight(child)
                        else:
                            previous.setRight(child)
                        del raiz
                else:
                    mm=self.searchMajorMinor(raiz.getLeft())
                    self.suppress(self.__items,mm.getValue())
                    raiz.setValue(mm.getValue())
            elif item<raiz.getValue():
                self.suppress(raiz.getLeft(),item,raiz)
            else:
                self.suppress(raiz.getRight(),item,raiz)
        else:
            print("No se encontro el item")


    def search(self,item):
        if self.__head!=None:
            if item==self.__head.getValue():
                return self.__head

            elif item<self.__head.getValue():
                self.__head=self.__head.getLeft()
                return self.search(item) 
            
            else:
                self.__head=self.__head.getRight()
                return self.search(item)
        else:
            return None  

    def levelNode(self,item):
        if self.__head!= None:
            if item==self.__head.getValue():
                return 0
            else:
                if item<self.__head.getValue():
                    self.__head=self.__head.getLeft()
                    return self.levelNode(item)+1
                else:
                    self.__head=self.__head.getRight()
                    return self.levelNode(item)+1
        else:
            return -1

    def sheet(self,item):
        if self.__head!=None:
            if item==self.__head.getValue():
                if self.__head.getLeft()==None and self.__head.getRight()==None:
                    return True 
                else:
                    return False

            else:
                if item<self.__head.getValue():
                    self.__head=self.__head.getLeft()
                    return self.sheet(item)
                else:
                    self.__head=self.__head.getRight()
                    return self.sheet(item)     
        else:
            return False 
    
    def child(self,father,child):
        if self.__head!=None:
            if father==self.__head.getValue():
                if self.__head.getLeft()!=None and self.__head.getRight()!=None: 
                    if self.__head.getLeft().getValue()==child or self.__head.getRight().getValue()==child:
                        return True
                else:
                    return False
            else:
                if father<self.__head.getValue():
                    self.__head=self.__head.getLeft()
                    return self.child(father,child)
                else:
                    self.__head=self.__head.getRight()
                    return self.child(father,child)
        else:
            return False

    def inOrden(self,raiz):
        if raiz!=None:
            self.inOrden(raiz.getLeft())
            print(raiz.getValue(),end="  ")
            self.inOrden(raiz.getRight())

    def preOrden(self,raiz):
        if raiz!=None:
            print(raiz.getValue(),end="  ")
            self.preOrden(raiz.getLeft())
            self.preOrden(raiz.getRight())

    def postOrden(self,raiz):
        if raiz!=None:
            self.postOrden(raiz.getLeft())
            self.postOrden(raiz.getRight())
            print(raiz.getValue(),end="  ")
    
    #--------------------------Ejercicio 2-----------------------------------
    def borders(self,raiz):
        if raiz!=None:
            if raiz.getLeft()==None and raiz.getRight()==None:
                print(raiz.getValue(),end="  ")
            else:
                self.borders(raiz.getLeft())
                self.borders(raiz.getRight())
                


    
if __name__=="__main__":
    os.system("cls")
    a=ABB()
    a.insert(10)
    a.insert(5)
    a.insert(12)
    a.insert(3)
    a.insert(7)
    a.insert(11)
    a.insert(15)

    raiz=a.getRaiz()
    print("\nRecorrido InOrden:")
    a.inOrden(raiz)
    print("\nFronteras:")
    a.borders(raiz)