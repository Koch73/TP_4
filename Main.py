from Funciones import *
from CargarArreglo import *

def menu():
    print("-" * 40)
    print("Seleccione una opción")

    print("1) guardar tickets en un archivo binario a partir de un archivo de texto")
    print("2) Crear un nuevo ticket para agregar al archivo binario con datos ingresados por teclado ")
    print("3) Mostrar todos los tickets del archivo binario ")
    print("4) Buscar y mostrar tickets por patente")
    print("5) Buscar un ticket por codigo")
    print("6) Mostrar cantidad de vehículos segun todas las combinaciones posibles "
          "de cabinas y tipo de vehículo ")
    print("7) Mostrar cantidad de vehículos segun cada cabina y cada tipo de vehículo ")
    print("8) Mostrar la distancia promedio recorrida, guardar y mostrar cuantos "
          "vehículos superan el promedio ordenados por distancia ")
    print("0) Salir ")
    print("-" * 40)
    opc = int(input('Opcion: '))

    # Bandera para verificar que el importe de cada
    # tipo de vehiculo fue calculado (necesario para el punto 8)


    #Constantes
    FD = "peajes.dat"

    Paises = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay")
    Vehiculos = ("Motocicleta", "Automovil", "Camión")

    while opc != 0:
        if opc == 1:
            decision = int(
                input("Estas seguro de que deseas eliminar el registro anterior y crear uno nuevo si(1) no (0): "))
            if decision == 1:
                registros = cargarArchivo(FD)
                print("\nRegistros cargados satisfactoriamente.\n")

        elif opc == 2:
            cargaPorTeclado(FD)
            print("\nRegistro cargado satisfactoriamente.\n")

        elif opc == 3:
            mostrarRegistros(FD)


        elif opc == 4:
            patente_buscada = validatePatente()

            r = BuscaryMostrarPatente(FD, patente_buscada)
            if r:
                print("se encontraron un total de: ", r, "registro/s")
            else:
                print("Patente no encontrada...")
        elif opc == 5:

            codigo_buscado = validateCodigo()
            r = buscarCodigo(FD, codigo_buscado)
            if r:
                print(r)
            else:
                print("registro no encontrado...")

        elif opc == 6:
            """En la f cantidadVehiculos() hay una variable gris"""

            Mc = MatrizConteo(FD)
            mostrarMatrizConteo(Mc, Paises, Vehiculos)

        elif opc == 7:
            Mc = MatrizConteo(FD)
            MostrarVehiculos(Mc, Paises, Vehiculos)

        elif opc == 8:
            may, porc, indice_may = porcentajeVehiculos()
            if may != 0 and porc != 0 and indice_may != 0:
                print("\nEl tipo de vehículo con mayor monto acumulado fue ", "'", lista_vehiculos[indice_may], "'",
                      "es igual a: ", may, "y representa el", porc, "% del total")

        opc = int(input('\nOpcion: '))


def Main():
    menu()


if __name__ == "__main__":
    Main()

#CORREGIR ERROR: EN LA OPCION 4, AL BUSCAR UNA PATENTE, EL PROGRAMA SOLO DEVUELVE UNA PATENTE, NO TODAS LAS CONCIDENCIAS
