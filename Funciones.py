import os
import pickle
import os.path
from Clases import *


# Verificar el pais de la patente
def definir_patente(patente):
    if len(patente) != 7:
        pais_patente = "Otro"

    # ARGENTINA
    elif (
            patente[0].isalpha()
            and patente[1].isalpha()
            and patente[2].isdigit()
            and patente[3].isdigit()
            and patente[4].isdigit()
            and patente[5].isalpha()
            and patente[6].isalpha()
    ):
        pais_patente = "Argentina"

    # BOLIVIA
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
    # BRASIL
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
    # CHILE

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

    # PARAGUAY
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

    # URUGUAY
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

    else:
        pais_patente = "Otro"

    return pais_patente


# Validar que el codigo del ticket contenga solo numeros y que no sea = 0
def validate_codigo():
    while True:
        codigo = input("Ingrese el codigo: ")

        if codigo.isdigit() and codigo != "0":
            return int(codigo)
        else:
            print("Incorrecto, ingrese un codigo valido")


# Validar que la patente contenga solo caracteres alfanumericos
def validate_patente():
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


# Validar que el pais de la cabina este entre 0 y 4
def validate_pais():
    while True:
        pais = input("Ingrese el pais de la cabina: ")
        if pais in "01234" and len(pais) == 1:
            return int(pais)
        else:
            print("Error, pais no valido")


# Validar que el tipo de vehiculo este entre 0 y 2
def validate_tipo():
    tipo = input("Ingrese el tipo de vehiculo: ")
    while not(tipo in '012') or len(tipo) != 1:
        print("Error, tipo de vehiculo no valido")
        tipo = input("Ingrese el tipo de vehiculo: ")
    return int(tipo)


# Validar que la forma de pago este entre  1 o 2
def validate_forma_de_pago():
    while True:
        pago = input("Ingrese la forma de pago: ")
        if pago in '12' and len(pago) == 1:
            return int(pago)
        else:
            print("Forma de pago inválida. Vuelva a intentar.")


# Validar que la distancia recorrida en kilometros este entre 000 y 999
def validate_km():
    distancia = input("Ingrese los kilómetros recorridos: ")
    while not distancia.isdigit():
        print("Error, distancia recorrida incorrecta, ingresela de nuevo")
        distancia = input("Ingrese los kilómetros recorridos: ")
    return int(distancia)


# Cargar un registro por teclado
def carga_por_teclado(fd):
    ticket_generado = Ticket()
    ticket_generado.codigo = validate_codigo()
    ticket_generado.patente = validate_patente()
    ticket_generado.tipoV = validate_tipo()
    ticket_generado.forma_de_pago = validate_forma_de_pago()
    ticket_generado.pais = validate_pais()
    ticket_generado.km_Recorridos = validate_km()

    if not os.path.exists(fd):

        registros = open(fd, "wb")
        pickle.dump(ticket_generado, registros)

    else:
        registros = open(fd, "ab")
        pickle.dump(ticket_generado, registros)

    registros.close()


# Mostrar registros de la lista ordenados
def mostrar_registros(fd):
    if not os.path.exists(fd):
        print("\nLos registros no existen, vuelva a la opcion 1 por favor...")
    else:
        registros = open(fd, "rb")

        size = os.path.getsize(fd)

        while registros.tell() < size:
            ticket = pickle.load(registros)
            r = definir_patente(ticket.patente)
            print(ticket, "  pais de origen: ", r)
        registros.close()


# Buscar registros con la patente p y retornar un contador de registros encontrados
def buscar_mostrar_patente(fd, p):
    if not (os.path.exists(fd)):
        print("\nLos registros no existen, vuelva a la opcion 1 por favor...")
        return False
    registros = open(fd, "rb")
    p = p.upper()
    c = 0
    # Linear search
    size = os.path.getsize(fd)
    while registros.tell() < size:
        ticket = pickle.load(registros)
        if ticket.patente == p:
            c += 1
            print("\n", ticket, "\n")
    registros.close()
    if c > 0:
        return c
    else:
        return None


# Buscar el codigo c en los registros
def buscar_codigo(fd, c):
    if not (os.path.exists(fd)):
        print("\nLos registros no existen, vuelva a la opcion 1 por favor...")
        return False
    registros = open(fd, "rb")

    # Linear search
    size = os.path.getsize(fd)

    while registros.tell() < size:
        ticket = pickle.load(registros)

        if ticket.codigo == c:
            registros.close()
            return ticket

    registros.close()
    return None


# Generar matriz de conteo de paises y vehiculos
def crear_matriz_conteo(fd):

    if not (os.path.exists(fd)):
        print("\nLos registros no existen, vuelva a la opcion 1 por favor...")
        return None

    # Crear la matriz 3*5
    mc = [[0] * 5 for _ in range(3)]

    registros = open(fd, "rb")

    size = os.path.getsize(fd)

    while registros.tell() < size:
        ticket = pickle.load(registros)
        mc[ticket.tipoV][ticket.pais] += 1

    registros.close()
    return mc


# Mostrar la matriz de conteo de paises y vehiculos
def mostrar_matriz_conteo(mc, paises, vehiculos):
    print("\n")
    for i in range(len(mc[0])):
        for j in range(len(mc)):
            if mc[j][i] != 0:
                print("El tipo de vehiculo ", vehiculos[j], " paso por el pais ", paises[i], " ", mc[j][i], " veces")


# Totalizar las filas y las columnas de la matriz
def mostrar_vehiculos(mc, paises, vehiculos):
    print("\nCantidad de vehículos que pasaron por cada pais: ")
    for i in range(len(mc[0])):
        acum_vehiculo = 0
        for j in range(len(mc)):
            acum_vehiculo += mc[j][i]
        print(paises[i], ": ", acum_vehiculo)
    print()
    print("\nCantidad de vehículos de cada tipo: ")
    for i in range(len(mc)):
        acum_cabina = 0
        for j in range(len(mc[0])):
            acum_cabina += mc[i][j]
        print(vehiculos[i], ": ", acum_cabina)


# Calcular el promedio desde la ultima cabina
def distancia_promedio(fd):
    if not (os.path.exists(fd)):
        print("\nLos registros no existen, vuelva a la opcion 1 por favor...")
        return None

    d_total = 0
    c = 0

    registros = open(fd, "rb")

    size = os.path.getsize(fd)

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


# Crea el arreglo con los tickets mayores al promedio
def crear_arreglo(fd, prom):
    if not (os.path.exists(fd)):
        print("\nLos registros no existen, vuelva a la opcion 1 por favor...")
        return None

    mayores_prom = []

    registros = open(fd, "rb")

    size = os.path.getsize(fd)

    while registros.tell() < size:
        ticket = pickle.load(registros)
        if ticket.km_Recorridos > prom:
            mayores_prom.append(ticket)

    return mayores_prom


# Ordenamiento del arreglo de tickets mayores al promedio con shellsort
def shell_sort(v):
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


# Muestra el arreglo ordenado de los tickets mayores al promedio
def mostrar_km_arreglo(v):
    n = len(v)
    print("\n", n, " Tickets son mayores al promedio: ")

    cantidad_lineas = input("\n¿Cuantas lineas quiere visualizar?: ")

    while not (cantidad_lineas.isdigit()):
        cantidad_lineas = input("\nError, ¿Cuantas lineas quiere visualizar?: ")

    print("\n")
    cantidad_lineas = int(cantidad_lineas)
    for i in range(n):
        print(v[i])
        if i >= cantidad_lineas - 1:
            break
