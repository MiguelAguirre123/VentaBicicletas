from Business.Diseno import Diseno
from Business.Referencia import Referencia
import pandas as pd

def BuscarArchivosInventario(nombre_archivo:str):

    df_inventarioreferencia = pd.read_csv(f'Datos/Archivos_Guardados/InventarioReferencia/{nombre_archivo}.csv')

    nombrereferencia = str(df_inventarioreferencia["|Nombre Referencia|"][0])

    referencia = Referencia()

    referencia.CrearReferencia(nombrereferencia)

    color1 = str(df_inventarioreferencia["|Color 1|"][0])
    color2 = str(df_inventarioreferencia["|Color 2|"][0])
    iddiseno = str(df_inventarioreferencia["|ID Diseno|"][0])

    diseno = Diseno()

    diseno.CrearDiseno(color1, color2, iddiseno)

    return referencia, diseno