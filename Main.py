from Business.Bicicleta import Bicicleta
from Business.Diseno import Diseno
from Business.EnumMaterial import EnumMaterial
from Business.EnumTipoBici import EnumTipoBici
from Business.Persona import Persona
from Business.Referencia import Referencia
from Business.Sede import Sede
from Datos.BicicletaArchivo import BicicletaArchivo
from Datos.DisenoArchivo import DisenoArchivo
from Datos.PersonaArchivo import PersonaArchivo
from Datos.ReferenciaArchivo import ReferenciaArchivo
import pandas as pd

from Datos.SedeArchivo import SedeArchivo

num = 10000

while num != 0:

    print("¿Que Quiere Hacer?")
    print("0. Para salirse del programa")
    print("1. Para crear Bicicleta")
    print("2. Para crear Sede")

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
        
    elif num == 2:

        inventariosede = None
        empleados = None

        sede = Sede(inventariosede, empleados)

        valores_sede = sede.CrearSede()
        sede = valores_sede[0]

        if valores_sede[1] == 1:
            print("Archivo creado con exito")
        elif valores_sede[1] == 2:
            print("Archivo cargado con exito")

        sedearchivo = SedeArchivo()
        sedearchivo.GenerarTXT(sede)

               




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
