from Business.Diseno import Diseno
from Business.Referencia import Referencia
from Datos.DisenoArchivo import DisenoArchivo
from Datos.ReferenciaArchivo import ReferenciaArchivo
from Funciones.BuscarArchivosInventario import BuscarArchivosInventario
import pandas as pd

class InventarioReferencia:

    _CantidadBodega:int
    _CantidadMostrador:int
    _CantidadVendida:int
<<<<<<< HEAD
    _IdInventario:str
=======
>>>>>>> 66bd4a2f57680edb34ac7e8af71d54b60e88daac


    def __init__(self, referencia:Referencia, diseno:Diseno):

<<<<<<< HEAD
        self._Referenciacion = referencia
        self._Diseno = diseno

    def CrearInventarioReferencia(self):

        inventarioreferencia = None

        while inventarioreferencia == None:

            print("¿Que Quiere Hacer?")
            print("1. Crear un inventario")
            print("2. Buscar un inventario existente")
            num = int(input("Introduzca un numero: "))

            if num == 1:

                diseno = Diseno()

                valores_diseno = diseno.CrearDiseno()
                diseno = valores_diseno[0]

                if valores_diseno[1] == 1:
                     print("Archivo creado con exito")
                elif valores_diseno[1] == 2:
                    print("Archivo cargado con exito")

                disenoarchivo = DisenoArchivo()
                disenoarchivo.GenerarTXT(diseno)

                referencia = Referencia()
    
                valores_referencia = referencia.CrearReferencia()
                referencia = valores_referencia[0]

                if valores_referencia[1] == 1:
                    print("Archivo creado con exito")
                elif valores_referencia[1] == 2:
                    print("Archivo cargado con exito")

                referenciaarchivo = ReferenciaArchivo()
                referenciaarchivo.GenerarTXT(referencia)

                inventarioreferencia = InventarioReferencia(referencia, diseno)

                inventarioreferencia._Referenciacion = referencia
                inventarioreferencia._Diseno = diseno
                inventarioreferencia._CantidadBodega = int(input("Introduzca la cantidad que hay en la bodega: "))
                inventarioreferencia._CantidadMostrador = int(input("Introduzca la cantidad que hay en el mostrador: "))
                inventarioreferencia._CantidadVendida = int(input("Introduzca la cantidad que fue vendida: "))
                inventarioreferencia._IdInventario = input("Introduzca la identificacion del inventario: ")

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")
                
                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/InventarioReferencia/{nombre_archivo}.csv').empty == False:
                        
                        df_inventarioreferencia = pd.read_csv(f'Datos/Archivos_Guardados/InventarioReferencia/{nombre_archivo}.csv')
                        
                        valores_archivosinventario = BuscarArchivosInventario(nombre_archivo)

                        referencia = valores_archivosinventario[0]
                        diseno = valores_archivosinventario[1]

                        inventarioreferencia = InventarioReferencia(referencia, diseno)

                        inventarioreferencia._Referenciacion = referencia
                        inventarioreferencia._Diseno = diseno
                        inventarioreferencia._CantidadBodega = int(df_inventarioreferencia["|CantidadBodega|"][0])
                        inventarioreferencia._CantidadMostrador = int(df_inventarioreferencia["|CantidadMostrador|"][0])
                        inventarioreferencia._CantidadVendida = int(df_inventarioreferencia["|CantidadVendida|"][0])
                        inventarioreferencia._IdInventario = str(df_inventarioreferencia["|ID Inventario|"][0])

                except FileNotFoundError:
                    print("No se encontro el archivo")              

        return inventarioreferencia, num           
=======
        self._Relacion = referencia
        self._Disenos = disenos
>>>>>>> 66bd4a2f57680edb34ac7e8af71d54b60e88daac
