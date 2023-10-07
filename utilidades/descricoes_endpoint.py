
class Descricoes():
    def deletar_base_dados(self):
        descricao = """
            Esse endpoint limpa a base de dados do onde são armazenados, os
        as informações após a consulta no endpoint da Open Weather API.
        \n
            Parâmetros:
            * usario_id(str): String. Esse o ID de usuário que deve ser
            gerado no endpoint '/gerar-usuario-id'
        \n
        """
        return descricao

    def resetar_cenario(self):
        descricao = """
            Esse endpoint limpa a base de dados do onde são armazenados, os
        as informações após a consulta no endpoint da Open Weather API.
        Assim como os IDs de usuários criados para utilização dos endpoints
        dessa aplicação.
            Ou seja, esse endpoint reseta deixando TODAS as base de dados
        vazias para utilização.
        \n
            Parâmetros:
            * usario_id(str): String. Esse o ID de usuário que deve ser
            gerado no endpoint '/gerar-usuario-id'
        \n
        """
        return descricao

    def gerar_usuario(self):
        descricao = """
            Esse endpoint gera ID de usuário necessário para utilizar TODOS
        os endpoints dessa aplicação.
        """
        return descricao

    def armazenar_temperatura(self):
        descricao = """
            Esse endpoint faz a consulta no endpoint da Open Weather API e
        armazena os dados dessa consulta, no banco de dados dessa aplicação.
            Vale resaltar que as cidades desejadas, estão de forma hard-code
        nessa aplicação.
        \n
            Parâmetros:
            * usario_id(str): String. Esse o ID de usuário que deve ser
            gerado no endpoint '/gerar-usuario-id'
        \n
        """
        return descricao

    def percentual_armazenado(self):
        descricao = """
            Esse endpoint retorna o percentual da lista de cidades que está
        hard-code nessa aplicação.
            Ou seja, esse enpoint traz a razão entre dados armazenados e o
        total de cidades listados no Anexo A do teste.
        \n
            Parâmetros:
            * usario_id(str): String. Esse o ID de usuário que deve ser
            gerado no endpoint '/gerar-usuario-id'
        \n
        """
        return descricao

    def todos_dados_climaticos(self):
        descricao = """
            Esse endpoint retorna todos os dados armazenados após consulta 
        no endpoint da Open Weather API.
        \n
            Parâmetros:
            * usario_id(str): String. Esse o ID de usuário que deve ser
            gerado no endpoint '/gerar-usuario-id'
        \n
        """
        return descricao


    def dados_climaticos_de_uma_cidade(self):
        descricao = """
            Esse endpoint retorna os dados armazenados após consulta 
        no endpoint da Open Weather API, de uma ciadade em específica.
        \n
            Parâmetros:
            * usario_id(str): String. Esse o ID de usuário que deve ser
            gerado no endpoint '/gerar-usuario-id';
            * cidade_id(str): String. Esse é o cidade_id que está no Anexo
            A do teste.
        \n
        """
        return descricao