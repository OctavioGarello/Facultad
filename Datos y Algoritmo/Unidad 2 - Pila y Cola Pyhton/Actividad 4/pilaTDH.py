import numpy as np
import os
 
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
            aux= self.__arreglo[self.__tope]
            self.__arreglo[self.__tope]= 0     #seteo el valor porque sino me obstaculiza una condicion y de ante mano guardo el valor que seteamos
            return(aux)
    
    def recorrer(self):
        i = self.__tope-1
        while i>=0:
            print(self.__arreglo[i])
            i-=1
    
    #---------Operaciones Extra------------#
    def obtener_elemento(self, indice):
        return self.__arreglo[indice - 1]

    def obtener_tope(self):
        return self.__tope

    def obtener_ultimo_elemento(self):
        return self.__arreglo[self.__tope - 1]

class ManejadorTDH:

    __arregloTorres: list[pilaSecuencial]  #Lista de Torres

    def __init__(self, cantidad):

        self.__arregloTorres=[]
        self.inicializar(cantidad) #inicializo 
        self.mostrar(cantidad) #muestro

    def inicializar(self, cantidad):

        for i in range(3):
            self.__arregloTorres.append(pilaSecuencial(cantidad))

        for i in range(cantidad, 0 , -1):
            self.__arregloTorres[0].insertar(i)
    
    def mostrar(self,cantidad):
        os.system("cls")
        print("\n")

        for i in range(cantidad, 0, -1):
            columna1 = str(self.__arregloTorres[0].obtener_elemento(i)) if i <= self.__arregloTorres[0].obtener_tope() else ' '
            columna2 = str(self.__arregloTorres[1].obtener_elemento(i)) if i <= self.__arregloTorres[1].obtener_tope() else ' '
            columna3 = str(self.__arregloTorres[2].obtener_elemento(i)) if i <= self.__arregloTorres[2].obtener_tope() else ' '
            print("[{}]      [{}]       [{}]".format(columna1, columna2, columna3))
        print("=====================")

    def movimiento(self, desde, hasta ,cantidad):

        #Almaceno los ultimos elementos en variables y si son None o Random las intercambio por 0

        if 0 <self.__arregloTorres[desde].obtener_ultimo_elemento() <= cantidad:
            valorTorreDesde = self.__arregloTorres[desde].obtener_ultimo_elemento() 
        else:
            valorTorreDesde = 0
        
        if 0 <self.__arregloTorres[hasta].obtener_ultimo_elemento() <= cantidad:
            valorTorreHasta = self.__arregloTorres[hasta].obtener_ultimo_elemento()
        else:
            valorTorreHasta = 0     

        #La primea: se fija que no este vacia la torre desde la cual voy a mover
        #La segunda: se fija que los movimientos del jugador sean validos
        #La tercera: valida que las fichas de mayor peso no se superpongan sobre la de menor peso
        
        #print("val desde:{}   val hasta:{}".format(valorTorreDesde,valorTorreHasta))

        if not self.__arregloTorres[desde].vacio():
            if 0<= desde < cantidad and 0<= hasta <cantidad:
                if  valorTorreDesde <= valorTorreHasta or valorTorreHasta == 0:

                    self.__arregloTorres[hasta].insertar(self.__arregloTorres[desde].suprimir())

                    self.mostrar(cantidad)

                else:
                    print("\nMovimiento Invalido\n")
            else:
                print("\nMovimiento Invalido\n")
        else:
            print("\nMovimiento Invalido\n")
    
    def verificarBandera(self):
        if self.__arregloTorres[2].lleno(): 
            return False
        else:
            return True

if __name__ == "__main__":
    os.system("cls")

    cantidad=int(input("Ingrese la cantidad de discos: "))
    manejador=ManejadorTDH(cantidad)

    bandera=True

    while(bandera==True):
        desde=int(input("Desde: ")) 
        hasta=int(input("Hasta: "))

        manejador.movimiento(desde-1,hasta-1,cantidad)

        bandera=manejador.verificarBandera()
    
    print("\n ¡¡ Felicidades Ganaste !! \n")
