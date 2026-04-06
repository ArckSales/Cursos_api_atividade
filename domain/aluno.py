from dataclasses import dataclass


@dataclass(frozen=True)
class Aluno:
    id: float
    nome: str = ""
    email: str = ""
