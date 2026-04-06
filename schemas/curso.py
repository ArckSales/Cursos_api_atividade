from pydantic import BaseModel

class CursoCreate(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: float = 0.0

class CursoOut(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: float = 0.0

class CursoAlterarValor(BaseModel):
    novo_valor = float
