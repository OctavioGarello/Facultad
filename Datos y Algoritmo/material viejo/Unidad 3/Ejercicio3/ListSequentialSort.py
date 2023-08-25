import numpy as np 
class Data:
    __p:str 
    __h:int
    __f:int 
    __ft:int

    def __init__(self,p,h,f,ft):
        self.__p=p 
        self.__h=h 
        self.__f=f 
        self.__ft=ft 

    def getHectareas(self):
        return self.__h
    
    def getProvincia(self):
        return self.__p
    
class ListSequentialSort:
    __items: np.ndarray
    __head:int 
    __size:int  

    def __init__(self,size):
        self.__items=np.empty(size,dtype=Data)
        self.__head=0
        self.__size=size
    
    def validPosicion(self,pos):
        return 0<=pos<=self.__head

    def validSize2(self):
        return  self.__head < self.__size
    
    def validSize1(self):
        return self.__size==0

    def insert(self,item:Data):
        pos=0
        while pos<self.__head and self.__items[pos].getHectareas()>item.getHectareas():
            pos+=1
        
        for i in range(self.__head, pos, -1):
            self.__items[i]=self.__items[i-1]

        self.__items[pos]=item
        self.__head+=1

    def suppress(self,pos=-1):
        if pos==-1:
            pos=self.__head
        if self.validPosicion(pos)==True and self.validSize1()==False:
            itemRemove=self.__items[pos-1]
            
            for i in range(pos-1,self.__head-1):
                self.__items[i]=self.__items[i+1]
            
            self.__head-=1
            return itemRemove
        else:
            print("Error la posicion ingresada es incorrecta")

    def watch(self):
        for i in self:
            print("Nombre:[%s] Hectareas:[%d]"%(i.getProvincia(),i.getHectareas()))

    def getItem(self,pos):
        return self.__items[pos-1]
        

    def search(self,item):
        i=0
        while i<self.__head and self.__items[i]!=item:
            i+=1
        
        if i<self.__head:
            print("El elemento se encontro en la posicion: [%d]"%(i+1))
        else:
            print("No encontro el elemento")
    
    def firstItem(self):
        if self.validSize2==True:
            return self.__items[0]
        else:
            print("No hay elementos")

    def next(self,pos):
        if self.validSize2==True:
            return self.__items[pos+1]
        else:
            print("No hay elementos")
    
    def __iter__(self):
        return iter(self.__items[:self.__head])



