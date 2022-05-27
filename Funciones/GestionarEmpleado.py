from Business.Empleado import Empleado
import pandas as pd

def GestionarEmpleado():

    empleado = None

    while empleado == None:
        
        print("¿Que Quiere Hacer?")
        print("1. Crear un Perfil de Empleado")
        print("2. Buscar un Perfil de Empleado")
        num = int(input("Introduzca un numero: "))

        if num == 1:
            
            empleado = Empleado()

            nombre = input("Introduzca un nombre: ")
            apellido = input("Introduzca un apellido: ")
            idpersona = input("Introduzca una identificacion: ")
            telefono = int(input("Introduzca un numero de telefono: "))
            direccion = input("Introduzca una direccion: ")
            sueldo = int(input("Introduzca el sueldo del empleado: "))
            correoempresa = input("Introduzca el correo de la empresa del empleado: ")
            login = input("Introduzca el usuario del empleado: ")
            contrasena = input("Introduzca la contrasena del empleado: ")

            empleado = Empleado()

            empleado.CrearPersona(nombre, apellido, idpersona, telefono, direccion)
            empleado.CrearEmpleado(sueldo, correoempresa, login, contrasena)

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")

            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Empleado/{nombre_archivo}.csv').empty == False:

                    df_empleado = pd.read_csv(f'Datos/Archivos_Guardados/Empleado/{nombre_archivo}.csv')

                    nombre = str(df_empleado["|Nombre|"][0])
                    apellido = str(df_empleado["|Apellido|"][0])
                    idpersona = str(df_empleado["|ID Persona|"][0])
                    telefono = int(df_empleado["|Telefono|"][0])
                    direccion = str(df_empleado["|Direccion|"][0])
                    sueldo = int(df_empleado["|Sueldo|"][0])
                    correoempresa = str(df_empleado["|CorreoEmpresa|"][0])
                    login = str(df_empleado["|Login|"][0])
                    contrasena = str(df_empleado["|Contrasena|"][0])

                    empleado = Empleado()

                    empleado.CrearPersona(nombre, apellido, idpersona, telefono, direccion)
                    empleado.CrearEmpleado(sueldo, correoempresa, login, contrasena)

            except FileNotFoundError:
                print("No se encontro el archivo")

    return empleado, num