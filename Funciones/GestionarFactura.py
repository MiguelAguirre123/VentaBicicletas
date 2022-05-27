from Business.Detalle import Detalle
from Business.Factura import Factura
from Datos.CuentaAhorroArchivo import CuentaAhorroArchivo
from Datos.DetalleArchivo import DetalleArchivo
from Datos.EfectivoArchivo import EfectivoArchivo
from Datos.PersonaArchivo import PersonaArchivo
from Datos.TarjetaCreditoArchivo import TarjetaCreditoArchivo
from Datos.TarjetaDebitoArchivo import TarjetaDebitoArchivo
from Funciones.BuscarArchivosFactura import BuscarArchivosFactura
from Funciones.GestionarCuentaAhorro import GestionarCuentaAhorro
from Funciones.GestionarDetalle import GestionarDetalle
from Funciones.GestionarEfectivo import GestionarEfectivo
from Funciones.GestionarPersona import GestionarPersona
from Funciones.GestionarTarjetaCredito import GestionarTarjetaCredito
from Funciones.GestionarTarjetaDebito import GestionarTarjetaDebito
import pandas as pd

def GestionarFactura():

    factura = None

    while factura == None:

        print("¿Que Quiere Hacer?")
        print("1. Crear una Factura")
        print("2. Buscar una Factura existente")
        num = int(input("Introduzca un numero: "))

        if num == 1:

            detalles = []
            detalle_ID = []

            while num != 0:

                valores_detalle = GestionarDetalle()
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

            valores_persona = GestionarPersona()
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

                    valores_efectivo = GestionarEfectivo()
                    efectivo = valores_efectivo[0]

                    if valores_efectivo[1] == 1:
                        print("Archivo creado con exito")
                    elif valores_efectivo[1] == 2:
                        print("Archivo cargado con exito")

                    efectivoarchivo = EfectivoArchivo()
                    efectivoarchivo.GenerarTXT(efectivo)

                    metodo = efectivo

                elif num == 2:

                    valores_cuentaahorro = GestionarCuentaAhorro()
                    cuentaahorro = valores_cuentaahorro[0]

                    if valores_cuentaahorro[1] == 1:
                        print("Archivo creado con exito")
                    elif valores_cuentaahorro[1] == 2:
                        print("Archivo cargado con exito")

                    cuentaahorroarchivo = CuentaAhorroArchivo()
                    cuentaahorroarchivo.GenerarTXT(cuentaahorro)

                    metodo = cuentaahorro

                elif num == 3:

                    valores_tarjetadebito = GestionarTarjetaDebito()
                    tarjetadebito = valores_tarjetadebito[0]

                    if valores_tarjetadebito[1] == 1:
                        print("Archivo creado con exito")
                    elif valores_tarjetadebito[1] == 2:
                        print("Archivo cargado con exito")

                    tarjetadebitoarchivo = TarjetaDebitoArchivo()
                    tarjetadebitoarchivo.GenerarTXT(tarjetadebito)

                    metodo = tarjetadebito
            
                elif num == 4:

                    valores_tarjetacredito = GestionarTarjetaCredito()
                    tarjetacredito = valores_tarjetacredito[0]

                    if valores_tarjetacredito[1] == 1:
                        print("Archivo creado con exito")
                    elif valores_tarjetacredito[1] == 2:
                        print("Archivo cargado con exito")

                    tarjetacreditoarchivo = TarjetaCreditoArchivo()
                    tarjetacreditoarchivo.GenerarTXT(tarjetacredito)

                    metodo = tarjetacredito

            valortotal = int(input("Introduzca el valor total de la factura: "))
            codigofactura = input("Introduzca el codigo de la factura: ")

            factura = Factura(detalles, persona, metodo)

            factura.CrearFactura(valortotal, codigofactura)

            num = 1

        elif num == 2:

            nombre_archivo = input("Introduzca el nombre del archivo: ")
            
            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/Factura/{nombre_archivo}.csv').empty == False:
                    
                    df_factura = pd.read_csv(f'Datos/Archivos_Guardados/Factura/{nombre_archivo}.csv')
                    
                    valores_archivosfactura = BuscarArchivosFactura(nombre_archivo)

                    detalles = valores_archivosfactura[0]
                    persona = valores_archivosfactura[1]
                    metodo = valores_archivosfactura[2]

                    valortotal = int(df_factura["|ValorTotal|"][0])
                    codigofactura = str(df_factura["|CodigoFactura|"][0])

                    factura = Factura(detalles, persona, metodo)

                    factura.CrearFactura(valortotal, codigofactura)

            except FileNotFoundError:
                print("No se encontro el archivo")

    return factura, num