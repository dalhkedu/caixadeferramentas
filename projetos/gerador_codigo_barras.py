import barcode
from barcode import generate
from barcode.writer import ImageWriter


class GeradorCodigoBarras:
    def __init__(self, formato="Code128"):
        self.formato = formato

    def gerar_codigo_barras(self, dado, nome_arquivo_saida):
        # Escolha o formato do código de barras
        if self.formato == "Code128":
            tipo_codigo = barcode.CODE128
        elif self.formato == "Code39":
            tipo_codigo = barcode.CODE39
        elif self.formato == "QRCode":
            tipo_codigo = barcode.QRCODE
        else:
            raise ValueError("Formato de código de barras não suportado.")

        # Gere o código de barras e salve em um arquivo de imagem
        codigo = generate(tipo_codigo(dado), writer=ImageWriter(), output=nome_arquivo_saida)


# Exemplo de uso:
gerador = GeradorCodigoBarras(formato="Code128")

# Gere um código de barras para um dado ou link e salve-o em um arquivo de imagem
gerador.gerar_codigo_barras("123456789", "codigo_barras.png")
