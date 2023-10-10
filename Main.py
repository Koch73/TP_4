from Funciones import *
from CargarArreglo import *
import os.path
def menu(registros):
    print("-" * 40)
    print("Seleccione una opción")

    print("1) Crear arreglo de registros con tickets guardados en un archivo ")
    print("2) Crear arreglo de registros con datos ingresados por teclado ")
    print("3) Mostrar todos los tickets ordenados ")
    print("4) Buscar un ticket por patente y cabina ")
    print("5) Mostrar cantidad de vehículos por cabina")
    print("6) Mostrar importe acumulado por cada vehículo ")
    print("7) Mostrar tipo de vehículo con mayor monto acumulado y el porcentaje que representa del total ")
    print("8) Mostrar la distancia promedio recorrida y cuantos vehículos superan el promedio ")
    print("9) Calcular y mostrar la distancia promedio entre todos los"
          " vehiculos y cuales de ellos superaron ese promedio")
    print("0) Salir ")
    print("-" * 40)
    opc = int(input('Opcion: '))

    # Bandera para verificar que el importe de cada
    # tipo de vehiculo fue calculado (necesario para el punto 8)
    importe_calculado = False
    FD = "peajes.dat"

    """ cargar paises """

    while opc != 0:
        if opc == 1:
            decision = int(
                input("Estas seguro de que deseas eliminar el registro anterior y crear uno nuevo si(1) no (0): "))
            if decision == 1:
                registros = cargarArchivo(FD)
                print("\nRegistros cargados satisfactoriamente.\n")

        elif opc == 2:
            cargaPorTeclado(registros)
            print("\nRegistro cargado satisfactoriamente.\n")

        elif opc == 3:
            mostrarRegistros(FD)


        elif opc == 4:
            """falta validar"""
            patente_buscada = input("\nIngrese la patente que desea buscar: ")

            r = BuscaryMostrarPatente(FD, patente_buscada)
            if r:
                print("se encontraron un total de: ", r, "registro/s")
            else:
                print("Patente no encontrada...")
        elif opc == 5:
            """" falta validar """
            codigo_buscado = int(input("Ingrese el código buscado: "))
            r = buscarCodigo(FD, codigo_buscado)
            if r:
                print(r)
            else:
                print("registro no encontrado...")

        elif opc == 6:
            """En la f cantidadVehiculos() hay una variable gris"""

            Mc = MatrizConteo(FD)
            mostrarMatrizConteo(Mc)

        elif opc == 7:
            importe_total_vehiculos, lista_vehiculos = importeTickets(registros)
            mostrarImportes(importe_total_vehiculos, lista_vehiculos)
            importe_calculado = True

        elif opc == 8:
            if not importe_calculado:
                importe_total_vehiculos, lista_vehiculos = importeTickets(registros)

            may, porc, indice_may = porcentajeVehiculos(importe_total_vehiculos, registros)
            if may != 0 and porc != 0 and indice_may != 0:
                print("\nEl tipo de vehículo con mayor monto acumulado fue ", "'", lista_vehiculos[indice_may], "'",
                      "es igual a: ", may, "y representa el", porc, "% del total")

        elif opc == 9:
            promedio, cantidad = promedioVehiculos(registros)
            if promedio != 0 and cantidad != 0:
                print("\nEl promedio de distancia desde la ultima cabina fue: ", promedio, " Km",
                      " y la cantidad de vehículos que superan el promedio es: ", cantidad)

        opc = int(input('\nOpcion: '))


def Main():
    registros = []
    menu(registros)


if __name__ == "__main__":
    Main()
