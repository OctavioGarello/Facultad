"""EJERCICIO 7
Sobrecarga por derecha (reverse operators)
Dada la clase ViajeroFrecuente definida en el ejercicio 2 con las sobrecargas de operadores solicitadas en el ejercicio 6, resolver 
lo siguiente:
1-Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero a través de la sobrecarga del operador 
igual (== o __eq__). Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, 
debe ser posible realizar tanto v ==  100 como 100 == v.

2-Acumular millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible 
realizar v =  100 + v.

3-Canjear millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible 
realizar v =  100 - v."""
from clase import ViajeroFrecuente
from controlador import Controlador

def test():
    print('TEST'.center(30,'-'))
    instancia=ViajeroFrecuente(1,"43281084","Octavio","Garello",500)
    instancia2=ViajeroFrecuente(2,"33333333","Mario","Perez",200)

    acum=100
    instancia.getNombre()
    instancia.cantidadTotalMillas()
    instancia.acumularMillas(acum)
    instancia.canjearMillas(acum)
    instancia.modificar(acum)

    gt=instancia>instancia2
    add=instancia+acum
    sub=instancia-acum

    eq=instancia==acum
    req=acum==instancia
    radd=acum+instancia
    rsub=acum-instancia
    print("No hay Error")
    print('TEST'.center(30,'-'))
    print("\n")
    
if __name__=="__main__":
    test()
    control=Controlador().comparar()


