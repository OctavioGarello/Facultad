import csv
from medicamentos import Medicamentos

class ContMedicamento:
    __lm: list[Medicamentos]

    def __init__ (self):
        self.__lm= self.getLista()

    def getLista(self):
        with open("medicamentos.csv","r") as archivo:
            contenido= csv.reader(archivo,delimiter=";")

            lista=[]
            next(contenido)
            for linea in contenido:
                instancia=Medicamentos(int(linea[0]), 
                                int(linea[1]),
                                str(linea[2]),
                                str(linea[3]),
                                str(linea[4]),
                                int(linea[5]),
                                float(linea[6]))
                lista.append(instancia)
        return(lista)
    
    def buscarMedicamentos(self,indice:int):
        acum=0

        print("Medicamento/monodroga\t\tPresentacion\t\tCantidad\tPrecio\n")
        for medicamento in self.__lm:
            if(medicamento.getId()==indice):
                print("%s\t\t\t%s\t\t%5d\t%15.2f"%(medicamento.getMonodroga(),medicamento.getPresentacion(),medicamento.getCantidad(),medicamento.getPrecio()))
                acum+=medicamento.getPrecio()
        print("Total Adeudado:\t\t\t\t\t\t\t\t%.2f\n"%(acum))


        
