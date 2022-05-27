from re import M
from Business.Diseno import Diseno
from Business.EnumMaterial import EnumMaterial
from Business.EnumTipoBici import EnumTipoBici
from Business.Referencia import Referencia

class Bicicleta:

    NombreBici:str
    NumVelocidades:int
    Material:EnumMaterial
    IdBicicleta:str
    TipoBici:EnumTipoBici
    TamanoBici:str
    Valor:int

    def __init__(self, referencia:Referencia, disenos:Diseno):

        self.Referenciacion = referencia
        self.Disenos = disenos

    def CrearBicicleta(self, nombrebici:str, numvelocidades:int, material:EnumMaterial,
    idbicicleta:str, tipobici:EnumTipoBici, tamanobici:str, valor:int):

        self.NombreBici = nombrebici
        self.NumVelocidades = numvelocidades
        self.Material = material
        self.IdBicicleta = idbicicleta
        self.TipoBici = tipobici
        self.TamanoBici = tamanobici
        self.Valor = valor