import pandas as pd
from Business.Detalle import Detalle

class DetalleArchivo:
    
    def GenerarTXT(self, detalle:Detalle):

        datos_detalle = {"|ID Detalle|":detalle._IdDetalle, "|CantidadProducto|":detalle._CantidadProducto}

        nombre_archivo = f'Datos/Archivos_Guardados/Detalle/{detalle._IdDetalle}.csv'
        df = pd.DataFrame(data=datos_detalle,index=[0])

        df_bicicleta = pd.read_csv(f'Datos/Archivos_Guardados/Bicicleta/{detalle._Producto.NombreBici}.csv')
        df = pd.merge(df, df_bicicleta, right_index=True, left_index=True, how='outer')            

        print(df)
        df.to_csv(nombre_archivo, index=False) 