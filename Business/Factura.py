from Business.CuentaAhorro import CuentaAhorro
from Business.Detalle import Detalle
from Business.Efectivo import Efectivo
from Business.MetodoPago import MetodoPago
from Business.Persona import Persona
from Business.TarjetaCredito import TarjetaCredito
from Business.TarjetaDebito import TarjetaDebito
from Datos.CuentaAhorroArchivo import CuentaAhorroArchivo
from Datos.DetalleArchivo import DetalleArchivo
from Datos.EfectivoArchivo import EfectivoArchivo
from Datos.PersonaArchivo import PersonaArchivo
from Datos.TarjetaCreditoArchivo import TarjetaCreditoArchivo
from Datos.TarjetaDebitoArchivo import TarjetaDebitoArchivo
import pandas as pd

class Factura:

    _ValorTotal:int
    _CodigoFactura:str


    def __init__(self, detallesfactura:Detalle, datoscliente:Persona, metodopagar:MetodoPago):

        self._DetallesFactura = detallesfactura
        self._DatosCliente = datoscliente
        self._MetodoPagar = metodopagar

    def CrearFactura(self):

        factura = None

        while factura == None:

            print("¿Que Quiere Hacer?")
            print("1. Crear una Factura")
            print("2. Buscar una Factura existente")
            num = int(input("Introduzca un numero: "))

            if num == 1:

                detalles = []
                detalle_ID = []

                bicicleta = None

                while num != 0:

                    detalle = Detalle(bicicleta)

                    valores_detalle = detalle.CrearDetalle()
                    detalle = valores_detalle[0]

                    detalle_ID.append(detalle._IdDetalle)

                    if detalle_ID.count(detalle._IdDetalle) == 1:
                        detalles.append(detalle)

                        if valores_detalle[1] == 1:
                            print("Archivo creado con exito")
                        elif valores_detalle[1] == 2:
                            print("Archivo cargado con exito")

                    else:

                        contador_detalles:Detalle

                        for contador_detalles in detalles:

                            if contador_detalles._IdDetalle == detalle._IdDetalle:

                                detalles[detalles.index(contador_detalles)] = detalle

                                if valores_detalle[1] == 1:
                                    print("El archivo creado con el mismo nombre de directorio fue modificado")
                                elif valores_detalle[1] == 2:
                                    print("El archivo ya fue subido anteriormente")

                    detallearchivo = DetalleArchivo()
                    detallearchivo.GenerarTXT(detalle)

                    print("¿Que quiere hacer?")
                    print("0. Salir del gestor de Detalles de Factura")
                    print("Cualquier otro numero para seguir en el gestor de Detalles de Factura")
                    num = int(input("Introduzca un numero: "))

                persona = Persona()
    
                valores_persona = persona.CrearPersona()
                persona = valores_persona[0]

                if valores_persona[1] == 1:
                    print("Archivo creado con exito")
                elif valores_persona[1] == 2:
                    print("Archivo cargado con exito")

                personaarchivo = PersonaArchivo()
                personaarchivo.GenerarTXT(persona)

                metodo = None

                while metodo == None:

                    print("¿Con cual medio de pago se realizara la transaccion?")
                    print("1. Efectivo")
                    print("2. Cuenta de Ahorro")
                    print("3. Tarjeta de Debito") 
                    print("4. Tarjeta de Credito")
                    num = int(input("Introduzca un numero: "))

                    if num == 1:

                        efectivo = Efectivo()

                        valores_efectivo = efectivo.CrearEfectivo()

                        efectivo = valores_efectivo[0]

                        if valores_efectivo[1] == 1:
                            print("Archivo creado con exito")
                        elif valores_efectivo[1] == 2:
                            print("Archivo cargado con exito")

                        efectivoarchivo = EfectivoArchivo()
                        efectivoarchivo.GenerarTXT(efectivo)

                        metodo = efectivo

                    elif num == 2:

                        cuentaahorro = CuentaAhorro()

                        valores_cuentaahorro = cuentaahorro.CrearCuentaAhorro()

                        cuentaahorro = valores_cuentaahorro[0]

                        if valores_cuentaahorro[1] == 1:
                            print("Archivo creado con exito")
                        elif valores_cuentaahorro[1] == 2:
                            print("Archivo cargado con exito")

                        cuentaahorroarchivo = CuentaAhorroArchivo()
                        cuentaahorroarchivo.GenerarTXT(cuentaahorro)

                        metodo = cuentaahorro

                    elif num == 3:

                        tarjetadebito = TarjetaDebito()

                        valores_tarjetadebito = tarjetadebito.CrearTarjetaDebito()

                        tarjetadebito = valores_tarjetadebito[0]

                        if valores_tarjetadebito[1] == 1:
                            print("Archivo creado con exito")
                        elif valores_tarjetadebito[1] == 2:
                            print("Archivo cargado con exito")

                        tarjetadebitoarchivo = TarjetaDebitoArchivo()
                        tarjetadebitoarchivo.GenerarTXT(tarjetadebito)

                        metodo = tarjetadebito
                
                    elif num == 4:

                        tarjetacredito = TarjetaCredito()

                        valores_tarjetacredito = tarjetacredito.CrearTarjetaCredito()

                        tarjetacredito = valores_tarjetacredito[0]

                        if valores_tarjetacredito[1] == 1:
                            print("Archivo creado con exito")
                        elif valores_tarjetacredito[1] == 2:
                            print("Archivo cargado con exito")

                        tarjetacreditoarchivo = TarjetaCreditoArchivo()
                        tarjetacreditoarchivo.GenerarTXT(tarjetacredito)

                        metodo = tarjetacredito

                factura = Factura(detalles, persona, metodo)

                factura._DetallesFactura = detalles
                factura._DatosCliente = persona
                factura._ValorTotal = int(input("Introduzca el valor total de la factura: "))
                factura._CodigoFactura = input("Introduzca el codigo de la factura: ")
                factura._MetodoPagar = metodo

                num = 1

            elif num == 2:

                nombre_archivo = input("Introduzca el nombre del archivo: ")
                
                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/Factura/{nombre_archivo}.csv').empty == False:
                        
                        df_factura = pd.read_csv(f'Datos/Archivos_Guardados/Factura/{nombre_archivo}.csv')
                        
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

        return factura, num


