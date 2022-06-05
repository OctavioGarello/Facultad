
from Electrico import Electrico
import numpy as np
import csv

class M_Elec:
    __arrE: np.ndarray

    def __init__(self,ruta):
        self.__arrE = np.empty(0, dtype=Electrico)
        self.LeerArchivo(ruta)
        #self.Mostrar()
    
    def LeerArchivo(self,ruta):
        with open(ruta,"r") as archivo:
            contenido=csv.reader(archivo,delimiter=";")
            next(contenido)
            for linea in contenido:
                    self.__arrE = np.append(self.__arrE, Electrico(linea[0],linea[1],int(linea[2]),float(linea[3])))#type: ignore 
    
    def Mostrar(self):
        print("Electrico:")
        for i in self.__arrE:
            print("%s"%(i.getMarca()))
    
    def getArrE(self):
        return self.__arrE
    
    def Ingresar(self):
        costo=float(input("Ingrese el costo por Kilowatt:"))
        cantidad=float(input("Ingrese la cantidad que se estima consumir en hora:"))
        total=costo*cantidad
        print("El/Los calefactor/es de menor costo de consumo son:")
        for i in self.__arrE:
            if i.getCostoConsumo()<=total:
                print("Calefactor[%s]:Modelo[%s] Potencia[%d] Costo[%.2f] CostoConsumo[%.2f]"%(i.getTipo(),i.getModelo(),i.getPotmax(),i.getCosto(),i.getCostoConsumo()))