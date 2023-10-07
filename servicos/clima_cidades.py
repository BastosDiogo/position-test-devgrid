from mongo.conexao import Pymongo
from utilidades.logger import Logger
from utilidades.lista_de_cidades import lista_cidades_do_teste

logger = Logger.init("Conectando com o Mongo DB")

class ClimaCidades(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self._colection = 'clima_cidades'

    @property
    def colection(self):
        return self._colection

    @property
    def conexao(self):
        return self.database[self.colection]

    @property
    def limpar_base_clima(self):
        self.conexao.delete_many({})

    def buscar_clima_de_uma_cidade(self, cidade_id:str):
        try:
            cidade = self.conexao.find_one(
                {"cidade_id": cidade_id},
                {"_id":0}
            )
            return cidade

        except Exception as erro:
            logger.error(f'{erro}')
            return {}


    def buscar_clima_todas_cidades(self):
        try:
            cidades = list(self.conexao.find({},{"_id":0}))
            return cidades

        except Exception as erro:
            logger.error(f'{erro}')
            return []

    def armazenar_dados_clima(self, lista_dados:list):
        try:
            self.conexao.insert_many(lista_dados)
            return True

        except Exception as erro:
            logger.error(f'{erro}')
            return False

    def percentual_armazenado(self):
        total_cidades_do_teste = len(lista_cidades_do_teste())
        armazenados_ate_o_momento = len(self.buscar_clima_todas_cidades())
        percentual_armazenado = (
            armazenados_ate_o_momento/total_cidades_do_teste
        )
        resposta = {
            "total_armazenados_ate_o_momento":armazenados_ate_o_momento,
            "total_cidades_do_teste": total_cidades_do_teste,
            "percentual_concluido":f'{round(percentual_armazenado*100, 2)}%'
        }

        return resposta
