from fastapi import APIRouter
from fastapi.responses import JSONResponse
from servicos.usuarios import Usuarios
from servicos.clima_cidades import ClimaCidades
from utilidades.descricoes_endpoint import Descricoes

router = APIRouter(prefix="/base-dados", tags=["Gestao Base dados"])

usuarios = Usuarios()
dados_clima = ClimaCidades()
descricoes = Descricoes()

@router.delete(
    "/limpar-base-dados",
    description=descricoes.deletar_base_dados()
)
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


@router.delete(
    "/resetar-cenario",
    description=descricoes.resetar_cenario()
)
async def resetar_cenario_do_aplicativo(usuario_id:str):
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
    usuarios.limpar_base_usuarios
    return JSONResponse(
            status_code=200,
            content={"mensagem": "Base de usuarios e de cidades, apagadas com sucesso."}
    )