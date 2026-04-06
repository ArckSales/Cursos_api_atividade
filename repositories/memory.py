from typing import Dict
from domain.aluno import Aluno
from domain.curso import Curso


class MemoryDB:
    def __init__(self):
        self.alunos_por_id: Dict[int, Aluno] = {}
        self.Cursos_por_codigo: Dict[int, Curso] = {}


db = MemoryDB()
