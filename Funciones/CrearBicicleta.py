from Business.Bicicleta import Bicicleta
from Business.Diseno import Diseno
from Business.EnumMaterial import EnumMaterial
from Business.EnumTipoBici import EnumTipoBici
from Business.Referencia import Referencia
from Datos.BicicletaArchivo import BicicletaArchivo
from Datos.DisenoArchivo import DisenoArchivo
from Datos.ReferenciaArchivo import ReferenciaArchivo
import pandas as pd

def CrearBicicleta(num):

    disenos = []
    diseno_ID = []
        
    while num != 0:

        print("¿Que Quiere Hacer?")
        print("0. Salir de gestor de Diseno: ")
        print("1. Crear un diseno: ")
        print("2. Buscar un diseno existente: ")
        num = int(input("Introduzca un numero: "))

        if num == 1:
                
            diseno = Diseno()

            diseno._Color1 = input("Introduzca un primer color en hexadecimal: ")
            diseno._Color2 = input("Introduzca un segundo color en hexadecimal: ")
            diseno._Id = input("Introduzca la identificacion del diseno: ")

            diseno_ID.append(diseno._Id)

            if diseno_ID.count(diseno._Id) == 1:
                disenos.append(diseno)
            else:
                print("El archivo creado con el mismo nombre de directorio fue modificado")

            disenoarchivo = DisenoArchivo()
            disenoarchivo.GenerarTXT(diseno)   

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")

            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{nombre_archivo}.csv').empty == False:

                    diseno_ID.append(nombre_archivo)

                    if disenos.count(nombre_archivo) == 0 and diseno_ID.count(nombre_archivo) == 1:

                        disenos.append(nombre_archivo)
                        print("Archivo cargado con exito")
                        print(pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{nombre_archivo}.csv'))

                    else:
                        print("El archivo no se cargo porque ya fue subido anteriormente")

            except FileNotFoundError:
                print("No se encontro el archivo")

        elif num == 0 and len(disenos) == 0:
                
            print("Es necesario minimo un diseno para crear bicicleta")
            num = 1

    referencia_guardada = 0

    while referencia_guardada == 0:

        print("¿Que Quiere Hacer?")
        print("1. Crear un referencia: ")
        print("2. Buscar una referencia existente: ")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            referencia = Referencia()

            referencia._NombreReferencia = input("Introduzca el nombre de la referencia: ")

            referenciaarchivo = ReferenciaArchivo()
            referenciaarchivo.GenerarTXT(referencia)     

            referencia_guardada = referencia

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")

            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{nombre_archivo}.csv').empty == False:

                    referencia_guardada = nombre_archivo
                    print("Archivo cargado con exito")
                    print(pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{nombre_archivo}.csv'))

            except FileNotFoundError:
                print("No se encontro el archivo")

    bicicleta = Bicicleta(referencia_guardada, disenos)

    bicicleta.NombreBici = input("Introduzca el nombre de la bicicleta: ")
    bicicleta.Referenciacion = referencia_guardada
    bicicleta.Disenos = disenos
    bicicleta.NumVelocidades = input("Introduzca las velocidades de la bicicleta: ")
    bicicleta.Material = EnumMaterial(int(input("Introduzca el numero de material: "))).name
    bicicleta.Identificacion = input("Introduzca el ID de la bicicleta: ")
    bicicleta.TipoBici = EnumTipoBici(int(input("Introduzca el numero del tipo de bicicleta: "))).name
    bicicleta.TamanoBici = input("Introduzca el tamano de la bicicleta: ")
    bicicleta.Valor = input("Introduzca el valor comercial de la bicicleta: ")

    bicicletaarchivo = BicicletaArchivo()
    bicicletaarchivo.GenerarTXT(bicicleta)