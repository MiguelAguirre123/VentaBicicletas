from Business.Empleado import Empleado
from Business.InventarioReferencia import InventarioReferencia
from Business.Sede import Sede
from Datos.EmpleadoArchivo import EmpleadoArchivo
from Datos.InventarioReferenciaArchivo import InventarioReferenciaArchivo
from Funciones.BuscarArchivosSede import BuscarArchivosSede
from Funciones.GestionarEmpleado import GestionarEmpleado
from Funciones.GestionarInventarioReferencia import GestionarInventarioReferencia
import pandas as pd

def GestionarSede():

    inventariosede = []
    inventarioreferencia_ID = []
    empleados = []
    empleado_ID = []

    sede = None

    while sede == None:

        print("¿Que Quiere Hacer?")
        print("1. Crear una Sede")
        print("2. Buscar una Sede existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            while num != 0:

                valores_invetarioreferencia = GestionarInventarioReferencia()
                inventarioreferencia = valores_invetarioreferencia[0]

                inventarioreferencia_ID.append(inventarioreferencia._IdInventario)

                if inventarioreferencia_ID.count(inventarioreferencia._IdInventario) == 1:
                    inventariosede.append(inventarioreferencia)

                    if valores_invetarioreferencia[1] == 1:
                        print("Archivo creado con exito")
                    elif valores_invetarioreferencia[1] == 2:
                        print("Archivo cargado con exito")

                else:

                    contador_inventarios:InventarioReferencia

                    for contador_inventarios in inventariosede:

                        if contador_inventarios._IdInventario == inventarioreferencia._IdInventario:

                            inventariosede[inventariosede.index(contador_inventarios)] = inventarioreferencia

                            if valores_invetarioreferencia[1] == 1:
                                print("El archivo creado con el mismo nombre de directorio fue modificado")
                            elif valores_invetarioreferencia[1] == 2:
                                print("El archivo ya fue subido anteriormente")

                inventarioreferenciaarchivo = InventarioReferenciaArchivo()
                inventarioreferenciaarchivo.GenerarTXT(inventarioreferencia)

                print("¿Que quiere hacer?")
                print("0. Salir del gestor de inventario")
                print("Cualquier otro numero para seguir en el gestor de inventario")
                num = int(input("Introduzca un numero: "))

            num = 1

            while num != 0:

                valores_empleado = GestionarEmpleado()
                empleado = valores_empleado[0]

                empleado_ID.append(empleado.IdPersona)

                if empleado_ID.count(empleado.IdPersona) == 1:
                    empleados.append(empleado)

                    if valores_empleado[1] == 1:
                        print("Archivo creado con exito")
                    elif valores_empleado[1] == 2:
                        print("Archivo cargado con exito")

                else:

                    contador_empleados:Empleado

                    for contador_empleados in empleados:

                        if contador_empleados.IdPersona == empleado.IdPersona:

                            empleados[empleados.index(contador_empleados)] = empleado

                            if valores_empleado[1] == 1:
                                print("El archivo creado con el mismo nombre de directorio fue modificado")
                            elif valores_empleado[1] == 2:
                                print("El archivo ya fue subido anteriormente")

                empleadoarchivo = EmpleadoArchivo()
                empleadoarchivo.GenerarTXT(empleado)

                print("¿Que quiere hacer?")
                print("0. Salir del gestor de Perfil de Empleado")
                print("Cualquier otro numero para seguir en el gestor de Perfil de Empleado")
                num = int(input("Introduzca un numero: "))

            nombre = input("Introduzca el nombre de la sede: ")
            direccion = input("Introduzca la direccion de la sede: ")
            ciudad = input("Introduzca la ciudad donde esta ubicada la sede: ")
            idsede = input("Introduzca la ID de la sede: ")

            sede = Sede(inventariosede, empleados)

            sede.CrearSede(nombre, direccion, ciudad, idsede)

            num = 1

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")
            
            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Sede/{nombre_archivo}.csv').empty == False:
                    
                    df_sede = pd.read_csv(f'Datos/Archivos_Guardados/Sede/{nombre_archivo}.csv')
                    
                    valores_archivossede = BuscarArchivosSede(nombre_archivo)

                    inventariosede = valores_archivossede[0]
                    empleados = valores_archivossede[1]

                    nombre = str(df_sede["|Nombre|"][0]) 
                    direccion = str(df_sede["|Direccion|"][0])
                    ciudad = str(df_sede["|Ciudad|"][0])
                    idsede = str(df_sede["|ID Sede|"][0])

                    sede = Sede(inventariosede, empleados)

                    sede.CrearSede(nombre, direccion, ciudad, idsede)

            except FileNotFoundError:
                print("No se encontro el archivo")   

    return sede, num