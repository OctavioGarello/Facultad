from zope.interface import Interface, implementer
from Heladeras import Heladeras
from Lavarropa import Lavarropas
from Nodo import Nodo
from Aparatos import Aparatos
from Interface import IColeccion
from Televisores import Televisores
import json

@implementer(IColeccion)
class ListaEnlazada:
    __cabeza: Nodo|None
    __tamaño: int

    def __init__(self):
        self.__cabeza = None
        self.__tamaño = 0
    
    def agregarElemento(self, dato):
        nuevoNodo = Nodo(dato)
        if self.__tamaño==0:
            self.__cabeza = nuevoNodo
        else:
            auxiliar=self.__cabeza
            if auxiliar is None:
                raise Exception("Lista vacia")
            while auxiliar.getSiguiente()!=None:  #type:ignore
                auxiliar=auxiliar.getSiguiente() #type:ignore
            auxiliar.setSiguiente(nuevoNodo) #type:ignore
        self.__tamaño+=1

        return(nuevoNodo)

    def insertarElemento(self, posicion, dato):
        posicion=posicion-1
        if posicion > self.__tamaño - 1:
            print ("Fuera de Rango")
            raise IndexError
        actual = self.__cabeza
        previo = None
        pos = 0
        if posicion is 0:
            nuevoNodo=Nodo(dato)
            nuevoNodo.setSiguiente(self.__cabeza)
            self.__cabeza=nuevoNodo
        else:
            nuevoNodo = Nodo(dato)
            while pos < posicion:
                pos += 1
                previo = actual
                actual = actual.getSiguiente() #type: ignore
            previo.setSiguiente(nuevoNodo) #type: ignore
            nuevoNodo.setSiguiente(actual)
       
    def __len__(self):
        return self.__tamaño
    
    def mostrarElementoLista(self, posicion):
        auxiliar=self.__cabeza
        bandera=True
        pos=0
        while auxiliar!=None and bandera!=False:
            if posicion==pos:
                tipo=type(auxiliar.getDato())
                if tipo==Televisores:
                    tipo="Televisores"
                    print("Tipo:"+tipo)
                elif tipo==Lavarropas:
                    tipo="Lavarropa"
                    print("Tipo:"+tipo)
                elif tipo==Heladeras:
                    tipo="Heladeras"
                    print("Tipo:"+tipo)
                bandera=False
            else:
                pos+=1
                auxiliar=auxiliar.getSiguiente()
        
        if pos>=self.__tamaño:
            print("No se encontro el dato")

    def mostrarCantidadLista(self):
        auxiliar=self.__cabeza
        tipo=None
        c1=0
        c2=0
        c3=0
        while auxiliar!=None:
            if(auxiliar.getDato().getMarca()=="Philips"):
                tipo=type(auxiliar.getDato())
                if tipo==Televisores:
                        c1+=1
                elif tipo==Lavarropas:
                        c2+=1
                elif tipo==Heladeras:
                        c3+=1
            auxiliar=auxiliar.getSiguiente()
        
        print("Televisores:[%d]\t\tLavarropas:[%d]\t\tHeladeras[%d]"%(c1,c2,c3))

    def mostrarMarcaLavarropas(self):
        auxiliar=self.__cabeza
        while auxiliar!=None:
            if type(auxiliar.getDato())==Lavarropas:
                if(auxiliar.getDato().getCarga()=="Superior"): #type:ignore
                    print("Marca:"+auxiliar.getDato().getMarca())
            auxiliar=auxiliar.getSiguiente()

    def mostrarLista(self):
        auxiliar=self.__cabeza
        print("[",end="")
        while auxiliar!=None:
            if auxiliar.getSiguiente()!=None:
                print("Marca:"+auxiliar.getDato().getMarca(),end=",")
            else:
                print("Marca:"+auxiliar.getDato().getMarca(),end="")
            auxiliar=auxiliar.getSiguiente()
        print("]")
        print("Tamaño:",self.__len__())

    def Eliminar(self,dato:int):
        if self.__tamaño==0:
            print("Lista vacia")
        else:
            bandera:bool=True
            auxiliar=self.__cabeza
            while (auxiliar.getSiguiente().getDato()!=dato) and (bandera!=False): #type:ignore
                if auxiliar.getSiguiente()==None: #type:ignore
                    print("No se encontro el dato")
                    bandera=False
                else:
                    auxiliar=auxiliar.getSiguiente() #type:ignore
                    NodoEliminado=auxiliar.getSiguiente() #type:ignore
                    auxiliar.setSiguiente(NodoEliminado.getSiguiente()) #type:ignore
                    bandera=False
            
            self.__tamaño-=1
    
    def __iter__(self):
        auxiliar = self.__cabeza
        while auxiliar != None:
            yield auxiliar.getDato() 
            auxiliar = auxiliar.getSiguiente()

    def GuardarJson(self,ruta: str):
        lista = []
        cabeza = self.__cabeza
        while cabeza is not None:
            dato = cabeza.getDato()
            dicc = dato.toJson()
            lista.append(dicc)
            cabeza = cabeza.getSiguiente()

        with open(ruta, "w") as file:
            json.dump(lista, file, indent='\t')

    """    def guardar(self, archivo: str):
        with open(archivo, "w") as file:
            lista = []

            for elem in self:
                lista.append({
                    '__class__': elem.__class__.__name__,
                    '__atributos__': elem.toJson()
                })
            
            json.dump(lista, file, indent='\t')"""