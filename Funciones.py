import io
import os
import pickle
import os.path
from Clases import *


#Verificar el pais de la patente
def definirPatente(patente):
    indice_pais = ""
    #ARGENTINA
    if (
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isdigit()
        and patente[3].isdigit()
        and patente[4].isdigit()
        and patente[5].isalpha()
        and patente[6].isalpha()
    ):
        pais_patente = "Argentina"
        indice_pais = 0

    #BOLIVIA
    elif (
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isdigit()
        and patente[3].isdigit()
        and patente[4].isdigit()
        and patente[5].isdigit()
        and patente[6].isdigit()
    ):
        pais_patente = "Bolivia"
        indice_pais = 1
    #BRASIL
    elif (
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isalpha()
        and patente[3].isdigit()
        and patente[4].isalpha()
        and patente[5].isdigit()
        and patente[6].isdigit()
    ):
        pais_patente = "Brasil"
        indice_pais = 2
    #CHILE

    elif (
        patente[0] == " "
        and patente[1].isalpha()
        and patente[2].isalpha()
        and patente[3].isalpha()
        and patente[4].isalpha()
        and patente[5].isdigit()
        and patente[6].isdigit()
    ):
        pais_patente = "Chile"
        indice_pais = 5

    #PARAGUAY
    elif (
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isalpha()
        and patente[3].isalpha()
        and patente[4].isdigit()
        and patente[5].isdigit()
        and patente[6].isdigit()
    ):
        pais_patente = "Paraguay"
        indice_pais = 3

    #URUGUAY
    elif (
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isalpha()
        and patente[3].isdigit()
        and patente[4].isdigit()
        and patente[5].isdigit()
        and patente[6].isdigit()
    ):
        pais_patente = "Uruguay"
        indice_pais = 4

    else:
        pais_patente = "Otro"
        indice_pais = 6

    return pais_patente, indice_pais


#Validar que el codigo del ticket contenga solo numeros y que no sea = 0
def validateCodigo():
    while True:
        codigo = input("Ingrese el codigo: ")

        if codigo.isdigit() and codigo != "0":
            return int(codigo)
        else:
            print("Incorrecto, ingrese un codigo valido")


#Validar que la patente contenga solo caracteres alfanumericos
def validatePatente():
    while True:
        patente = input("Ingrese la patente: ").upper()
        is_valid = True

        for char in patente:
            if not (char.isalpha() or char.isdigit()):
                is_valid = False
                break

        if is_valid:
            return patente
        else:
            print("Error, Patente incorrecta")


#Validar que el pais de la cabina este entre 0 y 4
def validatePais():
    while True:
        pais = input("Ingrese el pais de la cabina: ")
        if pais in "01234" and len(pais) == 1:
            return int(pais)
        else:
            print("Error, pais no valido")


#Validar que el tipo de vehiculo este entre 0 y 2
def validateTipo():
    tipo = input("Ingrese el tipo de vehiculo: ")
    while not tipo in '012' or len(tipo) != 1:
        print("Error, tipo de vehiculo no valido")
        tipo = input("Ingrese el tipo de vehiculo: ")
    return int(tipo)


#Validar que la forma de pago este entre  1 o 2
def validateFormaDePago():
    while True:
        pago = input("Ingrese la forma de pago: ")
        if pago in ('12') and len(pago) == 1:
            return int(pago)
        else:
            print("Forma de pago inválida. Vuelva a intentar.")

#Validar que la distancia recorrida en kilometros este entre 000 y 999
def validateKm():

    distancia = input("Ingrese los kilómetros recorridos: ")
    while not distancia.isdigit():
        print("Error, distancia recorrida incorrecta, ingresela de nuevo")
        distancia = input("Ingrese los kilómetros recorridos: ")
    return int(distancia)


#Cargar un registro por teclado
def cargaPorTeclado(FD):

    TicketGenerado = Ticket()
    TicketGenerado.codigo = validateCodigo()
    TicketGenerado.patente = validatePatente()
    TicketGenerado.tipoV = validateTipo()
    TicketGenerado.forma_de_pago = validateFormaDePago()
    TicketGenerado.pais = validatePais()
    TicketGenerado.km_Recorridos = validateKm()

    if not os.path.exists(FD):

        registros = open(FD, "wb")
        pickle.dump(TicketGenerado, registros)

    else:
        registros = open(FD, "ab")
        pickle.dump(TicketGenerado, registros)

    registros.close()


#Agregar los 0 que sean necesarios (x) a los componentes de una lista t
def agregarCeros(Registros, x):
    for i in range(len(Registros)):
        if len(str(Registros[i].codigo)) != x:
            cant_ceros = x - (len(str(Registros[i].codigo)))
            str_ceros = "0" * cant_ceros
            Registros[i] = str_ceros + str(Registros[i].codigo)
    return Registros


#Ordenar mediante selection sort los registros de una lista v
def ordenarRegistros(Registros):

    #ordenamiento por seleccion directa
    n = len(Registros)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if Registros[i].codigo > Registros[j].codigo:
                Registros[i], Registros[j] = Registros[j], Registros[i]

    #agregarle los 0 que falta delante de los codigos
    Registros = agregarCeros(Registros, 10)

    return Registros


# Mostrar registros de la lista ordenados
def mostrarRegistros(FD):
    if not os.path.exists(FD):
        print("Los registros no existen, vuelva a la opcion 1 por favor...")
    else:
        registros = open(FD, "rb")

        size = os.path.getsize(FD)

        while registros.tell() < size:
            print(pickle.load(registros))
        registros.close()


