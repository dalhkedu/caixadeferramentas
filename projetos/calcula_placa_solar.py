class CalculadoraEnergiaSolar:
    def __init__(self, potencia_placa_watts, irradiacao_media_diaria_kwh_m2_dia, eficiencia_sistema):
        self.potencia_placa_watts = potencia_placa_watts
        self.irradiacao_media_diaria_kwh_m2_dia = irradiacao_media_diaria_kwh_m2_dia
        self.eficiencia_sistema = eficiencia_sistema

    def calcular_energia_diaria(self):
        # Cálculo da energia gerada diariamente (kWh)
        energia_diaria_kwh = (self.potencia_placa_watts * self.irradiacao_media_diaria_kwh_m2_dia * self.eficiencia_sistema) / 1000
        return energia_diaria_kwh

    def calcular_energia_mensal(self):
        # Cálculo da energia gerada mensalmente (kWh)
        energia_diaria_kwh = self.calcular_energia_diaria()
        dias_no_mes = 30  # Assumindo um mês de 30 dias
        energia_mensal_kwh = energia_diaria_kwh * dias_no_mes
        return energia_mensal_kwh


# Exemplo de uso:
potencia_placa = 560  # Potência da placa solar em watts
irradiacao_media_diaria = 4.93  # Irradiação média diária de sol em kWh/m2/dia
eficiencia_sistema = 0.75  # Eficiência do sistema (75%)

calculadora_solar = CalculadoraEnergiaSolar(potencia_placa, irradiacao_media_diaria, eficiencia_sistema)

# Calcular a energia gerada diariamente
energia_diaria = calculadora_solar.calcular_energia_diaria()
print(f"Energia gerada diariamente: {energia_diaria:.2f} kWh")

# Calcular a energia gerada mensalmente
energia_mensal = calculadora_solar.calcular_energia_mensal()
print(f"Energia gerada mensalmente: {energia_mensal:.2f} kWh")
