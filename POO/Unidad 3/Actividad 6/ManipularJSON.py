from pathlib import Path
import json
from Heladeras import Heladeras
from Lavarropa import Lavarropas
from Televisores import Televisores

class ManipularJSON:

    def leerJSON(self, archivo):
        with open(archivo, 'r') as f:
            diccionario = json.load(f) #el load convierte en un dicc de python
        return diccionario

    def cargarObjeto(self, ClaseLista):
        ListaDicc=self.leerJSON("aparatoselectronicos.json")
        for elem in ListaDicc:
            print(elem)
            if "__class__" not in elem:
               raise Exception("No se encuentra la clase")
            else:
                class_name = elem ["__class__"] 
                #print(class_name)
                if class_name =="Heladeras":
                    atributos= elem["__atributos__"]
                    H= Heladeras(**atributos)
                    ClaseLista.agregarElemento(H)

                elif class_name =="Televisores":
                    atributos= elem["__atributos__"]
                    T= Televisores(**atributos)
                    ClaseLista.agregarElemento(T)
                
                elif class_name =="Lavarropa":
                    atributos= elem["__atributos__"]
                    L= Lavarropas(**atributos)
                    ClaseLista.agregarElemento(L)

