from Business.Bicicleta import Bicicleta
from Business.Detalle import Detalle
from Business.Diseno import Diseno
from Business.Referencia import Referencia
import pandas as pd

def BuscarArchivosBicicleta(nombre_archivo:str):

    detalles = []
    disenos = []

    df_factura = pd.read_csv(f'Datos/Archivos_Guardados/Factura/{nombre_archivo}.csv')

    shape = df_factura.shape
    num_detalles = int((shape[1] - 14)/19)

    for contador_detalles in range(num_detalles):

        referencia = Referencia()

        referencia._NombreReferencia = str(df_factura[f"|Nombre Referencia||{contador_detalles+1}|"][0])

        try:
            while contador_inventarioreferencia > -1:
                str(df_sede[f"|Nombre Referencia||{contador_inventarioreferencia+1}|||"][0])
                contador_inventarioreferencia += 1
        except KeyError:
            shape = df_sede.shape
            num_empleados = int((shape[1] - (4 + contador_inventarioreferencia*8))/9)       

        shape = df_factura.shape
        num_disenos = int((shape[1] - (14 + (13*(contador_detalles - 1) + 16)))/3)

        for contador_disenos in range(num_disenos):

            diseno = Diseno()

            diseno._Color1 = str(df_factura[f"|Color 1||{contador_disenos+1}||{contador_detalles+1}|"][0])
            diseno._Color2 = str(df_factura[f"|Color 2||{contador_disenos+1}||{contador_detalles+1}|"][0])
            diseno._IdDiseno = str(df_factura[f"|ID Diseno||{contador_disenos+1}||{contador_detalles+1}|"][0])
            disenos.append(diseno)

        bicicleta = Bicicleta(referencia, disenos)

        bicicleta.NombreBici = str(df_factura["|NombreBici||{contador_detalles+1}|"][0])
        bicicleta.Referenciacion = referencia
        bicicleta.Disenos = disenos
        bicicleta.NumVelocidades = int(df_factura["|NumVelocidades||{contador_detalles+1}|"][0])
        bicicleta.Material = str(df_factura["|Material||{contador_detalles+1}|"][0])
        bicicleta.IdBicicleta = str(df_factura["|ID||{contador_detalles+1}|"][0])
        bicicleta.TipoBici = str(df_factura["|TipoBici||{contador_detalles+1}|"][0])
        bicicleta.TamanoBici = str(df_factura["|TamanoBici||{contador_detalles+1}|"][0])
        bicicleta.Valor = int(df_factura["|Valor||{contador_detalles+1}|"][0])

    return referencia, disenos