import random


class GeradorCPF_CNPJ:
    @staticmethod
    def gerar_cpf():
        cpf = [random.randint(0, 9) for _ in range(9)]

        # Calcula os dígitos verificadores do CPF
        soma = sum((i + 1) * v for i, v in enumerate(cpf))
        resto = soma % 11

        if resto < 2:
            cpf.append(0)
        else:
            cpf.append(11 - resto)

        soma = sum((i + 2) * v for i, v in enumerate(cpf))
        resto = soma % 11

        if resto < 2:
            cpf.append(0)
        else:
            cpf.append(11 - resto)

        return ''.join(map(str, cpf))

    @staticmethod
    def gerar_cnpj():
        cnpj = [random.randint(0, 9) for _ in range(12)]

        # Calcula os dígitos verificadores do CNPJ
        def calcular_digito_verificador(cnpj):
            multiplicadores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            soma = sum(m * int(c) for m, c in zip(multiplicadores, cnpj))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto

        cnpj.append(calcular_digito_verificador(cnpj))
        cnpj.append(calcular_digito_verificador(cnpj))

        return ''.join(map(str, cnpj))


# Exemplo de uso:
gerador = GeradorCPF_CNPJ()
cpf = gerador.gerar_cpf()
cnpj = gerador.gerar_cnpj()

print(f"CPF gerado: {cpf}")
print(f"CNPJ gerado: {cnpj}")
