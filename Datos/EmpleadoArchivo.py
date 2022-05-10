import pandas as pd
from Business.Empleado import Empleado

class EmpleadoArchivo:
    
    def GenerarTXT(self, empleado:Empleado):

        datos_empleado = {"|Nombre|":pd.Series(empleado.Nombre,index=[0]), "|Apellido|":pd.Series(empleado.Apellido,index=[0]),
        "|ID Persona|":pd.Series(empleado.IdPersona,index=[0]), "|Telefono|":pd.Series(empleado.Telefono,index=list(range(len(empleado.Telefono)))),
        "|Direccion|":pd.Series(empleado.Direccion,index=[0]), "|Sueldo|":pd.Series(empleado._Sueldo,index=[0]),
        "|CorreoEmpresa|":pd.Series(empleado._CorreoEmpresa ,index=[0]), "|Login|":pd.Series(empleado._Login,index=[0]),
        "|Contrasena|":pd.Series(empleado._Contrasena,index=[0])}

        nombre_archivo = f'Datos/Archivos_Guardados/Empleado/{empleado.Nombre} {empleado.Apellido}.csv'
        df = pd.DataFrame(data=datos_empleado, index=range(len(empleado.Telefono)))

        print(df)
        df.to_csv(nombre_archivo, index=False) 