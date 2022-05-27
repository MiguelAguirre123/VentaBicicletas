from Business.Persona import Persona

class Empleado(Persona):

    _Sueldo:int
    _CorreoEmpresa:str
    _Login:str
    _Contrasena:str

    def CrearEmpleado(self, sueldo:int, correoempresa:str, login:str, contrasena:str):

        self._Sueldo = sueldo
        self._CorreoEmpresa = correoempresa
        self._Login = login
        self._Contrasena = contrasena