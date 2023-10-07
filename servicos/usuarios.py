from mongo.conexao import Pymongo
from utilidades.logger import Logger
from uuid import uuid4
from datetime import datetime

logger = Logger.init("Conectando com o Mongo DB")

class Usuarios(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self._colection = 'usuarios'

    @property
    def colection(self):
        return self._colection

    @property
    def conexao(self):
        return self.database[self.colection]

    @property
    def limpar_base_usuarios(self):
        self.conexao.delete_many({})

    def buscar_usuario(self, usuario_id:str):
        try:
            usuario = self.conexao.find_one({"id": usuario_id},{"_id":0})
            return {} if usuario == None else usuario

        except Exception as erro:
            logger.error(f'{erro}')
            return {}

    def criar_usuario(self):
        try:
            usuario_id = str(uuid4())
            self.conexao.insert_one(
                {
                    "id": usuario_id,
                    "data_criacao": datetime.now().isoformat()
                }
            )
            usuario = self.buscar_usuario(usuario_id)
            return usuario

        except Exception as erro:
            logger.error(f'{erro}')
            return {}
