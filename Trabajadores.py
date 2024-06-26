import Funciones as F

trabajadores=[]

while True:
    try:
        print("Menu de usuario")
        print("1. Registrar trabajador")
        print("2. Lista de todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir")
        opcion=int(input("Ingrese opción: "))
        if opcion==1:
            F.registrar_trabajador(trabajadores)
        elif opcion==2:
            F.listar_trabajadores(trabajadores)
        elif opcion==3:
            F.imprimir_plantilla(trabajadores)
        elif opcion==4:
            break
        else:
            print("Ingrese una opción válida")


    except ValueError:
        print("Ingrese una opción válida")