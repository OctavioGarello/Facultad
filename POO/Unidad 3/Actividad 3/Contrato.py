from Jugador import Jugador
from Equipo import Equipo
from datetime import datetime,date

class Contrato:
    __fi:date
    __ff:date
    __pm:float
    __jugador:Jugador
    __Equipo:Equipo

    def __init__(self,fi:str,ff:str,pm:float,jugador:Jugador,equipo:Equipo):
        self.__fi = datetime.strptime(fi, "%d/%m/%Y").date()
        self.__ff = datetime.strptime(ff, "%d/%m/%Y").date()
        self.__pm = pm
        self.__jugador=jugador
        self.__equipo=equipo

    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo
    
    def getFechaFin(self):
        return self.__ff

    def getPagoMensual(self):
        return self.__pm
    
    def getFechaInicio(self):
        return self.__fi