from Business.Detalle import Detalle
from Business.Factura import Factura
import pandas as pd

class FacturaArchivo:
    
    def GenerarTXT(self, factura:Factura):

        datos_factura = {"|CodigoFactura|":factura._CodigoFactura, "|ValorTotal|":factura._ValorTotal}

        nombre_archivo = f'Datos/Archivos_Guardados/Factura/{factura._CodigoFactura}.csv'
        df = pd.DataFrame(data=datos_factura,index=[0])

        try:
            if pd.read_csv(f'Datos/Archivos_Guardados/Efectivo/{factura._MetodoPagar._NumOperacion}.csv').empty == False:

                df_efectivo = pd.read_csv(f'Datos/Archivos_Guardados/Efectivo/{factura._MetodoPagar._NumOperacion}.csv')
                df = pd.merge(df_efectivo, df, right_index=True, left_index=True, how='outer')
                
        except FileNotFoundError:    

            try:
                if pd.read_csv(f'Datos/Archivos_Guardados/CuentaAhorro/{factura._MetodoPagar._NumOperacion}.csv').empty == False:

                    df_cuentaahorro = pd.read_csv(f'Datos/Archivos_Guardados/CuentaAhorro/{factura._MetodoPagar._NumOperacion}.csv')
                    df = pd.merge(df_cuentaahorro, df, right_index=True, left_index=True, how='outer')

            except FileNotFoundError:

                try:
                    if pd.read_csv(f'Datos/Archivos_Guardados/TarjetaDebito/{factura._MetodoPagar._NumOperacion}.csv').empty == False:

                        df_tarjetadebito = pd.read_csv(f'Datos/Archivos_Guardados/TarjetaDebito/{factura._MetodoPagar._NumOperacion}.csv')
                        df = pd.merge(df_tarjetadebito, df, right_index=True, left_index=True, how='outer')
                
                except FileNotFoundError:

                        try:
                            if pd.read_csv(f'Datos/Archivos_Guardados/TarjetaCredito/{factura._MetodoPagar._NumOperacion}.csv').empty == False:

                                df_tarjetacredito = pd.read_csv(f'Datos/Archivos_Guardados/TarjetaCredito/{factura._MetodoPagar._NumOperacion}.csv')
                                df = pd.merge(df_tarjetacredito, df, right_index=True, left_index=True, how='outer')

                        except FileNotFoundError:
                            pass

        contador_detalle:Detalle

        df_persona = pd.read_csv(f'Datos/Archivos_Guardados/Persona/{factura._DatosCliente.IdPersona}.csv')
        df = pd.merge(df_persona, df, right_index=True, left_index=True, how='outer')
        
        for contador_detalle in factura._DetallesFactura:

            df_detalle = pd.read_csv(f'Datos/Archivos_Guardados/Detalle/{contador_detalle._IdDetalle}.csv')
            df_detalle = df_detalle.add_suffix(f'|{factura._DetallesFactura.index(contador_detalle)+1}|')
            df = pd.merge(df_detalle, df, right_index=True, left_index=True, how='outer')

        print(df)
        df.to_csv(nombre_archivo, index=False) 