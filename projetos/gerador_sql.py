class GeradorSQLCRUD:
    def __init__(self, tabela, campos):
        self.tabela = tabela
        self.campos = campos

    def gerar_script_create(self):
        campos_sql = ", ".join(f'{campo} TEXT' for campo in self.campos)
        script = f'CREATE TABLE IF NOT EXISTS {self.tabela} ({campos_sql});'
        return script

    def gerar_script_insert(self, valores):
        campos_sql = ", ".join(self.campos)
        valores_sql = ", ".join(f'"{valor}"' for valor in valores)
        script = f'INSERT INTO {self.tabela} ({campos_sql}) VALUES ({valores_sql});'
        return script

    def gerar_script_select(self):
        script = f'SELECT * FROM {self.tabela};'
        return script

    def gerar_script_update(self, valores, condicao):
        atualizacoes = ", ".join(f'{campo} = "{valor}"' for campo, valor in zip(self.campos, valores))
        script = f'UPDATE {self.tabela} SET {atualizacoes} WHERE {condicao};'
        return script

    def gerar_script_delete(self, condicao):
        script = f'DELETE FROM {self.tabela} WHERE {condicao};'
        return script
