from Business.Persona import Persona
import pandas as pd

class Empleado(Persona):

    _Sueldo:int
    _CorreoEmpresa:str
    _Login:str
<<<<<<< HEAD
    _Contrasena:str

    def CrearEmpleado(self):

        lista_telefono = []
        empleado = None

        while empleado == None:
            
            print("¿Que Quiere Hacer?")
            print("1. Crear un Perfil de Empleado")
            print("2. Buscar un Perfil de Empleado")
            num = int(input("Introduzca un numero: "))

            if num == 1:
                
                empleado = Empleado()

                empleado.Nombre = input("Introduzca un nombre: ")
                empleado.Apellido = input("Introduzca un apellido: ")
                empleado.IdPersona = input("Introduzca una identificacion: ")
                empleado.Telefono = list(map(int, input("Introduzca una lista de telefonos: ").rstrip().split()))
                empleado.Direccion = input("Introduzca una direccion: ")
                empleado._Sueldo = int(input("Introduzca el sueldo del empleado: "))
                empleado._CorreoEmpresa = input("Introduzca el correo de la empresa del empleado: ")
                empleado._Login = input("Introduzca el usuario del empleado: ")
                empleado._Contrasena = input("Introduzca la contrasena del empleado: ")

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")

                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/Empleado/{nombre_archivo}.csv').empty == False:

                        df_empleado = pd.read_csv(f'Datos/Archivos_Guardados/Empleado/{nombre_archivo}.csv')

                        empleado = Empleado()

                        empleado.Nombre = str(df_empleado["|Nombre|"][0])
                        empleado.Apellido = str(df_empleado["|Apellido|"][0])
                        empleado.IdPersona = str(df_empleado["|ID Persona|"][0])
                        empleado.Direccion = str(df_empleado["|Direccion|"][0])
                        empleado._Sueldo = int(df_empleado["|Sueldo|"][0])
                        empleado._CorreoEmpresa = str(df_empleado["|CorreoEmpresa|"][0])
                        empleado._Login = str(df_empleado["|Login|"][0])
                        empleado._Contrasena = str(df_empleado["|Contrasena|"][0])

                        shape = df_empleado.shape

                        for contador_telefonos in range(shape[0]):

                            lista_telefono.append(int(df_empleado["|Telefono|"][contador_telefonos]))

                        empleado.Telefono = lista_telefono

                except FileNotFoundError:
                    print("No se encontro el archivo")

        return empleado, num
=======
    _Contraseña:str
>>>>>>> 66bd4a2f57680edb34ac7e8af71d54b60e88daac
