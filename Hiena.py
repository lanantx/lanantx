class Hiena:
    def __init__(self, Nombre, Edad, Peso, Tamaño, Sexo):
        self.__Nombre=Nombre
        self.__Edad=Edad
        self.__Peso=Peso
        self.__Tamaño=Tamaño
        self.__Sexo=Sexo
    
    def __str__(self):
        return f"Hiena: {self.__Nombre}, Edad: {self.__Edad}, Peso: {self.__Peso} kg, Tamaño: {self.__Tamaño} cm, Sexo: {self.__Sexo}\n"

    def correr(self):
        print("las hienas pueden correr a una velocidad máxima de alrededor de 50 kilómetros por hora en ráfagas cortas")

    def mordida(sefl):
        print( "Se ha estimado que las hienas pueden ejercer una fuerza de mordida de alrededor de 800 psi (libras por pulgada cuadrada), lo que les permite romper huesos y desgarrar la carne con facilidad")

    def peso(self):
        print("pueden pesar alrededor de 40 a 90 kilogramos")
    
    def sonido(self):
        print("las hienas son conocidas por sus vocalizaciones variadas; emiten una amplia gama de sonidos que incluyen gruñidos, ladridos, risas y gemidos")

    def vista(self):
        print("las hienas tienen una visión nocturna bastante buena, lo que les permite cazar y moverse durante la noche")

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


        