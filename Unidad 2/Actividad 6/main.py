"""Dada la clase ViajeroFrecuente definida en el ejercicio 2,resolver lo siguiente:

1-Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para distinguir entre dos objetos ViajeroFrecuente cuál 
posee mayor cantidad de millas acumuladas, sobrecargue el operador relacional mayor (> o  __gt__ en python).

2-Acumular millas usando la sobrecarga del operador binario suma(+), obteniendo como resultado de la suma una instancia 
de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de acumular millas 
se resuelve de la siguiente forma v = v + 100.

3-Canjear millas usando la sobrecarga del operador binario resta(-),obteniendo como resultado de la resta una instancia 
de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de canjear millas 
se resuelve de la siguiente forma v = v - 100."""
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
    print("No hay Error")
    print('TEST'.center(30,'-'))
    print("\n")
if __name__=="__main__":
    test()
    control=Controlador()
    control.cantidadViajeros()

