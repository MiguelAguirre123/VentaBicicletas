from Business.Bicicleta import Bicicleta
from Business.Diseno import Diseno
from Business.Referencia import Referencia
import pandas as pd

def BuscarArchivosDetalle(nombre_archivo:str):

    disenos = []

    df_detalle = pd.read_csv(f'Datos/Archivos_Guardados/Detalle/{nombre_archivo}.csv')

    nombrereferencia = str(df_detalle["|Nombre Referencia|"][0])

    referencia = Referencia()

    referencia.CrearReferencia(nombrereferencia)

    shape = df_detalle.shape
    num_disenos = int((shape[1] - 8)/3)

    for contador_disenos in range(num_disenos):

        color1 = str(df_detalle[f"|Color 1||{contador_disenos+1}|"][0])
        color2 = str(df_detalle[f"|Color 2||{contador_disenos+1}|"][0])
        iddiseno = str(df_detalle[f"|ID Diseno||{contador_disenos+1}|"][0])

        diseno = Diseno()

        diseno.CrearDiseno(color1, color2, iddiseno)

        disenos.append(diseno)

    nombrebici = str(df_detalle["|NombreBici|"][0])
    numvelocidades = int(df_detalle["|NumVelocidades|"][0])
    material = str(df_detalle["|Material|"][0])
    idbicicleta = str(df_detalle["|ID|"][0])
    tipobici = str(df_detalle["|TipoBici|"][0])
    tamanobici = str(df_detalle["|TamanoBici|"][0])
    valor = int(df_detalle["|Valor|"][0])

    bicicleta = Bicicleta(referencia, disenos)

    bicicleta.CrearBicicleta(nombrebici, numvelocidades, material,
    idbicicleta, tipobici, tamanobici, valor)

    return bicicleta