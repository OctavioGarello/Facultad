from __future__ import annotations 

class ViajeroFrecuente:
    __num_viajero: int=0
    __dni: str
    __nombre: str
    __apellido: str
    __millas_acum: int=0

    def __init__(self, num_viajero,dni,nombre,apellido,millas_acum):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum

    def getNombre(self):
        return(self.__nombre)
    
    def cantidadTotalMillas(self):
        return (self.__millas_acum)

    def canjearMillas(self, canjear):
        if(canjear<=self.__millas_acum):
            self.__millas_acum=self.__millas_acum-canjear
            return(self.__millas_acum)
        else: print("Error de Operacion")
    
    def modificar(self,valor):
        self.__millas_acum=valor
        return(self.__millas_acum)

    def __gt__(self,viajero:ViajeroFrecuente): #importamos de la libreria future anotetion para poder usar este tipo sino no nos deja
        return(self.__millas_acum > viajero.cantidadTotalMillas())
    
    def __add__(self,numero:int):
        self.__millas_acum=self.__millas_acum+numero
        return(self)
    
    def __sub__(self,numero: int):
        self.__millas_acum=self.__millas_acum-numero
        return(self)
    
    def __eq__(self,otro:int):
        return(self.__millas_acum==otro)

    def __req__(self,otro:int):#Si queres hacer el inverso se le pone una R adelante de la operacion para referenciar
        return(otro==self.__millas_acum)

    def __radd__(self,numero:int):#Si queres hacer el inverso se le pone una R adelante de la operacion para referenciar
        self.__millas_acum=numero+self.__millas_acum
        return(self)

    def __rsub__(self,numero:int):#Si queres hacer el inverso se le pone una R adelante de la operacion para referenciar
        self.__millas_acum=numero-self.__millas_acum
        self.__millas_acum=self.__millas_acum*-1
        return(self)

        
