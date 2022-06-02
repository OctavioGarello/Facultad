import numpy as np
import csv
import datetime
from Contrato import Contrato
from ManejadorJugador import ManejadorJugador
from ManejadorEquipo import ManejadorEquipo

class ManejadorContratos:
    __arreglo: np.ndarray

    def __init__(self):
        self.__arreglo = np.empty(0, dtype=Contrato)


    def generarContratos(self):
        a=ManejadorJugador("Jugadores.csv")
        b=ManejadorEquipo("Equipo.csv")
        
        lista=a.getLista()
        print("\n#Cargar Equipos")
        for jugador in lista:
            nom=input("Jugador[%s]: Ingrese el nombre del equipo: "%(jugador.getNom()))
            indice=b.buscarEquipo(nom)
            if(indice<len(b.getArreglo())):
                equipo=b.getArreglo()
                print("Equipo[%s]: encontrado"%(equipo[indice].getNom()))
                print("----")
                fi=input("Jugador[%s]: Ingrese la fecha de inicio del contrato: "%(jugador.getNom()))
                ff=input("Jugador[%s]: Ingrese la fecha de fin del contrato: "%(jugador.getNom()))
                pm=float(input("Jugador[%s]: Ingrese el precio mensual del contrato: "%(jugador.getNom())))
                print("----")
                self.__arreglo=np.append(self.__arreglo,Contrato(fi,ff,float(pm),jugador,equipo[indice])) #type: ignore
            else:
                print("Equipo[%s]: no encontrado"%(nom))
        self.MostrarArregloContratos()
        self.consultarJugadores()
        self.consultarEquipos()
        self.obtenerImporte()
        self.guardarContratos()
    
    def MostrarArregloContratos(self):
        print("\n#Mostrar Contratos")
        for i in range(0, len(self.__arreglo)):
            print("Contrato [%d]: Jugador[%s]"%(i+1,self.__arreglo[i].getJugador().getNom()))
    
    def consultarJugadores(self):
        print("\n#Buscar Jugadores: ")
        i=0
        dni=input("Ingrese el DNI del jugador: ")
        while (i<len(self.__arreglo)and(self.__arreglo[i].getJugador().getDni()!=dni)):
            i+=1
        
        if i<len(self.__arreglo):
            print("Jugador[%s] Equipo[%s]: Encontrado"%(self.__arreglo[i].getJugador().getNom(),self.__arreglo[i].getEquipo().getNom()))
            print("Fecha de Fin: %s"%(self.__arreglo[i].getFechaFin()))
        else:
            print("DNI[%s]: jugador no encontrado"%(dni))
    
    def consultarEquipos(self):
        print("\n#Contratos que terminan en los 6 meses: ")
        listaMeses6=[]
        meses=datetime.timedelta(days=180)+datetime.date.today()
        i=0
        nom=input("Ingrese el nombre del equipo: ")
        for i in self.__arreglo:
            if i.getEquipo().getNom()==nom:
                if i.getFechaFin()<=(meses):
                    listaMeses6.append(i)

        for i in listaMeses6:
            print("Jugador[%s]"%(i.getJugador().getNom()))
        
    def obtenerImporte(self):
        print("\n#Obtener importe de contratos: ")
        nom=input("Ingrese el nombre del equipo: ")
        importe=0
        for i in self.__arreglo:
            if i.getEquipo().getNom()==nom:
                importe+=i.getPagoMensual()
        print("Importe total de contratos: %.2f"%(importe))

    def guardarContratos(self):
        print("\n#Guardar Contratos")
        archivo=open("Contratos.csv","w")
        archivo.write("DNI,Nombre del equipo,Fecha de inicio,Fecha de fin,Pago mensual\n")
        for i in self.__arreglo:
            archivo.write("%s,%s,%s,%s,%.2f\n"%(i.getJugador().getDni(),i.getEquipo().getNom(),i.getFechaInicio(),i.getFechaFin(),i.getPagoMensual()))
        archivo.close()
        print("Contratos guardados en Contratos.csv")

    
            

                


            
                
                    