import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime
from utilidades.logger import Logger

load_dotenv()
logger = Logger.init("Iniciando Weather API")

class ConexaoWeatherAPI():
    def __init__(self) -> None:
        self._API_key = os.getenv("API_key")

    @property
    def api_key(self):
        return self._API_key

    def buscar_temperatura_uma_cidade(self, cidade_id:int, usuario_id:str):
        url = f'https://api.openweathermap.org/data/2.5/weather?id={cidade_id}&appid={self.api_key}&units=metric'
        conexao = requests.get(url)
        informacao = conexao.text
        if conexao.status_code not in [200, 201]:
            logger.error(informacao)
            return False

        cidade = json.loads(informacao)
        resposta = {
            'usuario_id': usuario_id,
            'cidade_id': str(cidade_id),
            'temperatura': cidade['main']['temp'],
            'unidade_temperatura': 'Celsius',
            'humidade':cidade['main']['humidity'],
            'data_criacao': datetime.now().isoformat()
        }
        return resposta


    def buscar_temperatura_lista_de_cidades(
        self,
        cidades_ids:list,
        usuario_id:str
    ):
        payloads_das_temperaturas_e_cidades = []
        for cidade_id in cidades_ids:
            payload_temperatura_e_cidade_id = (
                self.buscar_temperatura_uma_cidade(cidade_id,usuario_id)
            )
            if not payload_temperatura_e_cidade_id:
                logger.error(f'\nCidade_id {cidade_id} NÃO ENCONTRADO.\n')
                continue

            payloads_das_temperaturas_e_cidades.append(
                payload_temperatura_e_cidade_id
            )

        return payloads_das_temperaturas_e_cidades
