from Business.Diseno import Diseno
from Business.Referencia import Referencia
import pandas as pd

def BuscarArchivosSede(nombre_archivo):

    inventariosede = []
    empleados = []

    df_sede = pd.read_csv(f'Datos/Archivos_Guardados/Sede/{nombre_archivo}.csv')

    shape = df_sede.shape
    num_disenos = int((shape[1] - 8)/3)

    for contador_disenos in range(num_disenos):

        diseno = Diseno()

        diseno._Color1 = str(df_bicicleta[f"|Color 1||{contador_disenos+1}|"][0])
        diseno._Color2 = str(df_bicicleta[f"|Color 2||{contador_disenos+1}|"][0])
        diseno._IdDiseno = str(df_bicicleta[f"|ID Diseno||{contador_disenos+1}|"][0])
        disenos.append(diseno)

    return referencia, disenos