from pydantic import BaseModel

class AlunoCreate(BaseModel):
    id: float
    nome: str = ""
    email: str = ""

class AlunoOut(BaseModel):
    id: float
    nome: str = ""
    email: str = ""