from fastapi import APIRouter
from fastapi.responses import JSONResponse
from servicos.usuarios import Usuarios
from servicos.clima_cidades import ClimaCidades
from fastapi import APIRouter, BackgroundTasks
from servicos.armazenamento import Armazenar
from utilidades.descricoes_endpoint import Descricoes

router = APIRouter(prefix="/clima", tags=["Endpoints API clima"])

usuarios = Usuarios()
dados_clima = ClimaCidades()
descricoes = Descricoes()

@router.get("/gerar-usuario-id", description=descricoes.gerar_usuario())
async def gerar_usuario_id():
    usuario_criado = usuarios.criar_usuario()
    if len(usuario_criado) == 0:
        return JSONResponse(
            status_code=404,
            content={
                "ERRO": "Não foi possível criar um id de usuário.",
                "mensagem": "Verifique se você está usando as variáveis de ambiente corretas."
            }
        )
    return JSONResponse(
        status_code=201,
        content={
            "usuario_id": usuario_criado['id']
        }
    )


@router.post(
    "/armazenar-temperaturas",
    description=descricoes.armazenar_temperatura()
)
async def armazenar_temperaturas_da_lista_de_cidades(
    usuario_id:str,
    background: BackgroundTasks
):
    usurio_na_base = usuarios.buscar_usuario(usuario_id)
    if len(usurio_na_base) == 0:
        return JSONResponse(
            status_code=404,
            content={
                "ERRO": f"Usuário {usuario_id} NÃO ENCONTRADO.",
                "mensagem": "Verifique se você usou o endpoit para gerar usuários."
            }
        )
    background.add_task(Armazenar(usuario_id).start)
    return JSONResponse(
        status_code=202,
        content={
            "resposta": "Armazenamento de dados climáticos em andamento"
        }
    )


@router.get(
    "/percentual-armazenado",
    description=descricoes.percentual_armazenado()
)
async def conferir_percentual_dos_dados_armazenado(usuario_id:str):
    usurio_na_base = usuarios.buscar_usuario(usuario_id)
    if len(usurio_na_base) == 0:
        return JSONResponse(
            status_code=404,
            content={
                "ERRO": f"Usuário {usuario_id} NÃO ENCONTRADO.",
                "mensagem": "Verifique se você usou o endpoit para gerar usuários."
            }
        )
    percentual =  dados_clima.percentual_armazenado()
    return JSONResponse(status_code=200, content=percentual)


@router.get(
    "/trazer-todos-dados-climaticos-armazenados",
    description=descricoes.todos_dados_climaticos()
)
async def trazer_todos_dados_climaticos_armazenados(usuario_id:str):
    usurio_na_base = usuarios.buscar_usuario(usuario_id)
    if len(usurio_na_base) == 0:
        return JSONResponse(
            status_code=404,
            content={
                "ERRO": f"Usuário {usuario_id} NÃO ENCONTRADO.",
                "mensagem": "Verifique se você usou o endpoit para gerar usuários."
            }
        )
    dados_climaticos_armazenados = dados_clima.buscar_clima_todas_cidades()
    return JSONResponse(
        status_code=200,
        content={
            "dados_climaticos":  dados_climaticos_armazenados
        }
    )


@router.get(
    "/trazer-dados-climaticos-armazenados-cidade/{cidade_id}",
    description=descricoes.dados_climaticos_de_uma_cidade()
)
async def trazer_todos_dados_climaticos_armazenados(
    usuario_id:str,
    cidade_id:str
):
    usurio_na_base = usuarios.buscar_usuario(usuario_id)
    if len(usurio_na_base) == 0:
        return JSONResponse(
            status_code=404,
            content={
                "ERRO": f"Usuário {usuario_id} NÃO ENCONTRADO.",
                "mensagem": "Verifique se você usou o endpoit para gerar usuários."
            }
        )
    dado_climatico = dados_clima.buscar_clima_de_uma_cidade(cidade_id)
    if dado_climatico == None or len(dado_climatico) == 0:
        return JSONResponse(
            status_code=404,
            content={"ERRO": f"Cidade {cidade_id} NÃO ENCONTRADA."}
        )

    return JSONResponse(status_code=200, content=dado_climatico)