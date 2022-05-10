<<<<<<< HEAD
from Business.Diseno import Diseno
from Business.EnumMaterial import EnumMaterial
from Business.EnumTipoBici import EnumTipoBici
from Business.Referencia import Referencia
from Datos.DisenoArchivo import DisenoArchivo
from Datos.ReferenciaArchivo import ReferenciaArchivo
from Funciones.BuscarArchivosBicicleta import BuscarArchivosBicicleta
import pandas as pd
=======
from Business.Referencia import Referencia
from Business.Diseno import Diseno
from Business.EnumMaterial import EnumMaterial
from Business.EnumTipoBici import EnumTipoBici
>>>>>>> 66bd4a2f57680edb34ac7e8af71d54b60e88daac

class Bicicleta:

    NombreBici:str
    NumVelocidades:int
    Material:EnumMaterial
    IdBicicleta:str
    TipoBici:EnumTipoBici
    TamanoBici:str
    Valor:int

    def __init__(self, referencia:Referencia, disenos:Diseno):

        self.Referenciacion = referencia
<<<<<<< HEAD
        self.Disenos = disenos

    def CrearBicicleta(self):

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

                    diseno = Diseno()

                    valores_diseno = diseno.CrearDiseno()
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

                referencia = Referencia()
    
                valores_referencia = referencia.CrearReferencia()
                referencia = valores_referencia[0]

                if valores_referencia[1] == 1:
                    print("Archivo creado con exito")
                elif valores_referencia[1] == 2:
                    print("Archivo cargado con exito")

                referenciaarchivo = ReferenciaArchivo()
                referenciaarchivo.GenerarTXT(referencia)

                bicicleta = Bicicleta(referencia, disenos)

                bicicleta.NombreBici = input("Introduzca el nombre de la bicicleta: ")
                bicicleta.Referenciacion = referencia
                bicicleta.Disenos = disenos
                bicicleta.NumVelocidades = int(input("Introduzca las velocidades de la bicicleta: "))
                bicicleta.Material = EnumMaterial(int(input("Introduzca el numero de material: "))).name
                bicicleta.IdBicicleta = input("Introduzca el ID de la bicicleta: ")
                bicicleta.TipoBici = EnumTipoBici(int(input("Introduzca el numero del tipo de bicicleta: "))).name
                bicicleta.TamanoBici = input("Introduzca el tamano de la bicicleta: ")
                bicicleta.Valor = int(input("Introduzca el valor comercial de la bicicleta: "))

                num = 1

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")
                
                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/Bicicleta/{nombre_archivo}.csv').empty == False:
                        
                        df_bicicleta = pd.read_csv(f'Datos/Archivos_Guardados/Bicicleta/{nombre_archivo}.csv')
                        
                        valores_archivosbicicleta = BuscarArchivosBicicleta(nombre_archivo)

                        referencia = valores_archivosbicicleta[0]
                        disenos = valores_archivosbicicleta[1]

                        bicicleta = Bicicleta(referencia, disenos)

                        bicicleta.NombreBici = str(df_bicicleta["|NombreBici|"][0])
                        bicicleta.Referenciacion = referencia
                        bicicleta.Disenos = disenos
                        bicicleta.NumVelocidades = int(df_bicicleta["|NumVelocidades|"][0])
                        bicicleta.Material = str(df_bicicleta["|Material|"][0])
                        bicicleta.IdBicicleta = str(df_bicicleta["|ID|"][0])
                        bicicleta.TipoBici = str(df_bicicleta["|TipoBici|"][0])
                        bicicleta.TamanoBici = str(df_bicicleta["|TamanoBici|"][0])
                        bicicleta.Valor = int(df_bicicleta["|Valor|"][0])

                except FileNotFoundError:
                    print("No se encontro el archivo")              

        return bicicleta, num           
=======
        self.Disenos = disenos
>>>>>>> 66bd4a2f57680edb34ac7e8af71d54b60e88daac
