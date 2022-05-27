from Business.Diseno import Diseno
import pandas as pd

def GestionarDiseno():

    diseno = None

    while diseno == None:
        
        print("¿Que Quiere Hacer?")
        print("1. Crear un diseno")
        print("2. Buscar un diseno existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            color1 = input("Introduzca un primer color en hexadecimal: ")
            color2 = input("Introduzca un segundo color en hexadecimal: ")
            iddiseno = input("Introduzca la identificacion del diseno: ")

            diseno = Diseno()

            diseno.CrearDiseno(color1, color2, iddiseno)

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")

            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{nombre_archivo}.csv').empty == False:

                    df_diseno = pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{nombre_archivo}.csv')

                    color1 = str(df_diseno["|Color 1|"][0])
                    color2 = str(df_diseno["|Color 2|"][0])
                    iddiseno = str(df_diseno["|ID Diseno|"][0])

                    diseno = Diseno()

                    diseno.CrearDiseno(color1, color2, iddiseno)

            except FileNotFoundError:
                print("No se encontro el archivo")

    return diseno, num