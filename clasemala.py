import os
import time
from funciones import *


while True:
    print("Menú Trabajadores")
    print("1. Registrar trabajador")
    print("2. Listar trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")

    opc = int(input("Ingrese opción: "))
    os.system("cls")

    if opc == 1:
        registrar_trabajador()

    elif opc == 2:
        listar_trabajadores()
    elif opc == 3:
        exportar_archivo_txt()
    else:
        salir()
    time.sleep(3) 
