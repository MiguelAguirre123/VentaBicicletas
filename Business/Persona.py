class Persona:

    Nombre:str
    Apellido:str
    IdPersona:str
    Telefono:int
    Direccion:str

    def CrearPersona(self, nombre:str, apellido:str, idpersona:str, telefono:int, direccion:str):

        self.Nombre = nombre
        self.Apellido = apellido
        self.IdPersona = idpersona
        self.Telefono = telefono
        self.Direccion = direccion