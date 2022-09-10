import numpy as np 
class ListSequentialSort:
    __items: np.ndarray
    __head:int 
    __size:int  

    def __init__(self,size):
        self.__items=np.empty(size,dtype=int)
        self.__head=0
        self.__size=size
    
    def validPosicion(self,pos):
        return 0<=pos<=self.__head

    def validSize2(self):
        return  self.__head < self.__size
    
    def validSize1(self):
        return self.__size==0

    def insert(self,item):

        pos=0
        while pos<self.__head and self.__items[pos]<item:
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
            print(i)


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

    def removeRepeater(self):
        for i in self.__items:
            cont=0
            j=0
            band=True
            while j<self.__head and band==True:
                if self.__items[j]>i:
                    band=False
                else:
                    if self.__items[j]==i:
                        cont+=1
                        if cont==2:
                            self.suppress(j+1)
                            cont=0
                    j+=1

                
                    
                 

if __name__=="__main__":
    list=ListSequentialSort(6)

    list.insert(10)
    list.insert(5)
    list.insert(7)
    list.insert(5)
    list.insert(2)
    list.insert(10)

    list.watch()
    print("////")
    list.removeRepeater()
    print("////")
    list.watch()
    