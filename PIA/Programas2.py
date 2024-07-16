class Eleccion:
    def __init__(self):
        self.votos_candidatos = [0, 0, 0, 0]  # Lista para almacenar los votos de los 4 candidatos
        self.total_votos = 0

    def registrar_votos(self):
        print("Ingrese los votos uno por uno (finalice con 0):")
        while True:
            voto = int(input())
            if voto == 0:
                break
            if voto in [1, 2, 3, 4]:
                self.votos_candidatos[voto - 1] += 1
                self.total_votos += 1
            else:
                print("Voto inválido, por favor ingrese un voto entre 1 y 4, o 0 para finalizar.")

    def calcular_porcentajes(self):
        porcentajes = []
        for votos in self.votos_candidatos:
            if self.total_votos > 0:
                porcentajes.append((votos / self.total_votos) * 100)
            else:
                porcentajes.append(0)
        return porcentajes

    def imprimir_resultados(self):
        porcentajes = self.calcular_porcentajes()
        for i in range(4):
            print(f"Candidato {i+1}: {self.votos_candidatos[i]} votos, {porcentajes[i]:.2f}% del total")

# Crear una instancia de la clase Eleccion
eleccion = Eleccion()

# Registrar los votos
eleccion.registrar_votos()

# Imprimir los resultados
eleccion.imprimir_resultados()
