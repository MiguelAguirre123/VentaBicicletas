from Business.Bicicleta import Bicicleta
from Business.Diseno import Diseno
from Business.EnumMaterial import EnumMaterial
from Business.EnumTipoBici import EnumTipoBici
from Datos.DisenoArchivo import DisenoArchivo
from Datos.ReferenciaArchivo import ReferenciaArchivo
from Funciones.BuscarArchivosBicicleta import BuscarArchivosBicicleta
from Funciones.GestionarDiseno import GestionarDiseno
from Funciones.GestionarReferencia import GestionarReferencia
import pandas as pd

def GestionarBicicleta():

    disenos = []
    diseno_ID = []

    bicicleta = None

    while bicicleta == None:

        print("¿Que Quiere Hacer?")
        print("1. Crear una Bicicleta")
        print("2. Buscar una Bicicleta existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            while num != 0:

                valores_diseno = GestionarDiseno()
                diseno = valores_diseno[0]

                diseno_ID.append(diseno._IdDiseno)

                if diseno_ID.count(diseno._IdDiseno) == 1:
                    disenos.append(diseno)

                    if valores_diseno[1] == 1:
                        print("Archivo creado con exito")
                    elif valores_diseno[1] == 2:
                        print("Archivo cargado con exito")

                else:

                    contador_disenos:Diseno

                    for contador_disenos in disenos:

                        if contador_disenos._IdDiseno == diseno._IdDiseno:

                            disenos[disenos.index(contador_disenos)] = diseno

                            if valores_diseno[1] == 1:
                                print("El archivo creado con el mismo nombre de directorio fue modificado")
                            elif valores_diseno[1] == 2:
                                print("El archivo ya fue subido anteriormente")

                disenoarchivo = DisenoArchivo()
                disenoarchivo.GenerarTXT(diseno)

                print("¿Que quiere hacer?")
                print("0. Salir del gestor de diseno")
                print("Cualquier otro numero para seguir en el gestor de diseno")
                num = int(input("Introduzca un numero: "))

            valores_referencia = GestionarReferencia()
            referencia = valores_referencia[0]

            if valores_referencia[1] == 1:
                print("Archivo creado con exito")
            elif valores_referencia[1] == 2:
                print("Archivo cargado con exito")

            referenciaarchivo = ReferenciaArchivo()
            referenciaarchivo.GenerarTXT(referencia)

            nombrebici = input("Introduzca el nombre de la bicicleta: ")
            numvelocidades = int(input("Introduzca las velocidades de la bicicleta: "))
            material = EnumMaterial(int(input("Introduzca el numero de material: "))).name
            idbicicleta = input("Introduzca el ID de la bicicleta: ")
            tipobici = EnumTipoBici(int(input("Introduzca el numero del tipo de bicicleta: "))).name
            tamanobici = input("Introduzca el tamano de la bicicleta: ")
            valor = int(input("Introduzca el valor comercial de la bicicleta: "))

            bicicleta = Bicicleta(referencia, disenos)

            bicicleta.CrearBicicleta(nombrebici, numvelocidades, material,
            idbicicleta, tipobici, tamanobici, valor)

            num = 1

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")
            
            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Bicicleta/{nombre_archivo}.csv').empty == False:
                    
                    df_bicicleta = pd.read_csv(f'Datos/Archivos_Guardados/Bicicleta/{nombre_archivo}.csv')
                    
                    valores_archivosbicicleta = BuscarArchivosBicicleta(nombre_archivo)

                    referencia = valores_archivosbicicleta[0]
                    disenos = valores_archivosbicicleta[1]

                    nombrebici = str(df_bicicleta["|NombreBici|"][0])
                    numvelocidades = int(df_bicicleta["|NumVelocidades|"][0])
                    material = str(df_bicicleta["|Material|"][0])
                    idbicicleta = str(df_bicicleta["|ID|"][0])
                    tipobici = str(df_bicicleta["|TipoBici|"][0])
                    tamanobici = str(df_bicicleta["|TamanoBici|"][0])
                    valor = int(df_bicicleta["|Valor|"][0])

                    bicicleta = Bicicleta(referencia, disenos)

                    bicicleta.CrearBicicleta(nombrebici, numvelocidades, material,
                    idbicicleta, tipobici, tamanobici, valor)

            except FileNotFoundError:
                print("No se encontro el archivo")              

    return bicicleta, num           
