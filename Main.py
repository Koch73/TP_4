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
    FD = "peajes.dat"

    Paises = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay")
    Vehiculos = ("Motocicleta", "Automovil", "Camión")

    while opc != "0":

        if opc == "1":
            decision = input("Estas seguro de que deseas eliminar el registro anterior y crear uno nuevo si(1) no (0): ")
            while not(decision == "1" or decision == "0"):
                decision = input("Error, ingrese una opcion correcta si(1) no(0): ")
            if decision == "1":
                registros = cargarArchivo(FD)
                if registros:
                    print("\nRegistros cargados satisfactoriamente.\n")

        elif opc == "2":
            cargaPorTeclado(FD)
            print("\nRegistro cargado satisfactoriamente.\n")

        elif opc == "3":
            mostrarRegistros(FD)

        elif opc == "4":
            p = validatePatente()

            r = BuscaryMostrarPatente(FD, p)
            if r:
                print("se encontraron un total de: ", r, "registro/s")
            # Si se utilza un else, y el archivo no esta creado, se printeara tambien "Patente no encontrada"
            elif r is None:
                print("Patente no encontrada...")
        elif opc == "5":

            c = validateCodigo()
            r = buscarCodigo(FD, c)
            if r:
                print(r)
            # Si se utilza un else, y el archivo no esta creado, se printeara tambien "Patente no encontrada"
            elif r is None:
                print("Codigo no encontrado...")

        elif opc == "6":

            Mc = MatrizConteo(FD)
            if Mc:
                mostrarMatrizConteo(Mc, Paises, Vehiculos)

        elif opc == "7":
            Mc = MatrizConteo(FD)
            if Mc:
                MostrarVehiculos(Mc, Paises, Vehiculos)

        elif opc == "8":
            prom_distancia = distanciaPromedio(FD)
            if prom_distancia:
                print("La distancia promedio desde la ultima cabina es: ", prom_distancia, "Km" )
                mayores_prom = crearArreglo(FD, prom_distancia)
                mayores_prom_ordenado = shellSort(mayores_prom)
                mostrarKmArreglo(mayores_prom_ordenado)

        opc = (input('\nOpcion: '))
        while not(opc.isdigit() and opc in "012345678"):
            opc = input("\nError, ingrese una opcion valida: ")

        if opc == 9:
            pass


def Main():
    menu()


if __name__ == "__main__":
    Main()