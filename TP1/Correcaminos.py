class Correcaminos:
    def __init__(self, Nombre, Edad, Peso, Tamaño, Sexo):
        self.__Nombre=Nombre
        self.__Edad=Edad
        self.__Peso=Peso
        self.__Tamaño=Tamaño
        self.__Sexo=Sexo
    
    def __str__(self):
        return f"Correcaminos: {self.__Nombre}, Edad: {self.__Edad}, Peso: {self.__Peso} kg, Tamaño: {self.__Tamaño} cm, Sexo: {self.__Sexo}\n"

    def correr(self):
        print(" Pueden correr a velocidades de hasta 32 a 40 kilómetros por hora, lo que les permite capturar presas y escapar de los depredadores con facilidad.")

    def familia(sefl):
        print("Son aves terrestres pertenecientes a la familia Cuculidae")

    def vuelo(self):
        print("Pueden volar cuando es necesario, generalmente prefieren correr como su principal método de locomoción.")

    def longitud(self):
        print("Generalmente tienen una longitud de alrededor de 50 a 60 centímetros")
    
    def plumaje(self):
        print("Es generalmente de color marrón o grisáceo, con barras negras y manchas blancas en la parte inferior")

    @property
    def nombre(self):
        return self.__Nombre
    @nombre.setter
    def nombre(self,valor):
        self.__Nombre=valor
    
    @property
    def edad(self):
        return self.__Edad
    @edad.setter
    def edad(self, valor):
        self.__Edad=valor

    @property
    def peso(self):
        return self.__Peso
    @peso.setter
    def peso(self,valor):
        self.__Peso=valor

    @property
    def tamaño(self):
        return self.__Tamaño
    @tamaño.setter
    def tamaño(self,valor):
        self.__Tamaño=valor

    @property
    def sexo(self):
        return self._Sexo
    @sexo.setter
    def sexo(self,valor):
        self._Sexo=valor
