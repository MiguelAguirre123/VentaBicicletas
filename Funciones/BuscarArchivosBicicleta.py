from Business.Diseno import Diseno
from Business.Referencia import Referencia
import pandas as pd

def BuscarArchivosBicicleta(nombre_archivo:str):

    disenos = []

    df_bicicleta = pd.read_csv(f'Datos/Archivos_Guardados/Bicicleta/{nombre_archivo}.csv')

    nombrereferencia = str(df_bicicleta["|Nombre Referencia|"][0])

    referencia = Referencia()

    referencia.CrearReferencia(nombrereferencia)

    shape = df_bicicleta.shape
    num_disenos = int((shape[1] - 8)/3)

    for contador_disenos in range(num_disenos):

        color1 = str(df_bicicleta[f"|Color 1||{contador_disenos+1}|"][0])
        color2 = str(df_bicicleta[f"|Color 2||{contador_disenos+1}|"][0])
        iddiseno = str(df_bicicleta[f"|ID Diseno||{contador_disenos+1}|"][0])

        diseno = Diseno()

        diseno.CrearDiseno(color1, color2, iddiseno)

        disenos.append(diseno)

    return referencia, disenos
