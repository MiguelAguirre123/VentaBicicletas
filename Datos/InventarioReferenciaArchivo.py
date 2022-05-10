import pandas as pd
from Business.InventarioReferencia import InventarioReferencia

class InventarioReferenciaArchivo:
    
    def GenerarTXT(self, inventarioreferencia:InventarioReferencia):

        datos_inventario = {"|ID Inventario|":inventarioreferencia._IdInventario, "|CantidadBodega|":inventarioreferencia._CantidadBodega,
        "|CantidadMostrador|":inventarioreferencia._CantidadMostrador, "|CantidadVendida|":inventarioreferencia._CantidadVendida}

        nombre_archivo = f'Datos/Archivos_Guardados/InventarioReferencia/{inventarioreferencia._IdInventario}.csv'
        df = pd.DataFrame(data=datos_inventario,index=[0])

        df_diseno = pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{inventarioreferencia._Diseno._IdDiseno}.csv')
        df = pd.merge(df_diseno, df, right_index=True, left_index=True, how='outer')  
        
        df_referencia = pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{inventarioreferencia._Referenciacion._NombreReferencia}.csv')
        df = pd.merge(df_referencia, df, right_index=True, left_index=True, how='outer')                

        print(df)
        df.to_csv(nombre_archivo, index=False) 