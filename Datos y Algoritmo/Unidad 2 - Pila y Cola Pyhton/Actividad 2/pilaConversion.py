"""Ejercicio Nº 2:Realizar un programa para implementar la conversión de un número decimal a su 
representación binaria utilizando el método de las divisiones sucesivas."""

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

#Funcion Aparte
def convertirBinario(pila, num):
    while num >=2:
        pila.insertar(num%2)
        num = num//2
    pila.insertar(num)

if __name__ == "__main__":
    pila = pilaEncadenada()

    print("#Conversor a Binario")

    num= int(input("Ingrese un numero: "))
    convertirBinario(pila, num)

    print("#Mostrar")
    pila.recorrer()