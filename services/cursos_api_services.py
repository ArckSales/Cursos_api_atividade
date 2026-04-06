from domain.aluno import Aluno

from domain.curso import Curso

from repositories.memory import db

class Cursos_api_Service:
 def criar_alunos(self,id: float, nome: str, email: str):
    if id in db.alunos_por_id:
        return db.alunos_por_id[id]
    aluno = Aluno(id=id, email=email)
    db.alunos_por_id[id] = aluno
    return aluno
 def listar_alunos(li):
    pass

 def criar_curso(self, codigo: int, valor: float, tipo: int, desconto_percentual: float,) -> Curso:
     curso= Curso(codigo=codigo, valor=valor, tipo=tipo, desconto_percentual=desconto_percentual)
     db.cursos_por_codigo[codigo] = curso
     return curso

 def listar_cursos(self):
    pass

 def obter_curso(self, codigo: int) -> Curso | None:
        return db.curso_por_codigo.get(codigo)

 def atualizar_preco(codigo: int, novo_preco: float):
    pass


def service():
    return None