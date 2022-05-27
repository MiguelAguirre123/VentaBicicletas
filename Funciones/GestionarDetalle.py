from Business.Detalle import Detalle
from Datos.BicicletaArchivo import BicicletaArchivo
from Funciones.BuscarArchivosDetalle import BuscarArchivosDetalle
from Funciones.GestionarBicicleta import GestionarBicicleta
import pandas as pd

def GestionarDetalle():

    detalle = None

    while detalle == None:
        
        print("¿Que Quiere Hacer?")
        print("1. Crear Detalle de Factura")
        print("2. Buscar un Detalle de Factura")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            valores_bicicleta = GestionarBicicleta()
            bicicleta = valores_bicicleta[0]

            if valores_bicicleta[1] == 1:
                print("Archivo creado con exito")
            elif valores_bicicleta[1] == 2:
                print("Archivo cargado con exito")

            bicicletaarchivo = BicicletaArchivo()
            bicicletaarchivo.GenerarTXT(bicicleta)

            cantidadproducto = int(input("Introduzca la cantidad de la bicicleta comprada: "))
            iddetalle = input("Introduzca la ID del detalle: ")

            detalle = Detalle(bicicleta)

            detalle.CrearDetalle(cantidadproducto, iddetalle)

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")
            
            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Detalle/{nombre_archivo}.csv').empty == False:
                    
                    df_detalle = pd.read_csv(f'Datos/Archivos_Guardados/Detalle/{nombre_archivo}.csv')

                    bicicleta = BuscarArchivosDetalle(nombre_archivo)

                    cantidadproducto = int(df_detalle["|CantidadProducto|"][0])
                    iddetalle = str(df_detalle["|ID Detalle|"][0])

                    detalle = Detalle(bicicleta)

                    detalle.CrearDetalle(cantidadproducto, iddetalle)

            except FileNotFoundError:
                print("No se encontro el archivo")

    return detalle, num