from Business.Bicicleta import Bicicleta
from Datos.BicicletaArchivo import BicicletaArchivo
from Funciones.BuscarArchivosDetalle import BuscarArchivosDetalle
import pandas as pd

class Detalle:

    _CantidadProducto:int
    _IdDetalle:str


    def __init__(self, producto:Bicicleta):

        self._Producto = producto

    def CrearDetalle(self):

        detalle = None

        while detalle == None:
            
            print("¿Que Quiere Hacer?")
            print("1. Crear Detalle de Factura")
            print("2. Buscar un Detalle de Factura")
            num = int(input("Introduzca un numero: "))

            if num == 1:

                referencia = None
                disenos = None

                bicicleta = Bicicleta(referencia, disenos)

                valores_bicicleta = bicicleta.CrearBicicleta()
                bicicleta = valores_bicicleta[0]

                if valores_bicicleta[1] == 1:
                    print("Archivo creado con exito")
                elif valores_bicicleta[1] == 2:
                    print("Archivo cargado con exito")

                bicicletaarchivo = BicicletaArchivo()
                bicicletaarchivo.GenerarTXT(bicicleta)

                detalle = Detalle(bicicleta)

                detalle._Producto = bicicleta
                detalle._CantidadProducto = int(input("Introduzca la cantidad de la bicicleta comprada: "))
                detalle._IdDetalle = input("Introduzca la ID del detalle: ")

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")
                
                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/Detalle/{nombre_archivo}.csv').empty == False:
                        
                        df_detalle = pd.read_csv(f'Datos/Archivos_Guardados/Detalle/{nombre_archivo}.csv')

                        bicicleta = BuscarArchivosDetalle(nombre_archivo)

                        detalle = Detalle(bicicleta)

                        detalle._Producto = bicicleta
                        detalle._CantidadProducto = int(df_detalle["|CantidadProducto|"][0])
                        detalle._IdDetalle = str(df_detalle["|ID Detalle|"][0])
   
                except FileNotFoundError:
                    print("No se encontro el archivo")

        return detalle, num