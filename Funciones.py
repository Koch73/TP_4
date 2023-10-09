import io
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
        patente[0].isalpha()
        and patente[1].isalpha()
        and patente[2].isalpha()
        and patente[3].isalpha()
        and patente[4].isdigit()
        and patente[5].isdigit()
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





#Validar que el codigo del ticket contenga solo numeros
def validateCodigo(codigo):
    valid = False
    c = 0
    while not(valid):
        for i in range(len(codigo)):
            if codigo[i] in "123456789":
                c += 1
                continue
            else:
                codigo = input("Codigo incorrecto, ingrese un codigo valido: ")
                break
        if len(codigo) == c:
            valid = True



#Validar que la patente sea correcta
def validatePatente(patente):
    c = 0
    for i in range(len(patente)):
        if patente[i].isalpha() or patente[i] in "0123456789":
            c += 1
    if len(patente) == c:
        return True
    else:
        return False


#Validar que el pais sea correcto
def validatePais(pais):
    if not pais in '01234' or len(pais) != 1:
        return False
    return True


#Validar que el tipo de vehiculo sea correcto
def validateTipo(tipo):
    if not tipo in '012' or len(tipo) != 1:
        return False
    return True


#Validar que la forma de pago sea correcta
def validateFormadepago(pago):
    if not pago in '12' or len(pago) != 1:
        return False
    return True


#Validar que la distancia sea correcta
def validateKm(distancia):
    if not distancia.isdigit() or len(distancia) != 3:
        return False
    return True


#Cargar un registro por teclado
def cargaPorTeclado(Registros):

    codigo = input("Ingrese el código: ")
    validateCodigo(codigo)

    patente = (input("Ingrese la patente: ")).upper()
    while not(validatePatente(patente)):
        print("Error, patente incorrecta, ingresela de nuevo")
        patente = (input("Ingrese la patente: ")).upper()

    tipoV = input("Ingrese el tipo de vehiculo: ")
    while not(validateTipo(tipoV)):
        print("Error, tipo de vehiculo incorrecto, ingreselo de nuevo")
        tipoV = input("Ingrese el tipo de vehiculo: ")

    forma_de_pago = input("Ingrese la forma de pago: ")
    while not(validateFormadepago(forma_de_pago)):
        print("Error, forma de pago incorrecta, ingresela de nuevo")
        forma_de_pago = input("Ingrese la forma de pago: ")

    pais = input("Ingrese el país: ")
    while not(validatePais(pais)):
        print("Error, ingrese un pais correcto (0-4): ")
        pais = input("Ingrese el país: ")

    km_recorridos = input("Ingrese lo kilómetros recorridos: ")
    while not(validateKm(km_recorridos)):
        print("Error, distancia recorrida incorrecta, ingresela de nuevo")
        km_recorridos = input("Ingrese los kilómetros recorridos: ")

    TicketGenerado = Ticket()
    TicketGenerado.codigo = codigo
    TicketGenerado.patente = patente
    TicketGenerado.tipoV = tipoV
    TicketGenerado.forma_de_pago = forma_de_pago
    TicketGenerado.pais = pais
    TicketGenerado.km_Recorridos = km_recorridos
    Registros.append(TicketGenerado)


#Agregar los 0 que sean necesarios (x) a los componentes de una lista t
def agregarCeros(Registros, x):
    for i in range(len(Registros)):
        if len(str(Registros[i].codigo)) != x:
            cant_ceros = x - (len(str(Registros[i].codigo)))
            str_ceros = "0" * cant_ceros
            Registros[i] = str_ceros + str(Registros[i].codigo)
    return Registros

""" estas funcion no sirve en esste contexto """
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


""" estas funcion no sirve en esste contexto """
#Buscar registro con la patente p en el pais x
def buscarRegistro(Registros, p, x):
    p = p.upper()
    #Linear search
    for i in range(len(Registros)):
        if Registros[i].patente == p and Registros[i].pais == x:
            return Registros[i]

    return None

""" estas funcion no sirve en esste contexto """
#Buscar mediante busqueda binaria el codigo c en los registros
def buscarCodigo(Registros, c):
    # Linear search
    for i in range(len(Registros)):
        if Registros[i].codigo == c:
            return i

    return None


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
    contador_paises = 0

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


def mostrarImportes(importe_final_vehiculos, lista_vehiculos):
    for i in range(len(importe_final_vehiculos)):
        print("Importe total acumulado por tickets de ",
              lista_vehiculos[i], " : ", importe_final_vehiculos[i])


#Suma los importes de los distintos tipos de vehiculos
def importeTickets(Registros):

    lista_vehiculos = ["Motocicletas", "Automoviles", "Camiones"]
    importe_total_vehiculos = [0,0,0]

    for i in range(len(Registros)):
        total_vehiculo, indice_vehiculo = \
            calcularImporte(Registros[i].tipoV, Registros[i].pais, Registros[i].forma_de_pago)

        importe_total_vehiculos[indice_vehiculo] += total_vehiculo

    return importe_total_vehiculos, lista_vehiculos


#Calcular promedio y porcentaje del tipo vehiculo con el importe mas alto
def porcentajeVehiculos(importe_total_vehiculos, registros):
    may = 0
    total = 0
    indice = 0
    for i in range(len(importe_total_vehiculos)):
        total += importe_total_vehiculos[i]
        if importe_total_vehiculos[i] > may:
            may = importe_total_vehiculos[i]
            indice = i
    if total != 0:
        porc = round(may * 100 / total, 2)
    else:
        print("cargue el vector primero...")
        return 0, 0, 0
    return may, porc, indice


#Calcula el promedio de la distancia recorrida desde la ultima cabina
def promedioVehiculos(Registros):
    total = 0
    #Contador para los vehículos que superan la distancia promedio
    c_vehiculos = 0
    if not Registros:
        print("Primero cargue el vector por favor...")
        return 0, 0
    for i in range(len(Registros)):
        total += int(Registros[i].km_Recorridos)

    prom = round(total / len(Registros), 2)

    for i in range(len(Registros)):
        if int(Registros[i].km_Recorridos) > prom:
            c_vehiculos += 1
    return prom, c_vehiculos

