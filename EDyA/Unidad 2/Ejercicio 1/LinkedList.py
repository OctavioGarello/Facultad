#Ejercicio Nº 1: Implementar el TAD Pila con sus operaciones abstractas en Representación secuencial y encadenada.

from nodo import Nodo

class Pila: #Lifo
    __first=None
    __size=0

    def __init__(self):
        self.__first=None
        self.__size=0
    
    def getTamaño(self):
        return print(self.__size)
    
    def append(self,value):
        mynode=Nodo(value)
        if self.__size==0:
            self.__first=mynode
        
        else:
            mynode.setNext(self.__first)
            self.__first=mynode

        self.__size+=1

    def remove(self):
        if self.__first is None:
            raise Exception("Lista vacia")
        else:
            self.__first=self.__first.getNext()
            self.__size-=1

    
    def watch(self):
        current=self.__first
        while current!=None:
            current.getValue()
            current=current.getNext() 
    

if __name__=="__main__":
    pila=Pila()
    print("\n #Cargo(1,2,3,4,5)")
    pila.append(1)
    pila.append(2)
    pila.append(3)
    pila.append(4)
    pila.append(5)
    print("\n #Muestro(1,2,3,4,5)")
    pila.watch()
    print("\n #Elimino el primer elemento de Pila")
    pila.remove()
    print("\n #Muestro(1,2,3,4)")
    pila.watch()







