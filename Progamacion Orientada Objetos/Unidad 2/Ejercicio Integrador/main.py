import os
from contcama import ContCama

if __name__=="__main__":
    os.system("cls")
    print("\n**Programa**")

    na=str(input("#Ingrese Nombre y Apellido del Paciente--> "))
    iniciar1=ContCama().buscarPaciente(na)

    print("\n**Fin**")



