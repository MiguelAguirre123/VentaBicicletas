from Business.Bicicleta import Bicicleta
from Business.CuentaAhorro import CuentaAhorro
from Business.Detalle import Detalle
from Business.Diseno import Diseno
from Business.Efectivo import Efectivo
from Business.Persona import Persona
from Business.Referencia import Referencia
from Business.TarjetaCredito import TarjetaCredito
from Business.TarjetaDebito import TarjetaDebito
import pandas as pd

def BuscarArchivosFactura(nombre_archivo:str):

    detalles = []
    disenos = []

    df_factura = pd.read_csv(f'Datos/Archivos_Guardados/Factura/{nombre_archivo}.csv')

    shape1 = df_factura.shape
    num_detalles = int((shape1[1] - 14)/19)

    for contador_detalles in range(num_detalles):

        referencia = Referencia()

        referencia._NombreReferencia = str(df_factura[f"|Nombre Referencia||{contador_detalles+1}|"][0])

        nombre1 = df_factura[f"|NombreBici||{contador_detalles+1}|"][0]

        df_bicicleta = pd.read_csv(f'Datos/Archivos_Guardados/Bicicleta/{nombre1}.csv')

        shape2 = df_bicicleta.shape
        num_disenos = int((shape2[1] - 8)/3)

        for contador_disenos in range(num_disenos):

            diseno = Diseno()

            diseno._Color1 = str(df_factura[f"|Color 1||{contador_disenos+1}||{contador_detalles+1}|"][0])
            diseno._Color2 = str(df_factura[f"|Color 2||{contador_disenos+1}||{contador_detalles+1}|"][0])
            diseno._IdDiseno = str(df_factura[f"|ID Diseno||{contador_disenos+1}||{contador_detalles+1}|"][0])
            disenos.append(diseno)

        bicicleta = Bicicleta(referencia, disenos)

        bicicleta.NombreBici = str(df_factura[f"|NombreBici||{contador_detalles+1}|"][0])
        bicicleta.Referenciacion = referencia
        bicicleta.Disenos = disenos
        bicicleta.NumVelocidades = int(df_factura[f"|NumVelocidades||{contador_detalles+1}|"][0])
        bicicleta.Material = str(df_factura[f"|Material||{contador_detalles+1}|"][0])
        bicicleta.IdBicicleta = str(df_factura[f"|ID||{contador_detalles+1}|"][0])
        bicicleta.TipoBici = str(df_factura[f"|TipoBici||{contador_detalles+1}|"][0])
        bicicleta.TamanoBici = str(df_factura[f"|TamanoBici||{contador_detalles+1}|"][0])
        bicicleta.Valor = int(df_factura[f"|Valor||{contador_detalles+1}|"][0])

        detalle = Detalle(bicicleta)

        detalle._Producto = bicicleta
        detalle._CantidadProducto = int(df_factura[f"|CantidadProducto||{contador_detalles+1}|"][0])
        detalle._IdDetalle = str(df_factura[f"|ID Detalle||{contador_detalles+1}|"][0])
        detalles.append(detalle)

    persona = Persona()

    persona.Nombre = str(df_factura["|Nombre|"][0])
    persona.Apellido = str(df_factura["|Apellido|"][0])
    persona.IdPersona = str(df_factura["|ID Persona|"][0])
    persona.Telefono = int(df_factura["|Telefono|"][0])
    persona.Direccion = str(df_factura["|Direccion|"][0])

    nombre2 = str(df_factura[f"|NumOperacion|"][0])

    try:
        if pd.read_csv(f'Datos/Archivos_Guardados/Efectivo/{nombre2}.csv').empty == False:

            efectivo = Efectivo()

            efectivo._NumOperacion = str(df_factura["|NumOperacion|"][0])
            efectivo._FechaPago = df_factura["|FechaPago|"][0]
            efectivo._MonedaPago = str(df_factura["|MonedaPago|"][0])
            efectivo._CuentaBeneficiario = str(df_factura["|CuentaBeneficiario|"][0])
            efectivo._Monto = str(df_factura["|Monto|"][0])
            efectivo.ValorPagar = str(df_factura["|ValorPagar|"][0])

            metodo = efectivo
                
    except FileNotFoundError:    

        try:
            if pd.read_csv(f'Datos/Archivos_Guardados/CuentaAhorro/{nombre2}.csv').empty == False:


                cuentaahorro = CuentaAhorro()

                cuentaahorro._NumOperacion = str(df_factura["|NumOperacion|"][0])
                cuentaahorro._FechaPago = df_factura["|FechaPago|"][0]
                cuentaahorro._MonedaPago = str(df_factura["|MonedaPago|"][0])
                cuentaahorro._CuentaBeneficiario = str(df_factura["|CuentaBeneficiario|"][0])
                cuentaahorro._Monto = str(df_factura["|Monto|"][0])
                cuentaahorro.NumCuenta = str(df_factura["|NumCuenta|"][0])
                cuentaahorro.Contrasena = int(df_factura["|Contrasena|"][0])

                metodo = cuentaahorro

        except FileNotFoundError:

            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/TarjetaDebito/{nombre2}.csv').empty == False:

                    tarjetadebito = TarjetaDebito()

                    tarjetadebito._NumOperacion = str(df_factura["|NumOperacion|"][0])
                    tarjetadebito._FechaPago = df_factura["|FechaPago|"][0]
                    tarjetadebito._MonedaPago = str(df_factura["|MonedaPago|"][0])
                    tarjetadebito._CuentaBeneficiario = str(df_factura["|CuentaBeneficiario|"][0])
                    tarjetadebito._Monto = str(df_factura["|Monto|"][0])
                    tarjetadebito.NumTarjeta = str(df_factura["|NumTarjeta|"][0])
                    tarjetadebito.Contrasena = int(df_factura["|Contrasena|"][0])

                    metodo = tarjetadebito
                
            except FileNotFoundError:

                    try:
                        if pd.read_csv(f'Datos/Archivos_Guardados/TarjetaCredito/{nombre2}.csv').empty == False:

                            tarjetacredito = TarjetaCredito()

                            tarjetacredito._NumOperacion = str(df_factura["|NumOperacion|"][0])
                            tarjetacredito._FechaPago = df_factura["|FechaPago|"][0]
                            tarjetacredito._MonedaPago = str(df_factura["|MonedaPago|"][0])
                            tarjetacredito._CuentaBeneficiario = str(df_factura["|CuentaBeneficiario|"][0])
                            tarjetacredito._Monto = str(df_factura["|Monto|"][0])
                            tarjetacredito.NumTarjeta = str(df_factura["|NumTarjeta|"][0])
                            tarjetacredito.Contrasena = int(df_factura["|Contrasena|"][0])

                            metodo = tarjetacredito

                    except FileNotFoundError:

                        print("error")

    return detalles, persona, metodo