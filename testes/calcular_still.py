import unittest

from projetos.calcular_still import CalculadoraCustoFotografia


class TestCalculadoraCustoFotografia(unittest.TestCase):
    def test_calculo_custo_fotografia(self):
        # Valores de exemplo para o teste
        produtos = 10
        fotos_por_produto = 5
        valor_hora_edicao = 50  # Valor por hora de edição em reais
        valor_hora_estudio = 100  # Valor por hora do estúdio em reais
        fotos_editadas_hora = 3  # Quantidade de fotos editadas por hora
        fotos_feitas_hora = 5  # Quantidade de fotos feitas por hora

        # Cria uma instância da classe CalculadoraCustoFotografia com os valores de exemplo
        calculadora = CalculadoraCustoFotografia(
            produtos,
            fotos_por_produto,
            valor_hora_edicao,
            valor_hora_estudio,
            fotos_editadas_hora,
            fotos_feitas_hora
        )

        # Cálculo manual do custo total esperado
        tempo_fotografia_horas = produtos * fotos_por_produto
        tempo_edicao_horas = (tempo_fotografia_horas / fotos_editadas_hora) * valor_hora_edicao
        custo_estudio = (tempo_fotografia_horas / fotos_feitas_hora) * valor_hora_estudio
        custo_edicao = tempo_edicao_horas * valor_hora_edicao
        custo_total_esperado = custo_estudio + custo_edicao

        # Calcula o custo real usando a classe CalculadoraCustoFotografia
        custo_calculado = calculadora.calcular_custo_total()

        # Verifica se o custo calculado é igual ao custo esperado
        self.assertEqual(custo_calculado, custo_total_esperado)


if __name__ == "__main__":
    unittest.main()
