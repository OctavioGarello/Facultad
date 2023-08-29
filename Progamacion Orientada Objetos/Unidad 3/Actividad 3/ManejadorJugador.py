import csv
from Jugador import Jugador

class ManejadorJugador:
    __lista: list[Jugador]

    def __init__(self,ruta):
        self.__lista = self.leerArchivo(ruta)
        #self.Mostrar()
    
    def leerArchivo(self,ruta):
        with open(ruta,"r") as file:
            contenido = csv.reader(file, delimiter=';')
            next(contenido)
            lista = []
            for linea in contenido:
                lista.append(Jugador(linea[0],linea[1],linea[2],linea[3],linea[4]))
        return lista
    
    def Mostrar(self):
        for jugador in self.__lista:
            print(jugador.getNom())

    def getLista(self):
        return self.__lista
