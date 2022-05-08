        
def CrearBicicleta(num):

    disenos == 0

    while disenos == 0:

        print("¿Que Quiere Hacer?")
        print("1. Crear un diseno: ")
        print("2. Buscar un diseno existente: ")
        num = int(input("Introduzca un numero: "))

        if num == 1:
                
            diseno = Diseno()

            diseno._Color1 = input("Introduzca un primer color en hexadecimal: ")
            diseno._Color2 = input("Introduzca un segundo color en hexadecimal: ")
            diseno._Id = input("Introduzca la identificacion del diseno: ")

            disenos.append(diseno._Id)

            disenoarchivo = DisenoArchivo()
            disenoarchivo.GenerarTXT(diseno._Color1, diseno._Color2, diseno._Id)   