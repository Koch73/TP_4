from Funciones import *
from CrearArchivo import *


def menu():
    print("-" * 40)
    print("Seleccione una opción")

    print("1) Guardar tickets en un archivo binario a partir de un archivo de texto ")
    print("2) Crear un nuevo ticket para agregar al archivo binario con datos ingresados por teclado ")
    print("3) Mostrar todos los tickets del archivo binario ")
    print("4) Buscar y mostrar tickets por patente ")
    print("5) Buscar y mostrar un ticket por codigo ")
    print("6) Mostrar cantidad de vehículos segun todas las combinaciones posibles "
          "de cabinas y tipo de vehículo ")
    print("7) Mostrar cantidad de vehículos segun cada cabina y cada tipo de vehículo ")
    print("8) Mostrar la distancia promedio recorrida, guardar y mostrar cuantos "
          "vehículos superan el promedio ordenados por distancia ")
    print("0) Salir ")
    print("-" * 40)

    opc = (input('\nOpcion: '))
    while not (opc.isdigit() and opc in "012345678"):
        opc = input("\nError, ingrese una opcion valida: ")

    # Constantes
    fd = "peajes.dat"

    paises = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay")
    vehiculos = ("Motocicleta", "Automovil", "Camión")

    while opc != "0":

        if opc == "1":
            decision = input("Estas seguro de que deseas eliminar "
                             "el registro anterior y crear uno nuevo si(1) no (0): ")
            while not(decision == "1" or decision == "0"):
                decision = input("Error, ingrese una opcion correcta si(1) no(0): ")
            if decision == "1":
                registros = cargar_archivo(fd)
                if registros:
                    print("\nRegistros cargados satisfactoriamente.\n")

        elif opc == "2":
            carga_por_teclado(fd)
            print("\nRegistro cargado satisfactoriamente.\n")

        elif opc == "3":
            mostrar_registros(fd)

        elif opc == "4":
            p = validate_patente()

            r = buscar_mostrar_patente(fd, p)
            if r:
                print("\nSe encontraron un total de: ", r, "registro/s")
            # Si se utilza un else, y el archivo no esta creado, se printeara tambien "Patente no encontrada"
            elif r is None:
                print("\nPatente no encontrada...")

        elif opc == "5":
            c = validate_codigo()
            r = buscar_codigo(fd, c)
            if r:
                print("\n", r, "\n")
            # Si se utilza un else, y el archivo no esta creado, se printeara tambien "Patente no encontrada"
            elif r is None:
                print("\nCodigo no encontrado...")

        elif opc == "6":

            mc = crear_matriz_conteo(fd)
            if mc:
                mostrar_matriz_conteo(mc, paises, vehiculos)

        elif opc == "7":
            mc = crear_matriz_conteo(fd)
            if mc:
                mostrar_vehiculos(mc, paises, vehiculos)

        elif opc == "8":
            prom_distancia = distancia_promedio(fd)
            if prom_distancia:
                print("\nLa distancia promedio desde la ultima cabina es: ", prom_distancia, "Km")
                mayores_prom = crear_arreglo(fd, prom_distancia)
                mayores_prom_ordenado = shell_sort(mayores_prom)
                mostrar_km_arreglo(mayores_prom_ordenado)

        opc = (input('\nOpcion: '))
        while not(opc.isdigit() and opc in "012345678"):
            opc = input("\nError, ingrese una opcion valida: ")


if __name__ == "__main__":
    menu()
