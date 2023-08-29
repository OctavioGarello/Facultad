import os

class Nodo:
    __dato : None | int
    __siguiente = None

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__dato = dato
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
class colaEncadenada:
    __primero : None|Nodo
    __ultimo : None|Nodo
    __cantidad : int

    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0
    
    def insertar(self, dato):
        nuevoNodo = Nodo(dato)
        
        if self.__ultimo == None:
            self.__primero = nuevoNodo

        else:
            self.__ultimo.setSiguiente(nuevoNodo)
        
        self.__ultimo = nuevoNodo
        self.__cantidad += 1
    
    def suprimir(self):

        if self.vacia():
            raise Exception("Cola Vacia")
        
        else:
            self.__primero = self.__primero.getSiguiente() #type: ignore
            self.__cantidad -= 1
    
    def recorrer(self):
        aux = self.__primero
        
        while aux != None:
            print("Elemento: ", aux.getDato())
            aux = aux.getSiguiente()

if __name__ == "__main__":
    
    os.system("cls")

    cola=colaEncadenada()
    print("#Se Inserta: 1 2 3 4 5 en este orden\n")

    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    cola.insertar(4)
    cola.insertar(5)

    print("#Mostrar:\n")
    cola.recorrer()

    print("\n#Se Elimina el primero el 1\n")
    cola.suprimir()

    print("#Mostrar:\n")
    cola.recorrer()