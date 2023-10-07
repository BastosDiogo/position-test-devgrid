from threading import Thread
from servicos.clima_cidades import ClimaCidades
from servicos.conexao_weatherapi import ConexaoWeatherAPI
from utilidades.lista_de_cidades import lista_cidades_do_teste
from utilidades.logger import Logger
import time


class Armazenar(Thread):
    def __init__(self, usuario_id:str):
        self.clima = ClimaCidades()
        self.weatherapi = ConexaoWeatherAPI()
        self.usuario = usuario_id
        super().__init__()

    def run(self):
        cidades_do_teste = lista_cidades_do_teste()
        agrupamento_de_50_em_50_cidades = [
            cidades_do_teste[0:50],
            cidades_do_teste[50:100],
            cidades_do_teste[100:150],
            cidades_do_teste[150:],
        ]

        logger = Logger.init("Coleta e Amazenamento")
        etapa_de_busca = 1
        for agrupamento in agrupamento_de_50_em_50_cidades:
            logger.info(f'Iniciando a parte {etapa_de_busca}/4 de coleta.')
            dados_temperaturas = (
                self.weatherapi.buscar_temperatura_lista_de_cidades(
                    agrupamento, self.usuario
                )
            )
            self.clima.armazenar_dados_clima(dados_temperaturas)
            if etapa_de_busca == 4:
                break
            logger.info('Aguardando 60 segundos para nova coleta.')
            time.sleep(61.1)
            etapa_de_busca += 1
        logger.info(f'Coleta das {len(cidades_do_teste)} realizada.')
