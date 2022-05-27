from Business.InventarioReferencia import InventarioReferencia
from Datos.DisenoArchivo import DisenoArchivo
from Datos.ReferenciaArchivo import ReferenciaArchivo
from Funciones.BuscarArchivosInventario import BuscarArchivosInventario
from Funciones.GestionarDiseno import GestionarDiseno
from Funciones.GestionarReferencia import GestionarReferencia
import pandas as pd

def GestionarInventarioReferencia():

    inventarioreferencia = None

    while inventarioreferencia == None:

        print("¿Que Quiere Hacer?")
        print("1. Crear un inventario")
        print("2. Buscar un inventario existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            valores_diseno = GestionarDiseno()
            diseno = valores_diseno[0]

            if valores_diseno[1] == 1:
                    print("Archivo creado con exito")
            elif valores_diseno[1] == 2:
                print("Archivo cargado con exito")

            disenoarchivo = DisenoArchivo()
            disenoarchivo.GenerarTXT(diseno)

            valores_referencia = GestionarReferencia()
            referencia = valores_referencia[0]

            if valores_referencia[1] == 1:
                print("Archivo creado con exito")
            elif valores_referencia[1] == 2:
                print("Archivo cargado con exito")

            referenciaarchivo = ReferenciaArchivo()
            referenciaarchivo.GenerarTXT(referencia)

            cantidadbodega = int(input("Introduzca la cantidad que hay en la bodega: "))
            cantidadmostrador = int(input("Introduzca la cantidad que hay en el mostrador: "))
            cantidadvendida = int(input("Introduzca la cantidad que fue vendida: "))
            idinventario = input("Introduzca la identificacion del inventario: ")

            inventarioreferencia = InventarioReferencia(referencia, diseno)

            inventarioreferencia.CrearInventarioReferencia(cantidadbodega, cantidadmostrador, cantidadvendida, idinventario)

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")
            
            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/InventarioReferencia/{nombre_archivo}.csv').empty == False:
                    
                    df_inventarioreferencia = pd.read_csv(f'Datos/Archivos_Guardados/InventarioReferencia/{nombre_archivo}.csv')
                    
                    valores_archivosinventario = BuscarArchivosInventario(nombre_archivo)

                    referencia = valores_archivosinventario[0]
                    diseno = valores_archivosinventario[1]

                    cantidadbodega = int(df_inventarioreferencia["|CantidadBodega|"][0])
                    cantidadmostrador = int(df_inventarioreferencia["|CantidadMostrador|"][0])
                    cantidadvendida = int(df_inventarioreferencia["|CantidadVendida|"][0])
                    idinventario = str(df_inventarioreferencia["|ID Inventario|"][0])

                    inventarioreferencia = InventarioReferencia(referencia, diseno)

                    inventarioreferencia.CrearInventarioReferencia(cantidadbodega, cantidadmostrador, cantidadvendida, idinventario)

            except FileNotFoundError:
                print("No se encontro el archivo")              

    return inventarioreferencia, num      