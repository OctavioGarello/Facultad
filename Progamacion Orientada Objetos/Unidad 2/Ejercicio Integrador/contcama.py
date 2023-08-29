import csv
import numpy as np
from cama import Cama
from contmedicamento import ContMedicamento

class ContCama:
    __ac= np.array(list)

    def __init__(self):
        self.__ac= np.array(self.getArreglo())

    def getArreglo(self):

        with open("camas.csv","r") as archivo:
            contenido= csv.reader(archivo,delimiter=";")

            lista=[]
            next(contenido)
            for linea in contenido:
                instancia=Cama(int(linea[0]), 
                                int(linea[1]),
                                bool(linea[2]),
                                str(linea[3]),
                                str(linea[4]),
                                str(linea[5]),
                                str(linea[6]))
                lista.append(instancia)
        return(lista)

    def buscarPaciente(self, na):
        i=0
        while((i<len(self.__ac))and(na!=self.__ac[i].getNombre())):
            i=i+1

        if i<len(self.__ac):
            fecha=str(input("Ingrese Fecha de Alta--> "))
            self.__ac[i].modificar(fecha)

            print("\nPaciente:%s\t\tCama:%d\tHabitacion:%d"%(self.__ac[i].getNombre(),self.__ac[i].getCama(),self.__ac[i].getHabitacion()))
            print("Diagnostico:%s\t\tFecha de Internacion:%s"%(self.__ac[i].getDiagnostico(),self.__ac[i].getFi()))
            print("Fecha de Alta:%s"%(self.__ac[i].getFa()))
            print("\n")

            self.__ac[i].modificarNom()
            print(self.__ac[i].getNombre())
            med_pac=ContMedicamento().buscarMedicamentos(i+1)
        else:
            print("Error: No se encontro (%s)"%(na))

        self.buscarDiagnostico()

    def buscarDiagnostico(self):
        i=0
        nd=str(input("\n#Ingrese Nombre del Diagnostico--> "))
        while((i<len(self.__ac))and(nd!=self.__ac[i].getDiagnostico())):
                i=i+1
        
        if (i<len(self.__ac)and(None!=self.__ac[i].getNombre())):
            print("\nPaciente:%s\t\tCama:%d\tHabitacion:%d"%(self.__ac[i].getNombre(),self.__ac[i].getCama(),self.__ac[i].getHabitacion()))
            print("Diagnostico:%s\t\tFecha de Internacion:%s"%(self.__ac[i].getDiagnostico(),self.__ac[i].getFi()))
        else:
            print("**No esta Ocupada**")
