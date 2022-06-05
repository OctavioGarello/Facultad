from Aparatos import Aparatos
"""De un Lavarropas: capacidad de lavado (5 Kg, 6kg, etc), velocidad de centrifugado 
(600 rpm, 1200 rpm), cantidad de programas, tipo de carga (Frontal, Superior)."""

class Lavarropas(Aparatos):
    __capacidad: float
    __velocidad: int
    __programas: int
    __tipoCarga: str

    def __init__(self, marca: str, modelo: str, color: str, pais: str, precio: float, capacidad: float, velocidad: int, programas: int, tipoCarga: str):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidad = capacidad
        self.__velocidad = velocidad
        self.__programas = programas
        self.__tipoCarga = tipoCarga

    def getCarga(self):
        return self.__tipoCarga
    
    def toJson(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    marca= self.getMarca(),
                    modelo= self.getModelo(),
                    color= self.getColor(),
                    pais= self.getPais(),
                    precio= self.getPrecio(),
                    capacidad = self.__capacidad,
                    velocidad= self.__velocidad,
                    programas= self.__programas,
                    tipoCarga= self.__tipoCarga
                )
            )
        return d