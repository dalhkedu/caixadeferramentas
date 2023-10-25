import os

from PIL import Image


class RedutorTamanhoImagem:
    def __init__(self, pasta_entrada, pasta_saida):
        self.pasta_entrada = pasta_entrada
        self.pasta_saida = pasta_saida

    def reduzir_tamanho(self, nome_arquivo, formato="JPEG", qualidade=85):
        # Verifica se a pasta de saída existe, senão cria
        if not os.path.exists(self.pasta_saida):
            os.makedirs(self.pasta_saida)

        # Abre a imagem de entrada
        caminho_entrada = os.path.join(self.pasta_entrada, nome_arquivo)
        imagem = Image.open(caminho_entrada)

        # Salva a imagem redimensionada na pasta de saída
        nome_saida = nome_arquivo
        caminho_saida = os.path.join(self.pasta_saida, nome_saida)
        imagem.save(caminho_saida, formato, quality=qualidade)


# Exemplo de uso:
pasta_entrada = "imagens_entrada"
pasta_saida = "imagens_saida"
redutor = RedutorTamanhoImagem(pasta_entrada, pasta_saida)

# Reduz o tamanho de uma imagem chamada "exemplo.jpg" em formato JPEG
redutor.reduzir_tamanho("exemplo.jpg", formato="JPEG", qualidade=50)

# Reduz o tamanho de uma imagem chamada "exemplo.png" em formato PNG
redutor.reduzir_tamanho("exemplo.png", formato="PNG", qualidade=50)
