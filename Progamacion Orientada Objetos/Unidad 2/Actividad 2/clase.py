"""Atributos: número de viajero, DNI, nombre, apellido y millas acumuladas.
Métodos:
a- El constructor.
b- “cantidadTotaldeMillas”, retorna la cantidad de millas acumuladas.
c- “acumularMillas”, recibe como parámetro la cantidad de millas recorridas, 
las suma en el atributo correspondiente y retorna el valor del atributo actualizado.
d- “canjearMillas”, recibe como parámetro la cantidad de millas a canjear. 
Para utilizar las millas debe verificarse que la cantidad a canjear sea menor o igual a la cantidad de millas
acumuladas, caso contrario mostrar un mensaje de error en la operación. Retorna el valor de la cantidad de millas acumuladas."""

class ViajeroFrecuente:
    __num_viajero: int=0
    __dni=""
    __nombre=""
    __apellido=""
    __millas_acum: int=0

    def __init__(self, num_viajero,dni,nombre,apellido,millas_acum):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum
    def cantidadTotalMillas(self):
        return (self.__millas_acum)

    def acumularMillas(self, acumulador):
        self.__millas_acum=self.__millas_acum+acumulador
        return (self.__millas_acum)

    def canjearMillas(self, canjear):
        if(canjear<=self.__millas_acum):
            self.__millas_acum=self.__millas_acum-canjear
            return(self.__millas_acum)
        else: print("Error de Operacion")
      
    

