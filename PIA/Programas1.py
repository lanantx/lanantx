class Paciente:
    def __init__(self):
        self.tipo_enfermedad = int(input("Ingrese el tipo de enfermedad (1-4): "))
        self.edad = int(input("Ingrese la edad del paciente: "))
        self.dias_hospitalizado = int(input("Ingrese el número de días hospitalizado: "))
        self.costo_total = 0

    def calcular_costo(self):
        # Definir los costos diarios por tipo de enfermedad
        costos_diarios = {1: 25, 2: 16, 3: 20, 4: 32}

        # Obtener el costo diario según el tipo de enfermedad
        costo_diario = costos_diarios.get(self.tipo_enfermedad, 0)

        # Calcular el costo base
        self.costo_total = costo_diario * self.dias_hospitalizado

        # Aplicar costo adicional si la edad está entre 14 y 22 años
        if 14 <= self.edad <= 22:
            self.costo_total *= 1.10

    def imprimir_costo(self):
        print(f"El costo total por paciente es: {self.costo_total:.2f}")

# Crear una instancia de la clase Paciente
paciente = Paciente()

# Calcular el costo total
paciente.calcular_costo()

# Imprimir el costo total
paciente.imprimir_costo()