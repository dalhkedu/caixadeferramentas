from faker import Faker


class GeradorDadosBrasil:
    def __init__(self):
        self.fake = Faker(['pt_BR'])

    def gerar_pessoa_fisica(self):
        nome = self.fake.name()
        cpf = self.fake.unique.random_int(min=100_000_000, max=999_999_999)
        data_nascimento = self.fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%d/%m/%Y')
        endereco = self.fake.address()
        telefone = self.fake.phone_number()

        return {
            'Nome': nome,
            'CPF': f'{cpf:011}',
            'Data de Nascimento': data_nascimento,
            'Endereço': endereco,
            'Telefone': telefone
        }

    def gerar_pessoa_juridica(self):
        razao_social = self.fake.company()
        cnpj = self.fake.unique.random_int(min=100_000_000_00000, max=999_999_999_99999)
        endereco = self.fake.address()
        telefone = self.fake.phone_number()

        return {
            'Razão Social': razao_social,
            'CNPJ': f'{cnpj:014}',
            'Endereço': endereco,
            'Telefone': telefone
        }


# Exemplo de uso:
gerador = GeradorDadosBrasil()

# Gere dados de uma pessoa física
dados_pf = gerador.gerar_pessoa_fisica()
print("Dados de Pessoa Física:")
for chave, valor in dados_pf.items():
    print(f"{chave}: {valor}")

# Gere dados de uma pessoa jurídica
dados_pj = gerador.gerar_pessoa_juridica()
print("\nDados de Pessoa Jurídica:")
for chave, valor in dados_pj.items():
    print(f"{chave}: {valor}")
