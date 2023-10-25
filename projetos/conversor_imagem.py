import os

import cairosvg


class ConversorPNGtoSVG:
    def __init__(self, pasta_entrada, pasta_saida):
        self.pasta_entrada = pasta_entrada
        self.pasta_saida = pasta_saida

    def converter(self, nome_arquivo):
        if not os.path.exists(self.pasta_saida):
            os.makedirs(self.pasta_saida)

        caminho_entrada = os.path.join(self.pasta_entrada, nome_arquivo)
        caminho_saida = os.path.join(self.pasta_saida, nome_arquivo.replace('.png', '.svg'))

        cairosvg.svg2svg(url=caminho_entrada, write_to=caminho_saida)


# Exemplo de uso:
pasta_entrada = "imagens_png"
pasta_saida = "imagens_svg"
conversor = ConversorPNGtoSVG(pasta_entrada, pasta_saida)

# Converte uma imagem chamada "exemplo.png" para SVG
conversor.converter("exemplo.png")
