from Business.Referencia import Referencia
import pandas as pd

def GestionarReferencia():

    referencia = None

    while referencia == None:

        print("¿Que Quiere Hacer?")
        print("1. Crear un referencia")
        print("2. Buscar una referencia existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            nombrereferencia = input("Introduzca el nombre de la referencia: ")

            referencia = Referencia()

            referencia.CrearReferencia(nombrereferencia)

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")

            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{nombre_archivo}.csv').empty == False:

                    df_referencia = pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{nombre_archivo}.csv')

                    nombrereferencia = str(df_referencia["|Nombre Referencia|"][0])

                    referencia = Referencia()

                    referencia.CrearReferencia(nombrereferencia)

            except FileNotFoundError:
                print("No se encontro el archivo")

    return referencia, num