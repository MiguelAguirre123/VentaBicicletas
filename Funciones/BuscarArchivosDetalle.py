from Business.Bicicleta import Bicicleta
from Business.Diseno import Diseno
from Business.Referencia import Referencia
import pandas as pd

def BuscarArchivosDetalle(nombre_archivo:str):

    disenos = []

    df_detalle = pd.read_csv(f'Datos/Archivos_Guardados/Detalle/{nombre_archivo}.csv')

    referencia = Referencia()

    referencia._NombreReferencia = str(df_detalle["|Nombre Referencia|"][0])

    shape = df_detalle.shape
    num_disenos = int((shape[1] - 8)/3)

    for contador_disenos in range(num_disenos):

        diseno = Diseno()

        diseno._Color1 = str(df_detalle[f"|Color 1||{contador_disenos+1}|"][0])
        diseno._Color2 = str(df_detalle[f"|Color 2||{contador_disenos+1}|"][0])
        diseno._IdDiseno = str(df_detalle[f"|ID Diseno||{contador_disenos+1}|"][0])
        disenos.append(diseno)

    bicicleta = Bicicleta(referencia, disenos)

    bicicleta.NombreBici = str(df_detalle["|NombreBici|"][0])
    bicicleta.Referenciacion = referencia
    bicicleta.Disenos = disenos
    bicicleta.NumVelocidades = int(df_detalle["|NumVelocidades|"][0])
    bicicleta.Material = str(df_detalle["|Material|"][0])
    bicicleta.IdBicicleta = str(df_detalle["|ID|"][0])
    bicicleta.TipoBici = str(df_detalle["|TipoBici|"][0])
    bicicleta.TamanoBici = str(df_detalle["|TamanoBici|"][0])
    bicicleta.Valor = int(df_detalle["|Valor|"][0])

    return bicicleta