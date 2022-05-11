import pandas as pd

class Persona:

    Nombre:str
    Apellido:str
    IdPersona:str
    Telefono:int
    Direccion:str

    def CrearPersona(self):

        persona = None

        while persona == None:

            print("¿Que Quiere Hacer?")
            print("1. Crear un perfil de cliente")
            print("2. Buscar una un perfil de cliente existente")
            num = int(input("Introduzca un numero: "))

            if num == 1:

                persona = Persona()

                persona.Nombre = input("Introduzca un nombre: ")
                persona.Apellido = input("Introduzca un apellido: ")
                persona.IdPersona = input("Introduzca una identificacion: ")
                persona.Telefono = int(input("Introduzca un numero de telefono: "))
                persona.Direccion = input("Introduzca una direccion: ")

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")

                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/Persona/{nombre_archivo}.csv').empty == False:

                        df_persona = pd.read_csv(f'Datos/Archivos_Guardados/Persona/{nombre_archivo}.csv')

                        persona = Persona()

                        persona.Nombre = str(df_persona["|Nombre|"][0])
                        persona.Apellido = str(df_persona["|Apellido|"][0])
                        persona.IdPersona = str(df_persona["|ID Persona|"][0])
                        persona.Telefono = int(df_persona["|Telefono|"][0])
                        persona.Direccion = str(df_persona["|Direccion|"][0])                       

                except FileNotFoundError:
                    print("No se encontro el archivo")

        return persona, num      