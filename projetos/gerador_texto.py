from lorem_text import lorem


class GeradorTextoAleatorio:
    def __init__(self):
        self.lorem = lorem.words(500)

    def gerar_texto(self, com_titulo=True, quantidade_paragrafos=3):
        texto = ""

        if com_titulo:
            titulo = self.lorem.title()
            texto += f"<h1>{titulo}</h1>"

        for _ in range(quantidade_paragrafos):
            paragrafo = self.lorem.paragraph()
            texto += f"<p>{paragrafo}</p>"

        return texto


# Exemplo de uso:
gerador = GeradorTextoAleatorio()

# Gere um texto com título e 3 parágrafos (padrão)
texto_com_titulo = gerador.gerar_texto()
print("Texto com Título e 3 Parágrafos:")
print(texto_com_titulo)

# Gere um texto sem título e com 5 parágrafos
texto_sem_titulo = gerador.gerar_texto(com_titulo=False, quantidade_paragrafos=5)
print("\nTexto sem Título e 5 Parágrafos:")
print(texto_sem_titulo)
