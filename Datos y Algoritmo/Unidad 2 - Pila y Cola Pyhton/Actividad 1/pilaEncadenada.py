class Nodo:
    __dato: None|int
    __siguiente : None

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None 

    def getDato (self): 
        return self.__dato
    def getSiguiente (self): 
        return self.__siguiente
    
    def setDato (self, dato): 
        self.__dato = dato

    def setSiguiente (self, siguiente): 
        self.__siguiente = siguiente

class pilaEncadenada:
    __tope: None|Nodo
    __cantidad: int

    def __init__(self):
        self.__tope = None
        self.__cantidad = 0

    def vacio(self):
        return self.__cantidad == 0
    
    def insertar(self, dato):
        nuevoNodo = Nodo(dato)
        nuevoNodo.setSiguiente(self.__tope)

        self.__tope= nuevoNodo
        self.__cantidad += 1
    
    def suprimir(self):
        if self.vacio():
            raise Exception("Pila Vacia")
        
        else:
            self.__tope = self.__tope.getSiguiente() #type: ignore
            self.__cantidad -=1

    def recorrer(self):

        aux= self.__tope

        while(aux != None):
            print(aux.getDato())
            aux=aux.getSiguiente()

if __name__ == "__main__":
    Pila= pilaEncadenada()

    print("#Insercion Lista.\n")

    Pila.insertar(1)
    Pila.insertar(2)
    Pila.insertar(3)
    Pila.insertar(4)

    print("#Mostrar:")
    Pila.recorrer()

    print("\n#Suprimir el primero\n")  
    Pila.suprimir()
    
    print("#Mostrar de nuevo:")
    Pila.recorrer()

    print("\n#Suprimir el segundo\n")  
    Pila.suprimir()
    
    print("#Mostrar de nuevo:")
    Pila.recorrer()