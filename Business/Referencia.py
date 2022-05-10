import pandas as pd

class Referencia:

<<<<<<< HEAD
    _NombreReferencia:str

    def CrearReferencia(self):

        referencia = None

        while referencia == None:

            print("¿Que Quiere Hacer?")
            print("1. Crear un referencia")
            print("2. Buscar una referencia existente")
            num = int(input("Introduzca un numero: "))

            if num == 1:

                referencia = Referencia()

                referencia._NombreReferencia = input("Introduzca el nombre de la referencia: ")

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")

                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{nombre_archivo}.csv').empty == False:

                        df_referencia = pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{nombre_archivo}.csv')

                        referencia = Referencia()

                        referencia._NombreReferencia = str(df_referencia["|Nombre Referencia|"][0])

                except FileNotFoundError:
                    print("No se encontro el archivo")

        return referencia, num
=======
    _NombreReferencia:str
>>>>>>> 66bd4a2f57680edb34ac7e8af71d54b60e88daac
