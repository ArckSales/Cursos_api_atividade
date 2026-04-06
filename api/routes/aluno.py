from fastapi import APIRouter, HTTPException
from schemas.aluno import AlunoCreate, AlunoOut
from services.cursos_api_services import service

router = APIRouter(prefix="/alunos", tags=["alunos"])

@router.post("", response_model=AlunoOut)
def criar(payload: AlunoCreate):
    aluno = service.criar_aluno(payload.id, payload.nome)
    return AlunoOut(id=aluno.id, nome=aluno.nome)

@router.get("/{id}", response_model=AlunoOut)
def obter(cpf: str):
    aluno = service.obter_aluno(id)
    if not aluno:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
            )
    return AlunoOut(id=aluno.id, nome=aluno.nome)