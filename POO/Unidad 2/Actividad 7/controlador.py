from clase import ViajeroFrecuente
import csv

class Controlador:
    __lista: list[ViajeroFrecuente]

    def __init__(self):
        self.__lista=self.getLista()
    
    def getLista(self):
        with open("archivo.csv","r") as archivo:
            contenido=csv.reader(archivo,delimiter=",")
            lista=[]
            for linea in contenido:
                instancia=ViajeroFrecuente (int(linea[0]), int(linea[1]), str(linea[2]), str(linea[3]), int(linea[4]))
                lista.append(instancia)
        return(lista)
    
    def comparar(self):
        print("\n\n**Compara**\n")
        num=int(input("Millas a Comparar--> "))

        print("\n**Comparo #VIAJERO con #NUMERO**")
        for viajero in self.__lista:
            if(viajero==num):
                print("Viajero[%s]: (Cantidad Millas[%d])"%(viajero.getNombre(),viajero.cantidadTotalMillas()))
        
        print("\n**Comparo #NUMERO con #VIAJERO**")
        for viajero in self.__lista:
            if(num==viajero):
                print("Viajero[%s]: (Cantidad Millas[%d])"%(viajero.getNombre(),viajero.cantidadTotalMillas()))

        self.acumular()
    
    def acumular(self):
        print("\n\n**Acumular**\n")
        for viajero in self.__lista:
            num=int(input("Viajero[%s]: (Cantidad Millas[%d]) Millas Acumular--> "%(viajero.getNombre(),viajero.cantidadTotalMillas())))
            viajero=num+viajero
            print("Viajero[%s]: (Cantidad Millas[%d])\n"%(viajero.getNombre(),viajero.cantidadTotalMillas()))

        self.canjear()
        

    def canjear(self):
        print("\n\n**Canjear**\n")
        for viajero in self.__lista:
            num=int(input("Viajero[%s]: (Cantidad Millas[%d]) Millas Canjear--> "%(viajero.getNombre(),viajero.cantidadTotalMillas())))
            viajero=num-viajero
            print("Viajero[%s]: (Cantidad Millas[%d])\n"%(viajero.getNombre(),viajero.cantidadTotalMillas()))
        self.mostrar()
    
    def mostrar(self):
        i=0
        print("\n\n**Mostrar Todo**\n")
        for viajeros in self.__lista:
            i+=1
            print("Viajero[%d]: (Nombre[%s]) (Millas[%d])"%(i,viajeros.getNombre(),viajeros.cantidadTotalMillas()))