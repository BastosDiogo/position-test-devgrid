from fastapi import APIRouter
from fastapi.responses import JSONResponse
from servicos.usuarios import Usuarios
from servicos.clima_cidades import ClimaCidades

router = APIRouter(prefix="/base-dados", tags=["Gestao Base dados"])

usuarios = Usuarios()
dados_clima = ClimaCidades()

@router.delete("/limpar-base-dados")
async def limpar_base_dados(usuario_id:str):
    usurio_na_base = usuarios.buscar_usuario(usuario_id)
    if len(usurio_na_base) == 0:
        return JSONResponse(
            status_code=404,
            content={
                "ERRO": f"Usuário {usuario_id} NÃO ENCONTRADO.",
                "mensagem": "Verifique se você usou o endpoit para gerar usuários."
            }
        )
    dados_clima.limpar_base_clima
    return JSONResponse(
            status_code=200,
            content={"mensagem": "Dados apagados com sucesso."}
    )
