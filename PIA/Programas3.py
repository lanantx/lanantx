class Meteorologia:
    def __init__(self):
        self.lluvias_norte = []
        self.lluvias_centro = []
        self.lluvias_sur = []

        # Cargar los registros de lluvias por teclado
        print("Ingrese las lluvias mensuales de la región NORTE:")
        for i in range(12):
            lluvia = float(input(f"Mes {i+1}: "))
            self.lluvias_norte.append(lluvia)

        print("Ingrese las lluvias mensuales de la región CENTRO:")
        for i in range(12):
            lluvia = float(input(f"Mes {i+1}: "))
            self.lluvias_centro.append(lluvia)

        print("Ingrese las lluvias mensuales de la región SUR:")
        for i in range(12):
            lluvia = float(input(f"Mes {i+1}: "))
            self.lluvias_sur.append(lluvia)

    def promedio_anual_centro(self):
        promedio = sum(self.lluvias_centro) / 12
        return promedio

    def menor_lluvia_sur(self):
        menor_lluvia = min(self.lluvias_sur)
        mes_menor_lluvia = self.lluvias_sur.index(menor_lluvia) + 1
        return mes_menor_lluvia, menor_lluvia

    def mayor_lluvia_anual(self):
        total_norte = sum(self.lluvias_norte)
        total_centro = sum(self.lluvias_centro)
        total_sur = sum(self.lluvias_sur)

        max_lluvia = max(total_norte, total_centro, total_sur)

        if max_lluvia == total_norte:
            return "NORTE", total_norte
        elif max_lluvia == total_centro:
            return "CENTRO", total_centro
        else:
            return "SUR", total_sur

    def imprimir_resultados(self):
        print(f"Promedio anual de la región CENTRO: {self.promedio_anual_centro():.2f} mm")

        mes_menor_lluvia, menor_lluvia = self.menor_lluvia_sur()
        print(f"Mes con menor lluvia en la región SUR: Mes {mes_menor_lluvia} con {menor_lluvia:.2f} mm")

        region_mayor_lluvia, total_lluvia = self.mayor_lluvia_anual()
        print(f"La región con mayor lluvia anual es {region_mayor_lluvia} con un total de {total_lluvia:.2f} mm")

# Crear una instancia de la clase Meteorologia
meteorologia = Meteorologia()

# Imprimir los resultados
meteorologia.imprimir_resultados()