
trabajadores = []
cargos = ("CEO","DESARROLLADOR","ANALISTA")
def registrar_trabajador():
    print("Registro de trabajadores")
    nombre_apellido = input("Ingrese nombre y apellido: ")
    cargo = int(input("Ingrese cargo(1:CEO,2:DESARROLLADOR,3:ANALISTA): "))
    sueldo_bruto = int(input("Ingrese sueldo bruto: "))
    desc_salud = int(7/100 * sueldo_bruto)
    desc_afp = int(12/100 * sueldo_bruto)
    sueldoliquido = sueldo_bruto - (desc_afp+desc_salud)
    trabajador = [nombre_apellido,cargo[cargo-1],sueldo_bruto,desc_afp,desc_salud,sueldoliquido]
    trabajadores.append(trabajador)
    print("Trabajador registrado!")

def listar_trabajadores():
    if len(trabajadores) == 0:
        print("No hay trabajadores en la opción 1")
    else:
        print("\tLISTA DE TRABAJADORES")
        for t in trabajadores:
            print(f"NOMBRE: {t[0]}\CARGO: {t[1]}\nBRUTO: {t[2]}\nDESC sueldo {t[3]}\nDESC AFP {t[4]}\nLIQUIDO {t[5]}")

def exportar_archivo_txt():
    pass

def salir():
    print("Muchas gracias, adios!")
    exit()

###SE PUEDE HACER MÁS FUNCIONES PARA QUE AYUDE!