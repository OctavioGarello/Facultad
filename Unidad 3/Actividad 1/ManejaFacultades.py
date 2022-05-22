import csv
from Facultades import Facultades
class ManjeaFaultades:
    __lista: list[Facultades]

    def __init__(self):
        self.__lista=self.getLista()
        
    def getLista(self):
        with open("Facultades.csv","r") as archivo:
            contenido=csv.reader(archivo,delimiter=",")
            lista=[]
            for linea in contenido:
                if(len(linea)==5):
                    instancia=Facultades(int(linea[0]),linea[1],linea[2],linea[3],linea[4])
                    lista.append(instancia)
                if(len(linea)==6):
                    lista[int(linea[0])-1].setAgregar(linea)
        return(lista)
    
    def setInciso1(self):
        cod=int(input("\nIngrese el Cod>> "))
        for linea in self.__lista:
            if(linea.getCod()==cod):
                print("Nombre Facultad: [%s]"%(linea.getNom()))
                listaCarreras=linea.getCarreras()
                for linea2 in listaCarreras:
                    linea2.setMostrar()
    
    def setInciso2(self):
        nom=str(input("\nIngrese el Nombre>> "))
        for linea in self.__lista:
            listaCarreras=linea.getCarreras()
            for linea2 in listaCarreras:
                if (linea2.getNom()==nom):
                    print("Cod. Facultad:[%d]\t\tCod Carrera:[%d]"%(linea.getCod(),linea2.getCod()))
                    print("Direccion:[%s]\t\tNombre Facultad:[%s]"%(linea.getDir(),linea.getNom()))