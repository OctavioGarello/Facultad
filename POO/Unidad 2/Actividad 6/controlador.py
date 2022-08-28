"""3-Canjear millas usando la sobrecarga del operador binario resta(-),obteniendo como resultado de la resta una instancia 
de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de canjear millas 
se resuelve de la siguiente forma v = v - 100."""
import csv
from clase import ViajeroFrecuente

class Controlador:
    __lista: list[ViajeroFrecuente]

    def __init__(self):
        self.__lista= self.getLista()
    
    def getLista(self):
        with open("archivo.csv","r") as archivo:
            contenido=csv.reader(archivo,delimiter=",")
            lista=[]
            for linea in contenido:
                instancia=ViajeroFrecuente(int(linea[0]),int(linea[1]),str(linea[2]),str(linea[3]),int(linea[4]))
                lista.append(instancia)
        return(lista)
    
    def cantidadViajeros(self):
        viajero_con_mx=self.__lista[0]
        for viajeros in self.__lista:
            if viajeros > viajero_con_mx :
                viajero_con_mx=viajeros
        i=0
        print("\n\n**Viajero/s con mayores millas acumuladas**")
        for viajeros in self.__lista:
            i+=1
            if(viajero_con_mx.cantidadTotalMillas()==viajeros.cantidadTotalMillas()):
                print("Viajero[%d]: (Nombre[%s]) (Millas[%d])"%(i,viajeros.getNombre(),viajeros.cantidadTotalMillas()))

        self.AcumularMillas()
    
    def AcumularMillas(self):
        i=0
        print("\n\n**Acumular Millas**\n")
        for viajero in self.__lista:
            i+=1
            num=int(input("Viajero[%d]: (Millas[%d])\nIngrese Millas a Acumular--> "% (i,viajero.cantidadTotalMillas())))
            viajero+=num
            print("Nuevo Valor Acumulado: [%d]\n"%viajero.cantidadTotalMillas())

        self.mostrar()
        self.CanjearMillas()
    
    def CanjearMillas(self):
        i=0
        print("\n\n**Canjear Millas**\n")
        for viajero in self.__lista:
            i+=1
            num=int(input("Viajero[%d]: (Millas[%d])\nIngrese Millas a Canjear--> "% (i,viajero.cantidadTotalMillas())))
            viajero-=num
            print("Nuevo Valor Canjeado: [%d]\n"%viajero.cantidadTotalMillas())
        
        self.mostrar()
            
    def mostrar(self):
        i=0
        print("\n\n**Cambios**\n")
        for viajeros in self.__lista:
            i+=1
            print("Viajero[%d]: (Nombre[%s]) (Millas[%d])"%(i,viajeros.getNombre(),viajeros.cantidadTotalMillas()))
    


    
    

