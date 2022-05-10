from Business.Diseno import Diseno
from Business.Referencia import Referencia
import pandas as pd

def BuscarArchivosInventario(nombre_archivo):

    df_inventarioreferencia = pd.read_csv(f'Datos/Archivos_Guardados/InventarioReferencia/{nombre_archivo}.csv')

    referencia = Referencia()

    referencia._NombreReferencia = str(df_inventarioreferencia["|Nombre Referencia|"][0])

    diseno = Diseno()

    diseno._Color1 = str(df_inventarioreferencia[f"|Color 1|"][0])
    diseno._Color2 = str(df_inventarioreferencia[f"|Color 2|"][0])
    diseno._IdDiseno = str(df_inventarioreferencia[f"|ID Diseno|"][0])

    return referencia, diseno