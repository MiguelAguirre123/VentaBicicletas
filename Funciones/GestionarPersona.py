from Business.Persona import Persona
import pandas as pd

def GestionarPersona():

    persona = None

    while persona == None:

        print("¿Que Quiere Hacer?")
        print("1. Crear un perfil de cliente")
        print("2. Buscar una un perfil de cliente existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            nombre = input("Introduzca un nombre: ")
            apellido = input("Introduzca un apellido: ")
            idpersona = input("Introduzca una identificacion: ")
            telefono = int(input("Introduzca un numero de telefono: "))
            direccion = input("Introduzca una direccion: ")

            persona = Persona()

            persona.CrearPersona(nombre, apellido, idpersona, telefono, direccion)

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")

            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Persona/{nombre_archivo}.csv').empty == False:

                    df_persona = pd.read_csv(f'Datos/Archivos_Guardados/Persona/{nombre_archivo}.csv')

                    persona = Persona()

                    nombre = str(df_persona["|Nombre|"][0])
                    apellido = str(df_persona["|Apellido|"][0])
                    idpersona = str(df_persona["|ID Persona|"][0])
                    telefono = int(df_persona["|Telefono|"][0])
                    direccion = str(df_persona["|Direccion|"][0])    

                    persona = Persona()

                    persona.CrearPersona(nombre, apellido, idpersona, telefono, direccion)            

            except FileNotFoundError:
                print("No se encontro el archivo")

    return persona, num    