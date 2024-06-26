CARGOS=['ceo','desarrollador','analista de datos']

def registrar_trabajador(trabajadores):
    nombre=input("Ingrese nombre y apellido del trabajador: ")
    cargo=input("Ingrese el cargo del trabajador(CEO/Desarrollador/Analista de Datos): ").lower()
    while cargo not in CARGOS:
        print("Cargo no existe, intente nuevamente")
        cargo=input("Ingrese el cargo del trabajador(CEO/Desarrollador/Analista de Datos): ").lower()
    sueldobruto=int(input("Ingrese sueldo bruto del trabajador: "))
    #calcular descuentos
    descuento_salud=sueldobruto * 0.07
    descuento_afp=sueldobruto * 0.12
    liquido_pagar=sueldobruto-descuento_salud-descuento_afp

    trabajadores.append({
        'Nombre': nombre,
        'Cargo' : cargo,
        'Sueldobruto': sueldobruto,
        'Descuentosalud':descuento_salud,
        'Descuentoafp':descuento_afp,
        'Liquidopagar':liquido_pagar
    })
    print("Trabajador registrado exitosamente")
def listar_trabajadores(trabajadores):
    print("Lista de trabajadores")
    for trabajador in trabajadores:
        print(trabajador)
    print(trabajador["Nombre"])
def imprimir_plantilla(trabajadores):
    cargoSeleccionado=input("Ingrese cargo para imprimir planilla o bien presione enter para seleccionar todos: ").lower()
    if cargoSeleccionado== "":
        trabajadores_a_imprimir= trabajadores
        nombreArchivo="planilla_todos.txt"
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimir=[]
        for trabajador in trabajadores:
            if trabajador["Cargo"]==cargoSeleccionado:
                trabajadores_a_imprimir.append(trabajador)
        nombreArchivo=f"planilla_{cargoSeleccionado}.txt"
    else:
        print("Cargo no válido")
        return
    with open(nombreArchivo,"w") as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f"Nombre y Apellido: {trabajador["Nombre"]}\n")
            archivo.write(f"Cargo: {trabajador["Cargo"]}\n")
            archivo.write(f"Sueldo Bruto: {trabajador["Sueldobruto"]}\n")
            archivo.write(f"Descuento Salud: {trabajador["Descuentosalud"]}\n")
            archivo.write(f"Descuento AFP: {trabajador["Descuentoafp"]}\n")
            archivo.write(f"Liquido a pagar: {trabajador["Liquidopagar"]}\n\n")
