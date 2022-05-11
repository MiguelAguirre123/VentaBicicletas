from Business.Diseno import Diseno
from Business.Empleado import Empleado
from Business.InventarioReferencia import InventarioReferencia
from Business.Referencia import Referencia
import pandas as pd

def BuscarArchivosSede(nombre_archivo:str):

    inventariosede = []
    empleados = []

    df_sede = pd.read_csv(f'Datos/Archivos_Guardados/Sede/{nombre_archivo}.csv')

    contador_inventarioreferencia = 0
    contador_empleados = 0

    try:
        while contador_empleados > -1:
            str(df_sede[f"|Nombre||{contador_empleados+1}|"][0])
            contador_empleados += 1
    except KeyError:
        shape = df_sede.shape
        num_inventarioreferencia = int((shape[1] - (4 + contador_empleados*9))/8)

    try:
        while contador_inventarioreferencia > -1:
            str(df_sede[f"|Nombre Referencia||{contador_inventarioreferencia+1}|"][0])
            contador_inventarioreferencia += 1
    except KeyError:
        shape = df_sede.shape
        num_empleados = int((shape[1] - (4 + contador_inventarioreferencia*8))/9)

    for contador_archivos in range(num_inventarioreferencia):

        diseno = Diseno()

        diseno._Color1 = str(df_sede[f"|Color 1||{contador_archivos+1}|"][0])
        diseno._Color2 = str(df_sede[f"|Color 2||{contador_archivos+1}|"][0])
        diseno._IdDiseno = str(df_sede[f"|ID Diseno||{contador_archivos+1}|"][0])

        referencia = Referencia()

        referencia._NombreReferencia = str(df_sede[f"|Nombre Referencia||{contador_archivos+1}|"][0])        

        inventarioreferencia = InventarioReferencia(referencia, diseno)

        inventarioreferencia._Referenciacion = referencia
        inventarioreferencia._Diseno = diseno
        inventarioreferencia._CantidadBodega = int(df_sede[f"|CantidadBodega||{contador_archivos+1}|"][0])
        inventarioreferencia._CantidadMostrador = int(df_sede[f"|CantidadMostrador||{contador_archivos+1}|"][0])
        inventarioreferencia._CantidadVendida = int(df_sede[f"|CantidadVendida||{contador_archivos+1}|"][0])
        inventarioreferencia._IdInventario = str(df_sede[f"|ID Inventario||{contador_archivos+1}|"][0])   
        inventariosede.append(inventarioreferencia) 

    for contador_archivos in range(num_empleados):

        empleado = Empleado()

        empleado.Nombre = str(df_sede[f"|Nombre||{contador_archivos+1}|"][0])
        empleado.Apellido = str(df_sede[f"|Apellido||{contador_archivos+1}|"][0])
        empleado.IdPersona = str(df_sede[f"|ID Persona||{contador_archivos+1}|"][0])
        empleado.Telefono = int(df_sede[f"|Telefono||{contador_archivos+1}|"][0])
        empleado.Direccion = str(df_sede[f"|Direccion||{contador_archivos+1}|"][0])
        empleado._Sueldo = int(df_sede[f"|Sueldo||{contador_archivos+1}|"][0])
        empleado._CorreoEmpresa = str(df_sede[f"|CorreoEmpresa||{contador_archivos+1}|"][0])
        empleado._Login = str(df_sede[f"|Login||{contador_archivos+1}|"][0])
        empleado._Contrasena = str(df_sede[f"|Contrasena||{contador_archivos+1}|"][0])
        empleados.append(empleado)

    return inventariosede, empleados