# import requests
# from bs4 import BeautifulSoup
#
# class RequisicaoTudoSobreTodos:
#     def __init__(self, nome, data_nascimento, cidade, estado):
#         self.base_url = "https://www.tudosobretodos.se/resultadoBuscaAvancada"
#         self.nome = nome
#         self.data_nascimento = data_nascimento
#         self.cidade = cidade
#         self.estado = estado
#
#     def fazer_requisicao(self):
#         url = f"{self.base_url}?nome={self.nome}&nascimento={self.data_nascimento}&cidade={self.cidade}&estado={self.estado}"
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.text
#         else:
#             return None
#
#     def alterar_data_nascimento(self, nova_data_nascimento):
#         self.data_nascimento = nova_data_nascimento
#
#     def extrair_dados(self, pagina_html):
#         soup = BeautifulSoup(pagina_html, 'html.parser')
#         # Aqui você pode usar os métodos do BeautifulSoup para extrair os dados que deseja
#         # por exemplo, encontrar elementos com base em suas classes, ids ou tags
#         # e extrair informações deles
#         # Exemplo:
#         resultado = soup.find('div', class_='classe-do-resultado')
#         if resultado:
#             return resultado.text
#         else:
#             return None
#
# # Exemplo de uso:
# if __name__ == "__main__":
#     requisicao = RequisicaoTudoSobreTodos(
#         nome="ANDERSON DE SOUZA RODRIGUES",
#         data_nascimento="10/03/1982",
#         cidade="VALPARAISO",
#         estado="SP"
#     )
#
#     # Faz a primeira requisição
#     resultado1 = requisicao.fazer_requisicao()
#
#     # Extrai dados usando BeautifulSoup
#     dados1 = requisicao.extrair_dados(resultado1)
#     print(dados1)
#
#     # Altera a data de nascimento
#     requisicao.alterar_data_nascimento("11/04/1990")
#
#     # Faz uma nova requisição com a data de nascimento alterada
#     resultado2 = requisicao.fazer_requisicao()
#
#     # Extrai dados da segunda página
#     dados2 = requisicao.extrair_dados(resultado2)
#     print(dados2)



import requests
from bs4 import BeautifulSoup

class RequisicaoTudoSobreTodos:
    def __init__(self, url):
        self.url = url

    def fazer_requisicao(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def extrair_dados(self, pagina_html):
        soup = BeautifulSoup(pagina_html, 'html.parser')
        # Aqui você pode usar os métodos do BeautifulSoup para extrair os dados que deseja
        # por exemplo, encontrar elementos com base em suas classes, ids ou tags
        # e extrair informações deles
        # Exemplo:
        nome = soup.find('span', class_='nome').text.strip()
        cpf = soup.find('span', class_='cpf').text.strip()
        return f"Nome: {nome}\nCPF: {cpf}"

# Exemplo de uso:
if __name__ == "__main__":
    url = "https://tudosobretodos.info/30260358827"
    requisicao = RequisicaoTudoSobreTodos(url)

    # Faz a requisição
    resultado = requisicao.fazer_requisicao()

    # Extrai dados usando BeautifulSoup
    dados = requisicao.extrair_dados(resultado)
    print(dados)

