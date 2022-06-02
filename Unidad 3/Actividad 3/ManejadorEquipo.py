import numpy as np
import csv
from Equipo import Equipo

class ManejadorEquipo:
    __arreglo: np.ndarray

    def __init__(self,ruta):
        self.__arreglo = np.empty(0, dtype=Equipo)
        self.leerArchivo(ruta)
        #self.Mostrar()

    def leerArchivo(self, ruta):
        with open(ruta, 'r') as file:
            contenido = csv.reader(file, delimiter=';')
            tamaño = int(next(contenido)[1])# en el caso de que nos digan el tamaño se lo colocamos directamente
            self.__arreglo = np.empty(tamaño, dtype=Equipo)

            i = 0
            for linea in contenido:
                self.__arreglo[i] = Equipo(linea[0], linea[1])
                i += 1

    def Mostrar(self):
        for i in range(0, len(self.__arreglo)):
            print(self.__arreglo[i].getNom())
    
    def getArreglo(self):
        return self.__arreglo

    def buscarEquipo(self, nom):
        i=0
        while(i<len(self.__arreglo) and self.__arreglo[i].getNom()!=nom):
            i+=1
        return(i)
    
    

