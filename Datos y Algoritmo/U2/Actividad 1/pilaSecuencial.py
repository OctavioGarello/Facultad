import numpy as np

class pilaSecuencial:
    __arreglo : np.ndarray
    __tope : int
    __cantidad : int

    def __init__(self, cantidad):
        self.__arreglo = np.empty(cantidad, dtype= int)
        self.__tope = 0
        self.__cantidad = cantidad

    def vacio (self):
        return self.__tope == 0
    
    def lleno (self):
        return self.__tope == self.__cantidad
    
    def insertar(self, elemento):
        if self.lleno():
            raise Exception("Pila Llena")
        else:
            self.__arreglo[self.__tope] = elemento
            self.__tope += 1
    
    def suprimir (self):
        if self.vacio():
            raise Exception("Pila Vacia")
        else:
            self.__tope -= 1
    
    def recorrer(self):
        i = self.__tope-1
        while i>=0:
            print(self.__arreglo[i])
            i-=1
    
if __name__ == "__main__":
    Pila= pilaSecuencial(4)

    print("#Insercion Lista: 1 2 3 4 en este orden\n")

    Pila.insertar(1)
    Pila.insertar(2)
    Pila.insertar(3)
    Pila.insertar(4)

    print("#Mostrar:")
    Pila.recorrer()

    print("\n#Suprimir el ultimo\n")  
    Pila.suprimir()
    
    print("#Mostrar de nuevo:")
    Pila.recorrer()


