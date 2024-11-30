#Aluna: Gabryelly Jeniffer
#Disciplia: Raciociono Computacional

# Importando as funções criadas na atividade formativa
import FuncaoUtil as fun
import FuncaoEstudante as fun_estudante
import FuncaoProfessor as fun_professor
import FuncaoDisciplina as fun_disciplina
import FuncaoTurmas as fun_turma
import FuncaoMatriculas as fun_matricula

estudantes = [{"codigo_estudante": 1, "nome": "Gabryelly", "cpf": "123"}, {"codigo_estudante": 2, "nome": "Joao", "cpf": "456"}, {"codigo_estudante": 3, "nome": "Maria", "cpf": "789"}]
professores = [{"codigo_professor": 1, "nome": "Joao", "cpf": "123"}, {"codigo_professor": 2, "nome": "Maria", "cpf": "456"}, {"codigo_professor": 3, "nome": "Pedro", "cpf": "789"}]
disciplinas = [{"codigo_disciplina": 1, "nome": "Matematica", "codigo_professor": 1}, {"codigo_disciplina": 2, "nome": "Portugues", "codigo_professor": 2}, {"codigo_disciplina": 3, "nome": "Ingles", "codigo_professor": 3}]
turmas = [{"codigo_turma": 1, "codigo_professor": 1, "codigo_disciplina": 1}, {"codigo_turma": 2, "codigo_professor": 2, "codigo_disciplina": 2}, {"codigo_turma": 3, "codigo_professor": 3, "codigo_disciplina": 3}]
matriculas = [{"codigo_matricula": 1, "codigo_estudante": 1, "codigo_turma": 1}, {"codigo_matricula": 2, "codigo_estudante": 2, "codigo_turma": 2}, {"codigo_matricula": 3, "codigo_estudante": 3, "codigo_turma": 3}]



opcao = fun.menu_principal()
numero = 0

while opcao== "A" or opcao == "B" or opcao == "C" or opcao == "D" or opcao =="E":
      match opcao:
            case "A":
                  while True:
                        numero = fun.menu_secundario("Estudantes")
                        if numero == 1:
                              fun_estudante.editar_estudante(estudantes)
                        elif numero == 2:
                              fun.excluir_item(estudantes, "codigo_estudante")
                        elif numero == 3:
                              fun_estudante.cadastrar_estudante(estudantes)
                        elif numero == 4:
                              if not len(estudantes):
                                    print("Não há estudantes cadastrados\n")
                              else:
                                    fun_estudante.listar_estudantes(estudantes)
                        elif numero == 5:
                              break

            case "B":
                  while True:
                        numero = fun.menu_secundario("Disciplinas")
                        if numero == 1:
                              fun_disciplina.editar_disciplina(disciplinas)
                        elif numero == 2:
                              fun.excluir_item(disciplinas, "codigo_disciplina")
                        elif numero == 3:
                              fun_disciplina.cadastrar_disciplina(disciplinas)
                        elif numero == 4:
                              if not len(disciplinas):
                                    print("Não há disciplinas cadastrados\n")
                              else:
                                    fun_disciplina.listar_disciplina(disciplinas)
                        elif numero == 5:
                              break
            case "C":
                  while True:
                        numero = fun.menu_secundario("Matrículas")
                        if numero == 1:
                              fun_matricula.editar_matricula(matriculas, estudantes, turmas)
                        elif numero == 2:
                              fun.excluir_item(matriculas, "codigo_matricula")
                        elif numero == 3:
                              fun_matricula.criar_matricula(matriculas, estudantes, turmas)
                        elif numero == 4:
                              if not len(matriculas):
                                    print("Não há turmas cadastrados\n")
                              else:
                                    fun_matricula.listar_matricula(matriculas)
                        elif numero == 5:
                              break
            case "D":
                  while True:
                        numero = fun.menu_secundario("Professor")
                        if numero == 1:
                              fun_professor.editar_professor(professores)
                        elif numero == 2:
                              fun.excluir_item(professores, "codigo_professor")
                        elif numero == 3:
                              (fun_professor.cadastrar_professor(professores))
                        elif numero == 4:
                              if not len(professores):
                                    print("Não há professores cadastrados\n")
                              else:
                                    fun_professor.listar_professor(professores)
                        elif numero == 5:
                              break
            case "E":
                  while True:
                        numero = fun.menu_secundario("Turmas")
                        if numero == 1:
                              print("EM DESENVOLVIMENTO\n")
                        elif numero == 2:
                              fun.excluir_item(turmas, "codigo_turma")
                        elif numero == 3:
                              fun_turma.criar_turma(turmas, professores, disciplinas)
                        elif numero == 4:
                              if not len(turmas):
                                    print("Não há turas cadastrados\n")
                              else:
                                    fun_turma.listar_turma(turmas)
                        elif numero == 5:
                              break
            case _:
                  print("EM DESENVOLVIMENTO\n")

      opcao = fun.menu_principal()






