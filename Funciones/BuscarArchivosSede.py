from Business.Diseno import Diseno
from Business.Empleado import Empleado
from Business.InventarioReferencia import InventarioReferencia
from Business.Referencia import Referencia
import pandas as pd

def BuscarArchivosSede(nombre_archivo:str):

    inventariosede = []
    empleados = []

    df_sede = pd.read_csv(f'Datos/Archivos_Guardados/Sede/{nombre_archivo}.csv')

    num_inventarioreferencia = 0
    num_empleados = 0

    try:
        while num_empleados > -1:
            str(df_sede[f"|Nombre||{num_empleados+1}|"][0])
            num_empleados += 1
    except KeyError:
        pass

    try:
        while num_inventarioreferencia > -1:
            str(df_sede[f"|Nombre Referencia||{num_inventarioreferencia+1}|"][0])
            num_inventarioreferencia += 1
    except KeyError:
        pass

    for contador_archivos in range(num_inventarioreferencia):

        color1 = str(df_sede[f"|Color 1||{contador_archivos+1}|"][0])
        color2 = str(df_sede[f"|Color 2||{contador_archivos+1}|"][0])
        iddiseno = str(df_sede[f"|ID Diseno||{contador_archivos+1}|"][0])

        diseno = Diseno()

        diseno.CrearDiseno(color1, color2, iddiseno)       

        nombrereferencia = str(df_sede[f"|Nombre Referencia||{contador_archivos+1}|"][0])

        referencia = Referencia()

        referencia.CrearReferencia(nombrereferencia)   

        cantidadbodega = int(df_sede[f"|CantidadBodega||{contador_archivos+1}|"][0])
        cantidadmostrador = int(df_sede[f"|CantidadMostrador||{contador_archivos+1}|"][0])
        cantidadvendida = int(df_sede[f"|CantidadVendida||{contador_archivos+1}|"][0])
        idinventario = str(df_sede[f"|ID Inventario||{contador_archivos+1}|"][0])   

        inventarioreferencia = InventarioReferencia(referencia, diseno)

        inventarioreferencia.CrearInventarioReferencia(cantidadbodega, cantidadmostrador, cantidadvendida, idinventario)        

        inventariosede.append(inventarioreferencia) 

    for contador_archivos in range(num_empleados):

        nombre = str(df_sede[f"|Nombre||{contador_archivos+1}|"][0])
        apellido = str(df_sede[f"|Apellido||{contador_archivos+1}|"][0])
        idpersona = str(df_sede[f"|ID Persona||{contador_archivos+1}|"][0])
        telefono = int(df_sede[f"|Telefono||{contador_archivos+1}|"][0])
        direccion = str(df_sede[f"|Direccion||{contador_archivos+1}|"][0])
        sueldo = int(df_sede[f"|Sueldo||{contador_archivos+1}|"][0])
        correoempresa = str(df_sede[f"|CorreoEmpresa||{contador_archivos+1}|"][0])
        login = str(df_sede[f"|Login||{contador_archivos+1}|"][0])
        contrasena = str(df_sede[f"|Contrasena||{contador_archivos+1}|"][0])

        empleado = Empleado()

        empleado.CrearPersona(nombre, apellido, idpersona, telefono, direccion)
        empleado.CrearEmpleado(sueldo, correoempresa, login, contrasena)

        empleados.append(empleado)

    return inventariosede, empleados