"""Herencia y métodos de ligadura dinámica

Descripción del sistema

Una Empresa que funciona 8 horas diarias, necesita calefaccionar todas las oficinas que la 
conforman. Para ello debe elegir entre dos tipos de calefactores: eléctricos o a gas natural. 
La elección de uno u otro, está basada en el costo del consumo de cada uno de ellos.

De todos los calefactores se registra  una marca y un modelo.

De un calefactor eléctrico se registra además, 
la potencia máxima por ejemplo: 500 watts.

De un calefactor a gas natural se registra además, 
matrícula por ejemplo: GN01-00001-06-057, y calorías por ejemplo: 4000kilocalorias/m3. 
-------
Para el desarrollo del sistema requerido usted debe:

a-  Definir las clases de la jerarquía de clases identificada.

b-  Definir una clase colección basada en un arreglo cuyo tamaño se debe ingresar por teclado, para almacenar los  calefactores.

c-  Almacenar en memoria principal los calefactores obteniendo los datos de los archivos “calefactor-electrico.csv”
, “calefactor-a-gas.csv” que contienen los datos de cada uno de los tipos de calefactores.

d-  Implementar un programa que a partir de la información almacenada en memoria permita:

Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.
Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.
Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo."""

from M_Elec import M_Elec
from M_Gas import M_Gas
from M_Cal import M_Cal
if __name__ == '__main__':
    a=M_Elec("calefactor-electrico.csv")
    b=M_Gas("calefactor-a-gas.csv")
    c=M_Cal(a.getArrE(),b.getArrG())

    b.Ingresar()
    a.Ingresar()