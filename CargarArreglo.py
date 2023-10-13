import pickle
import os.path
from Clases import *

#Cargar vector por archivo de texto
def cargarArchivo(FD):
    registros = open(FD, "wb")
    if not os.path.exists("peajes-tp4.csv"):
        print("No existe el archivo de registros...")
    else:
        name = "peajes-tp4.csv"

        peajes = open(name, "r")
        lineas = peajes.readlines()

        # El for comienza en 2 salteando timestamp y campos
        for i in range(2, len(lineas)):
            linea = lineas[i]
            campos = linea.split(",")
            x = Ticket(int(campos[0]), campos[1], int(campos[2]), int(campos[3]), int(campos[4]), int(campos[5]))
            pickle.dump(x, registros)

        peajes.close()
        registros.close()
        return True
