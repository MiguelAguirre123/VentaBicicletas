from Business.Bicicleta import Bicicleta
from Business.CuentaAhorro import CuentaAhorro
from Business.Detalle import Detalle
from Business.Diseno import Diseno
from Business.Efectivo import Efectivo
from Business.Empleado import Empleado
from Business.Factura import Factura
from Business.InventarioReferencia import InventarioReferencia
from Business.Persona import Persona
from Business.Referencia import Referencia
from Business.Sede import Sede
from Business.TarjetaCredito import TarjetaCredito
from Business.TarjetaDebito import TarjetaDebito
from Datos.BicicletaArchivo import BicicletaArchivo
from Datos.CuentaAhorroArchivo import CuentaAhorroArchivo
from Datos.DetalleArchivo import DetalleArchivo
from Datos.EfectivoArchivo import EfectivoArchivo
from Datos.EmpleadoArchivo import EmpleadoArchivo
from Datos.FacturaArchivo import FacturaArchivo
from Datos.DisenoArchivo import DisenoArchivo
from Datos.InventarioReferenciaArchivo import InventarioReferenciaArchivo
from Datos.PersonaArchivo import PersonaArchivo
from Datos.ReferenciaArchivo import ReferenciaArchivo
from Datos.SedeArchivo import SedeArchivo
from Datos.TarjetaCreditoArchivo import TarjetaCreditoArchivo
from Datos.TarjetaDebitoArchivo import TarjetaDebitoArchivo

num = 10000

while num != 0:

    print("¿Que Quiere Hacer?")
    print("0. Para salirse del programa")
    print("1. Para crear Bicicleta")
    print("2. Para crear Sede")
    print("3. Para crear Factura")
    print("4. Para crear Diseno")
    print("5. Para crear Referencia")
    print("6. Para crear Inventario")
    print("7. Para crear MetodoPago")
    print("8. Para crear Detalle")
    print("9. Para crear Empleado")
    print("10. Para crear Persona")
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

    elif num == 3:

        detalle = None
        persona = None
        metodopago = None

        factura = Factura(detalle, persona, metodopago)

        valores_factura = factura.CrearFactura()
        factura = valores_factura[0]

        if valores_factura[1] == 1:
            print("Archivo creado con exito")
        elif valores_factura[1] == 2:
            print("Archivo cargado con exito")

        facturaarchivo = FacturaArchivo()
        facturaarchivo.GenerarTXT(factura)

    elif num == 4:

        diseno = Diseno()

        valores_diseno = diseno.CrearDiseno()
        diseno = valores_diseno[0]

        if valores_diseno[1] == 1:
            print("Archivo creado con exito")
        elif valores_diseno[1] == 2:
            print("Archivo cargado con exito")

        disenoarchivo = DisenoArchivo()
        disenoarchivo.GenerarTXT(diseno)

    elif num == 5:

        referencia = Referencia()

        valores_referencia = referencia.CrearReferencia()
        referencia = valores_referencia[0]

        if valores_referencia[1] == 1:
            print("Archivo creado con exito")
        elif valores_referencia[1] == 2:
            print("Archivo cargado con exito")

        referenciaarchivo = ReferenciaArchivo()
        referenciaarchivo.GenerarTXT(referencia)

    elif num == 6:

        inventarioreferencia = InventarioReferencia()

        valores_inventarioreferencia = inventarioreferencia.CrearInventarioReferencia()
        referencia = valores_inventarioreferencia[0]

        if valores_inventarioreferencia[1] == 1:
            print("Archivo creado con exito")
        elif valores_inventarioreferencia[1] == 2:
            print("Archivo cargado con exito")

        inventarioreferenciaarchivo = InventarioReferenciaArchivo()
        inventarioreferenciaarchivo.GenerarTXT(inventarioreferencia)

    elif num == 7:

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

    elif num == 8:

        detalle = Detalle()

        valores_detalle = detalle.CrearDetalle()
        detalle = valores_detalle[0]

        if valores_detalle[1] == 1:
            print("Archivo creado con exito")
        elif valores_detalle[1] == 2:
            print("Archivo cargado con exito")

        detallearchivo = DetalleArchivo()
        detallearchivo.GenerarTXT(detalle)

    elif num == 9:

        empleado = Empleado()

        valores_empleado = empleado.CrearEmpleado()
        empleado = valores_empleado[0]

        if valores_empleado[1] == 1:
            print("Archivo creado con exito")
        elif valores_empleado[1] == 2:
            print("Archivo cargado con exito")

        empleadoarchivo = EmpleadoArchivo()
        empleadoarchivo.GenerarTXT(empleado)

    elif num == 10:

        persona = Persona()

        valores_persona = persona.CrearPersona()
        persona = valores_persona[0]

        if valores_persona[1] == 1:
            print("Archivo creado con exito")
        elif valores_persona[1] == 2:
            print("Archivo cargado con exito")

        personaarchivo = PersonaArchivo()
        personaarchivo.GenerarTXT(persona)