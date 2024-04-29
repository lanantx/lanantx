from hiena import hiena
from correcaminos import correcaminos
from tiburon import tiburon

class zoologico:
    def __init__(self):
        self.mianimal=[]

    def añadirAnimal(self, animalNuevo):
        self.mianimal.append(animalNuevo)

    def verAnimales(self):
        for animales in self.mianimal:
            print(animales)


adminzoo=zoologico()

while True:
    opcion = int(input("1. Agregar animal \n 2. Ver los animales \n 3. Salir \n "))
    if opcion == 1:
        animal = int(input("Agrega a tu animal de preferencia: \n 1. Hiena \n 2. Correcaminos \n 3. Tiburon \n" ))
        if animal == 1:
            nombre = input("Ingresa el nombre de la hiena: ")
            edad = input("Ingresa la edad del la hiena: ")
            peso = input("Ingresa el peso de la hiena: ")
            tamaño = input("Ingresa el tamaño de la hiena: ")
            sexo = input("Ingresa el sexo de la hiena: ")
            hienanueva=hiena(nombre,edad,peso,tamaño,sexo)
            adminzoo.añadirAnimal(hienanueva)
        elif animal == 2:
            nombre = input("Ingresa el nombre del correcaminos: ")
            edad = input("Ingresa la edad del correcaminos: ")
            peso = input("Ingresa el peso del correcaminos: ")
            tamaño = input("Ingresa el tamaño del correcaminos: ")
            sexo = input("Ingresa el sexo del correcaminos: ")
            correcaminosnuevo=correcaminos(nombre,edad,peso,tamaño,sexo)
            adminzoo.añadirAnimal(correcaminosnuevo)
        elif animal == 3:
            nombre = input("Ingresa el nombre del tiburon: ")
            edad = input("Ingresa la edad del tiburon: ")
            peso = input("Ingresa el peso del tiburon: ")
            tamaño = input("Ingresa el tamaño del tiburon: ")
            sexo = input("Ingresa el sexo del tiburon: ")
            tiburonnuevo=tiburon(nombre,edad,peso,tamaño,sexo)
            adminzoo.añadirAnimal(tiburonnuevo)

    elif opcion == 2:
        adminzoo.verAnimales()

    elif opcion == 3:
        break
