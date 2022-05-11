import pandas as pd
from Business.Empleado import Empleado

class EmpleadoArchivo:
    
    def GenerarTXT(self, empleado:Empleado):

        datos_empleado = {"|Nombre|":empleado.Nombre, "|Apellido|":empleado.Apellido,
        "|ID Persona|":empleado.IdPersona, "|Telefono|":empleado.Telefono,
        "|Direccion|":empleado.Direccion, "|Sueldo|":empleado._Sueldo,
        "|CorreoEmpresa|":empleado._CorreoEmpresa, "|Login|":empleado._Login,
        "|Contrasena|":empleado._Contrasena}

        nombre_archivo = f'Datos/Archivos_Guardados/Empleado/{empleado.IdPersona}.csv'
        df = pd.DataFrame(data=datos_empleado, index=[0])

        print(df)
        df.to_csv(nombre_archivo, index=False) 