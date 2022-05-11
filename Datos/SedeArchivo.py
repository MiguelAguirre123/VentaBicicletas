from Business.Empleado import Empleado
from Business.InventarioReferencia import InventarioReferencia
from Business.Sede import Sede
import pandas as pd

class SedeArchivo:
    
    def GenerarTXT(self, sede:Sede):

        datos_sede = {"|Nombre|":sede.Nombre, "|Direccion|":sede.Direccion,
        "|Ciudad|":sede.Ciudad, "|ID Sede|":sede.IdSede}  

        nombre_archivo = f'Datos/Archivos_Guardados/Sede/{sede.IdSede}.csv'
        df = pd.DataFrame(data=datos_sede,index=[0])

        contador_inventarioreferencia:InventarioReferencia
        contador_empleado:Empleado

        for contador_inventarioreferencia in sede.InventarioSede:

            df_inventarioreferencia = pd.read_csv(f'Datos/Archivos_Guardados/InventarioReferencia/{contador_inventarioreferencia._IdInventario}.csv')
            df_inventarioreferencia = df_inventarioreferencia.add_suffix(f'|{sede.InventarioSede.index(contador_inventarioreferencia)+1}|')
            df = pd.merge(df, df_inventarioreferencia, right_index=True, left_index=True, how='outer')
        
        for contador_empleado in sede.Empleados:

            df_empleado = pd.read_csv(f'Datos/Archivos_Guardados/Empleado/{contador_empleado.IdPersona}.csv')
            df_empleado = df_empleado.add_suffix(f'|{sede.Empleados.index(contador_empleado)+1}|')
            df = pd.merge(df, df_empleado, right_index=True, left_index=True, how='outer')                 

        print(df)
        df.to_csv(nombre_archivo, index=False) 