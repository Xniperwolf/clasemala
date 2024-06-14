import os
import time

trabajadores = []
cargos = ("CEO","DESARROLLADOR","ANALISTA")
while True:
    print("Menú Trabajadores")
    print("1. Registrar trabajador")
    print("2. Listar trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")

    opc = int(input("Ingrese opción: "))
    os.system("cls")

    if opc == 1:
        print("Registro de trabajadores")
        nombre_apellido = input("Ingrese nombre y apellido: ")
        cargo = int(input("Ingrese cargo(1:CEO,2:DESARROLLADOR,3:ANALISTA): "))
        sueldo_bruto = int(input("Ingrese sueldo bruto: "))
        desc_salud = int(7/100 * sueldo_bruto)
        desc_afp = int(12/100 * sueldo_bruto)
        sueldoliquido = sueldo_bruto - (desc_afp+desc_salud)
        trabajador = [nombre_apellido,cargo[cargo-1],sueldo_bruto,desc_afp,desc_salud,sueldoliquido]
        trabajadores.append(trabajador)

        print("Trabajador Registrado!")

    elif opc == 2:
        pass
    elif opc == 3:
        pass
    else:
        print("Muchas gracias, adios!")
        break
    time.sleep(3) 
