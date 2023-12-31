
import random
import pytest
from servicos.usuarios import Usuarios
from servicos.conexao_weatherapi import ConexaoWeatherAPI
from servicos.clima_cidades import ClimaCidades
from utilidades.lista_de_cidades import lista_cidades_do_teste
from utilidades.logger import Logger


class TestClass():
    def test_se_nao_existir_usuarios_criados_devolver_dicionario_vazio(self):
        entrada = "Id de usuário inexistente"
        resultado_esperado = {}

        resultado_teste = Usuarios().buscar_usuario(entrada)

        assert resultado_teste == resultado_esperado


    @pytest.mark.skipif(Usuarios().lista_colections == True, reason='STRING')
    def test_retornar_o_nome_da_colection_que_esta_tentando_conectar_mesmo_se_env_nao_encontrada(self):
        resultado_esperado = str

        resultado_teste = type(Usuarios().conexao.name)

        assert resultado_teste == resultado_esperado


    def test_devolver_lista_com_cidades_do_teste_quando_chamar_a_funcao(self):
        entrada = lista_cidades_do_teste()
        resultado_esperado = list

        resultado_teste = type(entrada)

        assert resultado_teste == resultado_esperado


    def test_devolver_False_se_env_API_key_nao_existir_ou_tiver_um_valor_errado(self):
        entrada = 'valor não existe'
        resultado_esperado = False

        conexao_teste = ConexaoWeatherAPI()
        conexao_teste._API_key = entrada

        usuario_id = Usuarios().criar_usuario()['id']
        index = random.randrange(0, len(lista_cidades_do_teste()))
        cidade_id = lista_cidades_do_teste()[index]

        resultado_teste = conexao_teste.buscar_temperatura_uma_cidade(
            cidade_id,usuario_id
        )

        assert resultado_teste == resultado_esperado


    def test_quando_chamar_a_funcao_de_trazer_mais_de_uma_cidade_devolver_lista_vazia_se_env_API_key_nao_existir_ou_tiver_um_valor_errado(self):
        entrada = 'valor não existe'
        resultado_esperado = []

        conexao_teste = ConexaoWeatherAPI()
        conexao_teste._API_key = entrada

        usuario_id = Usuarios().criar_usuario()['id']
        cidades_ids = lista_cidades_do_teste()[0:3]

        resultado_teste = conexao_teste.buscar_temperatura_lista_de_cidades(
            cidades_ids,usuario_id
        )

        assert len(resultado_teste) == len(resultado_esperado)


    def test_sempre_que_iniciado_a_classe_logger_traz_seus_valores_atributos_como_none(self):
        resultado_esperado = None

        logger_teste = Logger().logger
        resultado_teste = logger_teste

        assert resultado_teste == resultado_esperado


    def test_retorna_dicionario_quando_busca_uma_cidade(self):
        resultado_esperado = dict

        conexao_teste = ConexaoWeatherAPI()

        usuario_id = Usuarios().criar_usuario()['id']
        index = random.randrange(0, len(lista_cidades_do_teste()))
        cidade_id = lista_cidades_do_teste()[index]

        resultado_teste = type(
            conexao_teste.buscar_temperatura_uma_cidade(
                cidade_id,
                usuario_id
            )
        )
        assert resultado_teste == resultado_esperado


    def test_limpa_base_de_usuarios_e_retorna_none(self):
        resultado_esperado = None

        usuario_teste = Usuarios()
        resultado_teste = usuario_teste.limpar_base_usuarios

        assert resultado_teste == resultado_esperado


    def test_retorna_dicionario_quando_busca_uma_cidade_na_base_de_dados(self):
        resultado_esperado = dict

        conexao_base_dados_teste = ClimaCidades()
        conexo_api_teste = ConexaoWeatherAPI()
        usuario_teste = Usuarios()

        conexao_base_dados_teste.limpar_base_clima
        usuario_id = usuario_teste.criar_usuario()['id']
        index = random.randrange(0, len(lista_cidades_do_teste()))
        cidade_id = lista_cidades_do_teste()[index]
        dados = conexo_api_teste.buscar_temperatura_uma_cidade(cidade_id, usuario_id)
        conexao_base_dados_teste.armazenar_dados_clima([dados])

        resultado_teste = type(
            conexao_base_dados_teste.buscar_clima_de_uma_cidade(str(cidade_id))
        )
        conexao_base_dados_teste.limpar_base_clima
        assert resultado_teste == resultado_esperado


    def test_retorna_lista_quando_busca_todas_as_cidade_na_base_de_dados(self):
        resultado_esperado = list

        conexao_base_dados_teste = ClimaCidades()
        conexo_api_teste = ConexaoWeatherAPI()
        usuario_teste = Usuarios()

        conexao_base_dados_teste.limpar_base_clima
        usuario_id = usuario_teste.criar_usuario()['id']
        cidades_ids = lista_cidades_do_teste()[0:3]
        dados = conexo_api_teste.buscar_temperatura_lista_de_cidades(
            cidades_ids,
            usuario_id
        )
        conexao_base_dados_teste.armazenar_dados_clima(dados)

        resultado_teste = type(
            conexao_base_dados_teste.buscar_clima_todas_cidades()
        )
        conexao_base_dados_teste.limpar_base_clima
        assert resultado_teste == resultado_esperado


    def test_retorna_float_representando_o_percentual_quando_usa_a_funcao_percentual(self):
        entrada = lista_cidades_do_teste()[0:5]
        resultado_esperado = round(5/len(lista_cidades_do_teste()),2)

        conexao_base_dados_teste = ClimaCidades()
        conexo_api_teste = ConexaoWeatherAPI()
        usuario_teste = Usuarios()

        conexao_base_dados_teste.limpar_base_clima
        usuario_id = usuario_teste.criar_usuario()['id']
        dados = conexo_api_teste.buscar_temperatura_lista_de_cidades(
            entrada,
            usuario_id
        )
        conexao_base_dados_teste.armazenar_dados_clima(dados)
        resposta_funcao = conexao_base_dados_teste.percentual_armazenado()

        resultado_teste = round(
            (resposta_funcao['total_armazenados_ate_o_momento'])/(resposta_funcao['total_cidades_do_teste']),2
        )
        conexao_base_dados_teste.limpar_base_clima
        assert resultado_teste == resultado_esperado