"""
Ejercicio 3
El gobierno de la Nación cuenta con conjunto de datos dataset: Estadística de incendios
forestales descritos por superficie (hectárea), número de focos por departamento y por provincia.
se pide:

b) Leer los datos del archivo csv, y generar una lista donde cada componente contenga: 
Nombre de provincia y superficie total afectada.

c)Mostrar, Nombre de provincia y superficie afectada ordenada de mayor a menor por superficie total afectada."""
import csv 
from ListSequentialSort import Data,ListSequentialSort


if __name__=="__main__":
    ruta="Ejercicio3//file.csv"
    list=ListSequentialSort(7)
    
    with open(ruta,"r") as file:
        content=csv.reader(file,delimiter=";")
        next(content)
        for object in content:
            item=Data(object[0],int(object[1]),int(object[2]),int(object[3]))
            list.insert(item)
    
    list.watch()

