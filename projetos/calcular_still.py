class CalculadoraCustoFotografia:
    def __init__(self, produtos, fotos_por_produto, valor_hora_edicao, valor_hora_estudio, fotos_editadas_hora,
                 fotos_feitas_hora):
        self.produtos = produtos
        self.fotos_por_produto = fotos_por_produto
        self.valor_hora_edicao = valor_hora_edicao
        self.valor_hora_estudio = valor_hora_estudio
        self.fotos_feitas_hora = fotos_feitas_hora
        self.fotos_editadas_hora = fotos_editadas_hora

    def calcular_custo_total(self):
        # Cálculo do tempo necessário para fotografar e editar todas as fotos
        tempo_fotografia_horas = self.produtos * self.fotos_por_produto
        tempo_edicao_horas = (tempo_fotografia_horas / self.fotos_editadas_hora) * self.valor_hora_edicao

        # Cálculo do custo total
        custo_estudio = (tempo_fotografia_horas / self.fotos_feitas_hora) * self.valor_hora_estudio
        custo_edicao = tempo_edicao_horas * self.valor_hora_edicao
        custo_total = custo_estudio + custo_edicao

        return custo_total
