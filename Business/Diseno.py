import pandas as pd

class Diseno:

    _Color1:str
    _Color2:str
    _IdDiseno:str

    def CrearDiseno(self):

        diseno = None

        while diseno == None:
            
            print("¿Que Quiere Hacer?")
            print("1. Crear un diseno")
            print("2. Buscar un diseno existente")
            num = int(input("Introduzca un numero: "))

            if num == 1:
                
                diseno = Diseno()

                diseno._Color1 = input("Introduzca un primer color en hexadecimal: ")
                diseno._Color2 = input("Introduzca un segundo color en hexadecimal: ")
                diseno._IdDiseno = input("Introduzca la identificacion del diseno: ")

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")

                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{nombre_archivo}.csv').empty == False:

                        df_diseno = pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{nombre_archivo}.csv')

                        diseno = Diseno()

                        diseno._Color1 = str(df_diseno["|Color 1|"][0])
                        diseno._Color2 = str(df_diseno["|Color 2|"][0])
                        diseno._IdDiseno = str(df_diseno["|ID Diseno|"][0])

                except FileNotFoundError:
                    print("No se encontro el archivo")

        return diseno, num