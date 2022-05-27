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
    num_detalles = 0
    num_disenos = 0

    df_factura = pd.read_csv(f'Datos/Archivos_Guardados/Factura/{nombre_archivo}.csv')

    try:
        while num_detalles > -1:
            str(df_factura[f"|ID Detalle||{num_detalles+1}|"][0])
            num_detalles += 1
    except KeyError:
        pass

    for contador_detalles in range(num_detalles):

        nombrereferencia = str(df_factura[f"|Nombre Referencia||{contador_detalles+1}|"][0])

        referencia = Referencia()

        referencia.CrearReferencia(nombrereferencia)

        try:
            while num_disenos > -1:
                str(df_factura[f"|ID Diseno||{num_disenos+1}||{contador_detalles+1}|"][0])
                num_disenos += 1
        except KeyError:
            pass

        for contador_disenos in range(num_disenos):

            color1 = str(df_factura[f"|Color 1||{contador_disenos+1}||{contador_detalles+1}|"][0])
            color2 = str(df_factura[f"|Color 2||{contador_disenos+1}||{contador_detalles+1}|"][0])
            iddiseno = str(df_factura[f"|ID Diseno||{contador_disenos+1}||{contador_detalles+1}|"][0])

            diseno = Diseno()

            diseno.CrearDiseno(color1, color2, iddiseno)

            disenos.append(diseno)

        nombrebici = str(df_factura[f"|NombreBici||{contador_detalles+1}|"][0])
        numvelocidades = int(df_factura[f"|NumVelocidades||{contador_detalles+1}|"][0])
        material = str(df_factura[f"|Material||{contador_detalles+1}|"][0])
        idbicicleta = str(df_factura[f"|ID||{contador_detalles+1}|"][0])
        tipobici = str(df_factura[f"|TipoBici||{contador_detalles+1}|"][0])
        tamanobici = str(df_factura[f"|TamanoBici||{contador_detalles+1}|"][0])
        valor = int(df_factura[f"|Valor||{contador_detalles+1}|"][0])

        bicicleta = Bicicleta(referencia, disenos)

        bicicleta.CrearBicicleta(nombrebici, numvelocidades, material,
        idbicicleta, tipobici, tamanobici, valor)  

        cantidadproducto = int(df_factura[f"|CantidadProducto||{contador_detalles+1}|"][0])
        iddetalle = str(df_factura[f"|ID Detalle||{contador_detalles+1}|"][0])

        detalle = Detalle(bicicleta)

        detalle.CrearDetalle(cantidadproducto, iddetalle)

        detalles.append(detalle)

    nombre = str(df_factura["|Nombre|"][0])
    apellido = str(df_factura["|Apellido|"][0])
    idpersona = str(df_factura["|ID Persona|"][0])
    telefono = int(df_factura["|Telefono|"][0])
    direccion = str(df_factura["|Direccion|"][0])

    persona = Persona()

    persona.CrearPersona(nombre, apellido, idpersona, telefono, direccion)    

    nombre2 = str(df_factura[f"|NumOperacion|"][0])

    try:
        if pd.read_csv(f'Datos/Archivos_Guardados/Efectivo/{nombre2}.csv').empty == False:

            numoperacion = str(df_factura["|NumOperacion|"][0])
            fechapago = df_factura["|FechaPago|"][0]
            monedapago = str(df_factura["|MonedaPago|"][0])
            cuentabeneficiario = str(df_factura["|CuentaBeneficiario|"][0])
            monto = str(df_factura["|Monto|"][0])
            valorpagar = str(df_factura["|ValorPagar|"][0])

            efectivo = Efectivo()

            efectivo.CrearMetodoPago(numoperacion, fechapago, monedapago,
            cuentabeneficiario, monto)
            efectivo.CrearPago(valorpagar) 

            metodo = efectivo
                
    except FileNotFoundError:    

        try:
            if pd.read_csv(f'Datos/Archivos_Guardados/CuentaAhorro/{nombre2}.csv').empty == False:


                cuentaahorro = CuentaAhorro()

                numoperacion = str(df_factura["|NumOperacion|"][0])
                fechapago = df_factura["|FechaPago|"][0]
                monedapago = str(df_factura["|MonedaPago|"][0])
                cuentabeneficiario = str(df_factura["|CuentaBeneficiario|"][0])
                monto = str(df_factura["|Monto|"][0])
                numcuenta = str(df_factura["|NumCuenta|"][0])
                contrasena = int(df_factura["|Contrasena|"][0])

                cuentaahorro = CuentaAhorro()

                cuentaahorro.CrearMetodoPago(numoperacion, fechapago, monedapago,
                cuentabeneficiario, monto)
                cuentaahorro.CrearPago(numcuenta, contrasena)

                metodo = cuentaahorro

        except FileNotFoundError:

            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/TarjetaDebito/{nombre2}.csv').empty == False:

                    tarjetadebito = TarjetaDebito()

                    numoperacion = str(df_factura["|NumOperacion|"][0])
                    fechapago = df_factura["|FechaPago|"][0]
                    monedapago = str(df_factura["|MonedaPago|"][0])
                    cuentabeneficiario = str(df_factura["|CuentaBeneficiario|"][0])
                    monto = str(df_factura["|Monto|"][0])
                    numtarjeta = str(df_factura["|NumTarjeta|"][0])
                    contrasena = int(df_factura["|Contrasena|"][0])

                    tarjetadebito = TarjetaDebito()

                    tarjetadebito.CrearMetodoPago(numoperacion, fechapago, monedapago,
                    cuentabeneficiario, monto)
                    tarjetadebito.CrearPago(numtarjeta, contrasena)

                    metodo = tarjetadebito
                
            except FileNotFoundError:

                    try:
                        if pd.read_csv(f'Datos/Archivos_Guardados/TarjetaCredito/{nombre2}.csv').empty == False:

                            tarjetacredito = TarjetaCredito()

                            numoperacion = str(df_factura["|NumOperacion|"][0])
                            fechapago = df_factura["|FechaPago|"][0]
                            monedapago = str(df_factura["|MonedaPago|"][0])
                            cuentabeneficiario = str(df_factura["|CuentaBeneficiario|"][0])
                            monto = str(df_factura["|Monto|"][0])
                            numtarjeta = str(df_factura["|NumTarjeta|"][0])
                            contrasena = int(df_factura["|Contrasena|"][0])

                            tarjetacredito = TarjetaCredito()

                            tarjetacredito.CrearMetodoPago(numoperacion, fechapago, monedapago,
                            cuentabeneficiario, monto)
                            tarjetacredito.CrearPago(numtarjeta, contrasena)   

                            metodo = tarjetacredito

                    except FileNotFoundError:
                        pass

    return detalles, persona, metodo