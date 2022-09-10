"""Ejercicio Nº 4

La secretaria de modernización de presidencia de la Nación, cuenta con conjuntos de datos (Dataset):  
Estadística de designaciones de magistrados de la Justicia Federal y Nacional por género.

Los datos del archivo están ordenados por año.

se pide

a) Generar la clase designación: con los atributos que posee el archivo.

b)Leer los datos del archivo csv, y generar una lista de designaciones.

c)Leer un tipo de cargo por teclado, y mostrar la cantidad de mujeres designadas en ese cargo por año.

d)Leer una materia, un cargo y un año y mostrar la cantidad de agentes designados en ese cargo,  esa materia en ese año."""
import csv 
from ListSequentialSort import Designaciones,ListSequentialSort

class Handler:
    __ruta=None
    __list=None

    def __init__(self,ruta,size):
        self.__ruta=ruta
        self.__list=[]
        self.load(size)
        self.charge()
        self.agents()

    def load(self,size):
        self.__list=ListSequentialSort(size)

        with open(self.__ruta,"r") as file:
            content=csv.reader(file,delimiter=";")
            next(content)
    
            for object in content:
                item=Designaciones(int(object[0]),object[1],object[2],object[3])
                self.__list.insert(item)
        
        #self.__list.watch()


    def charge(self):
        tc=input("\nIngrese Tipo de Cargo>> ")
        listYears=[]
        listFemale=[]

        for i in self.__list:
            if i.getAño() not in listYears:
                listYears.append(i.getAño())
                listFemale.append(0)

        for i in self.__list:
            if i.getGenero()=="Femenino" and i.getCargo()==tc:
                pos=0
                for j in listYears:
                    if i.getAño()==j:
                        listFemale[pos]+=1
                    else:
                        pos+=1
        
        for i in range(len(listYears)):
            print("Año:[%d]  Cantidad de Mujeres[%d]"%(listYears[i],listFemale[i]))
    
    def agents(self):
        matter=input("\nIngrese Materia: ")
        charge=input("Ingrese cargo: ")
        year=int(input("Ingrese Año: "))
        cont=0
        for i in self.__list:
            if i.getMateria()==matter and i.getCargo()==charge and i.getAño()==year:
                cont+=1
        
        print("La cantidad de agentes es: [%d]"%(cont))

        
if __name__ == "__main__":
    ruta="Ejercicio4//file.csv"
    handler=Handler(ruta,18)
    
    


