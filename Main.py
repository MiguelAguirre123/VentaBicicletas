from Business.Bicicleta import Bicicleta
from Business.Diseno import Diseno
from Business.EnumMaterial import EnumMaterial
from Business.EnumTipoBici import EnumTipoBici
from Business.Persona import Persona
from Business.Referencia import Referencia
from Datos.BicicletaArchivo import BicicletaArchivo
from Datos.DisenoArchivo import DisenoArchivo
from Datos.PersonaArchivo import PersonaArchivo
from Datos.ReferenciaArchivo import ReferenciaArchivo
import pandas as pd

num = 10000

while num != 0:

    print("¿Que Quiere Hacer?")
    print("0. Para salirse del programa")
    print("1. Para crear Bicicleta")
    print("2. Para crear Sede")

    num = int(input("Introduzca un numero: "))

    if num == 1:

        disenos = []
        
        while num != 0:

            print("¿Que Quiere Hacer?")
            print("0. Salir de gestor de Diseno: ")
            print("1. Crear un diseno: ")
            print("2. Buscar un diseno existente: ")
            num = int(input("Introduzca un numero: "))

            if num == 1:
                
                diseno = Diseno()

                diseno.__Color1 = input("Introduzca un primer color en hexadecimal: ")
                diseno.__Color2 = input("Introduzca un segundo color en hexadecimal: ")
                diseno.__Id = input("Introduzca la identificacion del diseno: ")

                disenos.append(diseno.__Id)

                disenoarchivo = DisenoArchivo()
                disenoarchivo.GenerarTXT(diseno.__Color1, diseno.__Color2, diseno.__Id)   

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")

                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/Diseno/{nombre_archivo}.csv').empty == False:

                        if disenos.count(nombre_archivo) == 0:

                            disenos.append(nombre_archivo)
                            print("Archivo cargado con exito")

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

                referencia.__NombreReferencia = input("Introduzca el nombre de la referencia: ")

                referenciaarchivo = ReferenciaArchivo()
                referenciaarchivo.GenerarTXT(referencia.__NombreReferencia)     

                referencia_guardada = referencia.__NombreReferencia

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")

                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{nombre_archivo}.csv').empty == False:

                        referencia_guardada = referencia.__NombreReferencia

                except FileNotFoundError:
                    print("No se encontro el archivo")

        bicicleta = Bicicleta(referencia_guardada, disenos)

        bicicleta.NombreBici = input("Introduzca el nombre de la bicicleta: ")
        bicicleta.Relacion = referencia_guardada
        bicicleta.Disenos = disenos
        bicicleta.NumVelocidades = input("Introduzca las velocidades de la bicicleta: ")
        bicicleta.Material = EnumMaterial(int(input("Introduzca el numero de material: "))).name
        bicicleta.Identificacion = input("Introduzca el ID de la bicicleta: ")
        bicicleta.TipoBici = EnumTipoBici(int(input("Introduzca el numero del tipo de bicicleta: "))).name
        bicicleta.TamanoBici = input("Introduzca el tamano de la bicicleta: ")
        bicicleta.Valor = input("Introduzca el valor comercial de la bicicleta: ")

        bicicletaarchivo = BicicletaArchivo()
        bicicletaarchivo.GenerarTXT(bicicleta.NombreBici, bicicleta.NumVelocidades,
        bicicleta.Material, bicicleta.Identificacion, bicicleta.TipoBici,
        bicicleta.TamanoBici, bicicleta.Valor, bicicleta.Relacion, disenos)
        
    elif num == 2:

        disenos == 0

        while disenos == 0:

            print("¿Que Quiere Hacer?")
            print("1. Crear un diseno: ")
            print("2. Buscar un diseno existente: ")
            num = int(input("Introduzca un numero: "))

            if num == 1:
                
                diseno = Diseno()

                diseno.__Color1 = input("Introduzca un primer color en hexadecimal: ")
                diseno.__Color2 = input("Introduzca un segundo color en hexadecimal: ")
                diseno.__Id = input("Introduzca la identificacion del diseno: ")

                disenos.append(diseno.__Id)

                disenoarchivo = DisenoArchivo()
                disenoarchivo.GenerarTXT(diseno.__Color1, diseno.__Color2, diseno.__Id)   

               




#persona = Persona()

#persona.Nombre = input()
#persona.Apellido = input()
#persona.Id = input()
#persona.Telefono = list(map(int, input().rstrip().split()))
#persona.Direccion = input()

#personaarchivo = PersonaArchivo()
#personaarchivo.GenerarTXT(persona.Nombre, persona.Apellido, persona.Id, persona.Telefono, persona.Direccion)

#disenos = []

#for i in range(3):
    #diseno = Diseno()

    #diseno.__Color1 = input()
    #diseno.__Color2 = input()
    #diseno.__Id = input()

    #disenos.append(diseno.__Id)

    #disenoarchivo = DisenoArchivo()
    #disenoarchivo.GenerarTXT(diseno.__Color1, diseno.__Color2, diseno.__Id)

#print(disenos)

#referencia = Referencia()

#referencia.__NombreReferencia = input()

#referenciaarchivo = ReferenciaArchivo()
#referenciaarchivo.GenerarTXT(referencia.__NombreReferencia)
#df_referencia = pd.read_csv(f'Datos/Archivos_Guardados/Referencia/{referencia.__NombreReferencia}.csv')

#referencia_guardada = referencia.__NombreReferencia

#bicicleta = Bicicleta(referencia_guardada, disenos)

#bicicleta.NombreBici = input()
#bicicleta.Relacion = referencia_guardada
#bicicleta.Disenos = disenos
#bicicleta.NumVelocidades = input()
#bicicleta.Material = EnumMaterial(int(input())).name
#bicicleta.Identificacion = input()
#bicicleta.TipoBici = EnumTipoBici(int(input())).name
#bicicleta.TamanoBici = input()
#bicicleta.Valor = input()

#bicicletaarchivo = BicicletaArchivo()
#bicicletaarchivo.GenerarTXT(bicicleta.NombreBici, bicicleta.NumVelocidades,
#bicicleta.Material, bicicleta.Identificacion, bicicleta.TipoBici,
#bicicleta.TamanoBici, bicicleta.Valor, bicicleta.Relacion, disenos)

#df_refer= pd.read_csv(f'Datos/Archivos_Guardados/Bicicleta/{bicicleta.NombreBici}.csv')
#print(df_refer)

#df = pd.read_csv('Persona.csv') 
#print(df["Nombre"][0])
