import unittest

from projetos.calcula_energia import CalculadoraCustoEnergia


class TestCalculadoraCustoEnergia(unittest.TestCase):
    def test_calculo_custo_energia(self):
        tarifa_energia = 0.95
        consumo_kwh_mes = 17.1
        horas = 8
        dias = 30

        calculadora = CalculadoraCustoEnergia(tarifa_energia)

        custo_esperado = (consumo_kwh_mes / 30) * tarifa_energia
        horas_custo_esperado = horas * custo_esperado
        dias_custo_esperado = dias * horas_custo_esperado

        print(custo_esperado)
        print(horas_custo_esperado)
        print(f"{dias_custo_esperado:.2f}")

        custo_calculado = calculadora.calcular_custo(consumo_kwh_mes)
        custo_horas = calculadora.calcular_horas(horas, consumo_kwh_mes)
        custo_dias = calculadora.calcular_dias(dias, horas, consumo_kwh_mes)

        self.assertEqual(custo_calculado, custo_esperado)
        self.assertEqual(custo_horas, horas_custo_esperado)
        self.assertEqual(custo_dias, dias_custo_esperado)


if __name__ == "__main__":
    unittest.main()