#Buscar registros con la patente p y retornar un contador de registros encontrados
def BuscaryMostrarPatente(FD, p):

    if not(os.path.exists(FD)):
        print("Los registros no existen, vuelva a la opcion 1 por favor...")
        return False
    registros = open(FD, "rb")
    p = p.upper()
    c = 0
    #Linear search
    size = os.path.getsize(FD)
    while registros.tell() < size:
        ticket = pickle.load(registros)
        if ticket.patente == p:
            c += 1
            print(ticket)
    registros.close()
    if c > 0:
        return c
    else:
        return None


#Buscar mediante busqueda el codigo c en los registros
def buscarCodigo(FD, c):
    if not(os.path.exists(FD)):
        print("Los registros no existen, vuelva a la opcion 1 por favor...")
        return False
    registros = open(FD, "rb")

    #Linear search
    size = os.path.getsize(FD)

    while registros.tell() < size:
        ticket = pickle.load(registros)

        if ticket.codigo == c:

            registros.close()
            return ticket

    registros.close()
    return None


def MatrizConteo(FD):
    # Crear la matriz 3*5
    Mc = [[0]*5 for _ in range(3)]

    if not(os.path.exists(FD)):
        print("Los registros no existen, vuelva a la opcion 1 por favor...")
        return None

    registros = open(FD, "rb")

    size = os.path.getsize(FD)

    while registros.tell() < size:
        ticket = pickle.load(registros)
        Mc[ticket.tipoV][ticket.pais] += 1

    registros.close()
    return Mc


def mostrarMatrizConteo(Mc, Paises, Vehiculos):
    for i in range(len(Mc[0])):
        for j in range(len(Mc)):
            if Mc[j][i] != 0:
                print("\nEl tipo de vehiculo ", Vehiculos[j], " paso por el pais ", Paises[i], " ", Mc[j][i], " veces")


def MostrarVehiculos(Mc, Paises, Vehiculos):

    print("Cantidad de vehículos que pasaron por cada pais: ")
    for i in range(len(Mc[0])):
        acumVehiculo = 0
        for j in range(len(Mc)):
            acumVehiculo += Mc[j][i]
        print(Paises[i], ": ", acumVehiculo)
    print()
    print("Cantidad de vehículos de cada tipo: ")
    for i in range(len(Mc)):
        acumCabina = 0
        for j in range(len(Mc[0])):
            acumCabina += Mc[i][j]
        print(Vehiculos[i], ": ", acumCabina)


#Cambia el valor de la forma de pago de 1 a 2 y viceversa
def cambiarValor(Registros,indice):
    if Registros[indice].forma_de_pago == "1":
        Registros[indice].forma_de_pago = "2"
    else:
        Registros[indice].forma_de_pago = "1"

    return Registros


#Mostrar la cantidad de vehiculos de cada pais que pasaron por las cabinas
def mostrarPaises(lista_nombres_paises, lista_paises):

    print("\n")

    for i in range(len(lista_nombres_paises)):

        if lista_nombres_paises[i] == "otros":
            print("Cantidad de vehiculos de ", lista_nombres_paises[i],
                  "paises que pasaron por las cabinas: ", lista_paises[i])
        else:
            print("Cantidad de vehiculos de ", lista_nombres_paises[i],
                " que pasaron por las cabinas: ", lista_paises[i])

    print("\n")


#Cuenta la cantidad de vehiculos de cada pais que pasaron por las cabinas
def cantidadVehiculos(Registros):

    lista_nombres_paises = ["Argentina","Bolivia","Brasil","Paraguay","Uruguay","Chile","otros"]
    lista_paises = [0,0,0,0,0,0,0]

    for i in range(len(Registros)):

        #pais patente(pp), indice patente(ip)
        pp, ip = definirPatente(Registros[i].patente)
        lista_paises[ip] += 1

    return lista_nombres_paises, lista_paises


#Calcula los importes que se le cobra a cada vehiculo
def calcularImporte(vehiculo,pais,forma_de_pago):
    total = 0
    indice_importe = ""

    vehiculo = int(vehiculo)
    pais = int(pais)
    forma_de_pago = int(forma_de_pago)

    #Argentina, Paraguay o Uruguay
    if pais == 0 or pais == 3 or pais == 4:
        importe_base = 300

    #Bolivia
    elif pais == 1:
        importe_base = 200

    #Brasil
    else:
        importe_base = 300

    if vehiculo == 0:
        importe_basico = importe_base/2
        indice_importe = 0

    elif vehiculo == 1:
        importe_basico = importe_base
        indice_importe = 1

    else:
        importe_basico = importe_base * 1.6
        indice_importe = 2

    if forma_de_pago == 1:
        importe_final = importe_basico

    else:
        importe_final = importe_basico - (importe_basico * 0.1)


    return importe_final, indice_importe


def distanciaPromedio(FD):
    d_total = 0
    c = 0

    registros = open(FD, "rb")

    size = os.path.getsize(FD)

    while registros.tell() < size:
        ticket = pickle.load(registros)
        d_total += ticket.km_Recorridos
        c += 1

    registros.close()
    if c != 0:
        prom = round((d_total / c), 2)
        return prom
    else:
        prom = 0
        return prom



def crearArreglo(FD, prom):

    mayores_prom = []

    registros = open(FD, "rb")

    size = os.path.getsize(FD)

    while registros.tell() < size:
        ticket = pickle.load(registros)
        if ticket.km_Recorridos > prom:
            mayores_prom.append(ticket)

    return mayores_prom


def shellSort(v):
    n = len(v)
    h = 1

    while h <= n // 9:
        h = 3 * h + 1

    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y.km_Recorridos < v[k].km_Recorridos:
                v[k + h] = v[k]
                k -= h
            v[k + h] = y
        h //= 3

    return v


def mostrarKmArreglo(v):
    n = len(v)
    print(n, "tickets son mayores al promedio: ")

    for i in range(n):
        print(v[i])


















