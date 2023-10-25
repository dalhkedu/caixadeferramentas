class CalculadoraCustoEnergia:
    def __init__(self, tarifa_kwh):
        self.tarifa_kwh = tarifa_kwh

    def calcular_custo(self, consumo_kwh_mes):
        custo_reais = (consumo_kwh_mes / 30) * self.tarifa_kwh
        return custo_reais

    def calcular_horas(self, horas, consumo_kwh_mes):
        custo_reais = horas * ((consumo_kwh_mes / 30) * self.tarifa_kwh)
        return custo_reais

    def calcular_dias(self, dias, horas, consumo_kwh_mes):
        custo_reais = (horas * ((consumo_kwh_mes / 30) * self.tarifa_kwh)) * dias
        return custo_reais


if __name__ == "__main__":
    pass
