from fastapi import APIRouter, HTTPException
from schemas.curso import CursoCreate, CursoOut, CursoAlterarValor
from services.cursos_api_services import service

router = APIRouter(prefix="/cursos", tags=["cursos"])


@router.post("", response_model=CursoOut)
def criar(payload: CursoCreate):
    curso = service.criar_curso(
        payload.codigo,
        payload.titulo,
        payload.preco,
        payload.tipo,
        payload.desconto_percentual
    )
    return CursoOut(**curso.__dict__)


@router.get("/{codigo}", response_model=CursoOut)
def obter(codigo: int):
    curso = service.obter_curso(codigo)
    if not curso:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return CursoOut(**curso.__dict__)


@router.put("/{codigo}/valor")
def alterar_valor(codigo: int, payload: CursoAlterarValor):
    alterou = service.alterar_valor_curso(codigo, payload.novo_valor)
    if not alterou:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return {"alterou": True}