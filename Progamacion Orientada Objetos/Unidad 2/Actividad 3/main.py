"""Listas bidimensionales:
Se necesita desarrollar una aplicación que procese la información de las variables meteorológicas temperatura, humedad y presión 
atmosférica. 
El registro de estas variables se hace cada una hora durante todos los días del mes. Esto se guarda en un archivo de texto 
separado con coma que contiene los siguientes datos: número de día, hora, valor de la variable temperatura, 
valor de la variable humedad y valor de la variable presión atmosférica. Se genera un archivo por cada mes.

Defina la clase “Registro” que posea como atributos los valores de las tres variables meteorológicas que se registran.

Implemente un programa que:

1.Defina una lista bidimensional en la que se almacene el registro de 
las variables meteorológicas (instancia de la clase Registro) para cada día del mes, por cada hora.

2.Almacene en la lista bidimensional los datos registrados en el archivo.

3.Presente un menú de opciones permita realizar las siguientes tareas:

3.1.Mostrar para cada variable el día, la hora de menor y mayor valor.

3.2.Indicar la temperatura promedio mensual por cada hora.

3.3.Dado un número de día listar los valores de las tres 
variables para cada hora del día dado. El listado debe tener el siguiente formato."""
import csv
import os
from clase import  Registro

def test():
    print("------------\n#TEST")
    objeto=Registro(26.0,69,1017)
    print(objeto.getTemp())
    print(objeto.getHumedad())
    print(objeto.getPatmosferica())
    print("------------\n")
    
def compararValores(matriz,m,n):
    mx=mn=matriz[0][0].getTemp() #inicializo el maximo y el minimo
    dia_mxt=hora_mxt=dia_tmn=hora_tmn=0 #inicializo las variables en 0

    mx2=mn2=matriz[0][0].getHumedad()
    dia_mxh=hora_mxh=dia_hmn=hora_hmn=0 

    mx3=mn3=matriz[0][0].getPatmosferica()
    dia_mxp=hora_mxp=dia_pmn=hora_pmn=0 

    for i in range(m):
        for j in range(n):

                #Temperatura
            if(mx<matriz[i][j].getTemp()):
                mx=matriz[i][j].getTemp()
                dia_mxt=i+1
                hora_mxt=j+1

            if(mn>matriz[i][j].getTemp()):
                mn=matriz[i][j].getTemp()
                dia_tmn=i+1
                hora_tmn=j+1

                #Humedad
            if(mx2<matriz[i][j].getHumedad()):
                mx2=matriz[i][j].getHumedad()
                dia_mxh=i+1
                hora_mxh=j+1
                
            if(mn2>matriz[i][j].getHumedad()):
                mn2=matriz[i][j].getHumedad()
                dia_hmn=i+1
                hora_hmn=j+1

                #Presion Atmosferica
            if(mx3<matriz[i][j].getPatmosferica()):
                mx3=matriz[i][j].getPatmosferica()
                dia_mxp=i+1
                hora_mxp=j+1

            if(mn3>matriz[i][j].getPatmosferica()):
                mn3=matriz[i][j].getPatmosferica()
                dia_pmn=i+1
                hora_pmn=j+1
            

    print("-----\n#Maximas y Minimas")
    print("#Temperatura  Maxima  = (Dia: %d Hora: %d)/ Minima = (Dia: %d Hora: %d)"  % (dia_mxt,hora_mxt,dia_tmn,hora_tmn))
    print("#Humedad   Maxima  = (Dia: %d Hora: %d)/ Minima = (Dia: %d Hora: %d)"  % (dia_mxh,hora_mxh,dia_hmn,hora_hmn))
    print("#Presion Atmosferica   Maxima  = (Dia: %d Hora: %d)/ Minima = (Dia: %d Hora: %d)"% (dia_mxp,hora_mxp,dia_pmn,hora_pmn))
    print("-----")

def temperaturaPromedio(matriz,m,n):
    promediotemperatura: float=0
    for i in range(n):
        acum: float=0
        for j in range(m):
            acum=acum+matriz[j][i].getTemp()
            promediotemperatura=acum/m
        print("-----\n#Promedio de Temperatura de la hora (%d): (%.2f)\n"% (i+1,promediotemperatura))
    
def listarVariables(dia:int,matriz,n):
    print("Hora\t\tTemperatura\t\tHumedad\t\tPresion")
    for j in range(n):
        print("%2d %21.2f %20d %16d"%(j+1,matriz[dia-1][j].getTemp(),matriz[dia-1][j].getHumedad(),matriz[dia-1][j].getPatmosferica()))





if __name__=="__main__":

    test()
    with open("archivo.csv","r") as archivo:         #declarar el with con la apertura y la variable q almacena 
        lista= csv.reader(archivo,delimiter=",")     #declarar la variable lista con el tipo de separador del archivo csv

        matriz=[]                                      #creo la matriz inicializo q esta vacia
        m=30                                            #filas i
        n=24                                            #columnas j
        for i in range(m):
            matriz.append([])                           #significa que se agrega una una fila
            for j in range(n):
                matriz[i].append([None,None,None])      # significa que agrega una columna con elementos adentro

        for linea in lista:
            instancia=Registro(float(linea[2]),int(linea[3]),int(linea[4]))
            matriz [int(linea[0])-1][int(linea[1])-1]=instancia
            

        centinela=None
        while(centinela!=0):
            menu=int(input("""
#Menu
-Seleccione >[1] Mostrar Varaiable (Menor/Mayor)
-Seleccione >[2] Temperatura Promedio Mensual (por hora)
-Seleccione >[3] Listar Valores (por dia)

-Ingrese Opcion(0 Finaliza): """))
            if menu==1:
                os.system("cls")
                compararValores(matriz,m,n)
            elif menu==2:
                os.system("cls")
                temperaturaPromedio(matriz,m,n)
            elif menu==3:
                os.system("cls")
                dia=int(input("Ingrese el Dia:"))
                listarVariables(dia,matriz,n)
            elif menu==0:
                os.system("cls")
                print("-----\n#Fin del Programa")
                centinela=0
            else: print("Error")