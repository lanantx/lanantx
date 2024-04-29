class Tiuron:
    def __init__(self, Nombre, Edad, Peso, Tamaño, Sexo):
        self.__Nombre=Nombre
        self.__Edad=Edad
        self.__Peso=Peso
        self.__Tamaño=Tamaño
        self.__Sexo=Sexo
    
    def __str__(self):
        return f"Tiburon: {self.__Nombre}, Edad: {self.__Edad}, Peso: {self.__Peso} kg, Tamaño: {self.__Tamaño} cm, Sexo: {self.__Sexo}\n"

    def nadar(self):
        print("Puede nadar a velocidades de hasta 25 kilómetros por hora en ráfagas cortas.")

    def dientes(sefl):
        print("Puede tener alrededor de 300-400 dientes en su boca")

    def mordida(self):
        print("Su fuerza de mordida puede alcanzar hasta aproximadamente 1.8 toneladas por centímetro cuadrado ")

    def tamaño(self):
        print("Generalmente tienen una longitud que oscila entre los 4 y los 6 metros, aunque pueden llegar a superar los 7 metros en casos excepcionales. ")

    def dieta(self):
        print("Son carnívoros y se alimentan principalmente de peces, calamares, crustáceos y otros animales marinos.")
    

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
